import os
import re
import glob
import yaml
import nltk
from pathlib import Path
from collections import Counter, defaultdict
import string
import unicodedata
from datetime import datetime
import unidecode
import types

# Configurações
NOTES_DIR = "10 - PERMANENT/Zettels/Yoga"
MOC_FILE = "30 - MPS OF CONTENT/Yoga MOC.md"
KEYWORDS_MIN_COUNT = 2  # Mínimo de ocorrências para considerar uma palavra-chave
SIMILARITY_THRESHOLD = 0.3  # Limiar para considerar notas relacionadas

# Baixar recursos do NLTK (rodar apenas uma vez)
def download_nltk_resources():
    """Baixar recursos do NLTK necessários para processamento de texto"""
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
    except LookupError:
        print("Baixando recursos NLTK básicos...")
        nltk.download('punkt')
        nltk.download('stopwords')

# Estrutura para armazenar dados das notas
class Note:
    def __init__(self, file_path, title, tags, content):
        self.file_path = file_path
        self.title = title
        self.tags = tags
        self.content = content
        self.keywords = []
        self.related_notes = []
        self.backlinks = []
        
    def __repr__(self):
        return f"Note('{self.title}', tags={self.tags})"

# Extrair metadados e conteúdo de uma nota
def parse_note(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extrair frontmatter YAML
    frontmatter_match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
    if not frontmatter_match:
        return None
    
    try:
        # Parsear YAML
        frontmatter = yaml.safe_load(frontmatter_match.group(1))
        
        # Extrair conteúdo principal (após o frontmatter)
        main_content = content[frontmatter_match.end():].strip()
        
        # Obter título e tags
        title = frontmatter.get('title', os.path.basename(file_path).replace('.md', ''))
        tags = frontmatter.get('tags', [])
        
        return Note(file_path, title, tags, main_content)
    except Exception as e:
        print(f"Erro ao processar {file_path}: {e}")
        return None

# Carregar todas as notas no diretório
def load_notes(directory):
    """Carrega todas as notas do diretório especificado."""
    notes = {}
    
    for file_path in glob.glob(f"{directory}/*.md"):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrair frontmatter
            frontmatter = {}
            if content.startswith('---'):
                _, fm, content_without_fm = content.split('---', 2)
                try:
                    frontmatter = yaml.safe_load(fm)
                    content = content_without_fm
                except Exception as e:
                    print(f"Erro ao processar frontmatter de {file_path}: {e}")
            
            # Extrair título da nota
            title = ""
            # Tentar extrair do frontmatter
            if frontmatter and 'title' in frontmatter:
                title = frontmatter['title']
            else:
                # Tentar extrair do primeiro cabeçalho
                title_match = re.search(r'^#\s+(.*?)$', content, re.MULTILINE)
                if title_match:
                    title = title_match.group(1)
                else:
                    # Usar o nome do arquivo como título
                    title = os.path.basename(file_path).replace('.md', '')
            
            # Usar o nome do arquivo sem a extensão como ID da nota
            file_id = os.path.basename(file_path).replace('.md', '')
            
            # Criar objeto Note com propriedades básicas
            note = types.SimpleNamespace()
            note.id = file_id
            note.title = title
            note.content = content
            note.frontmatter = frontmatter
            
            # Adicionar ao dicionário de notas
            notes[file_id] = note
            
        except Exception as e:
            print(f"Erro ao carregar {file_path}: {e}")
    
    print(f"Carregadas {len(notes)} notas.")
    return notes

# Extrair palavras-chave de uma nota
def extract_keywords(note, stopwords):
    # Remover pontuação e converter para minúsculas
    translator = str.maketrans('', '', string.punctuation)
    text = note.content.translate(translator).lower()
    
    # Tokenização simples usando espaços e pontuação
    words = text.split()
    
    # Remover stopwords e palavras muito curtas
    keywords = [word for word in words if word not in stopwords and len(word) > 3]
    
    # Contar frequência
    word_freq = Counter(keywords)
    
    # Selecionar palavras-chave com frequência acima do limiar
    note.keywords = [word for word, count in word_freq.items() 
                    if count >= KEYWORDS_MIN_COUNT]
    
    return note.keywords

# Calcular a similaridade entre duas notas
def calculate_similarity(note1, note2):
    # Se não houver palavras-chave, retorna 0
    if not note1.keywords or not note2.keywords:
        return 0
    
    # Conjunto de palavras-chave comuns
    common_keywords = set(note1.keywords) & set(note2.keywords)
    
    # Calcular similaridade Jaccard
    similarity = len(common_keywords) / len(set(note1.keywords) | set(note2.keywords))
    
    return similarity

def build_keyword_index(notes):
    """Cria um índice de palavras-chave para todas as notas."""
    keyword_index = {}
    
    for note_id, note in notes.items():
        # Usar o título e o conteúdo para extrair palavras-chave
        text = f"{note.title} {note.content}"
        
        # Tokenizar e normalizar o texto
        tokens = nltk.word_tokenize(text.lower())
        
        # Remover stopwords e palavras curtas
        stopwords = set(nltk.corpus.stopwords.words('portuguese') + 
                       nltk.corpus.stopwords.words('english'))
        filtered_tokens = [token for token in tokens 
                          if token not in stopwords and len(token) > 3]
        
        # Adicionar ao índice
        for token in set(filtered_tokens):  # Usar set para contar cada palavra apenas uma vez por nota
            if token not in keyword_index:
                keyword_index[token] = []
            keyword_index[token].append(note_id)
    
    return keyword_index

def find_related_notes(notes, keyword_index):
    """Encontra notas relacionadas com base em palavras-chave compartilhadas."""
    related_notes = {}
    
    for note_id, note in notes.items():
        # Obter palavras-chave desta nota
        text = f"{note.title} {note.content}"
        tokens = nltk.word_tokenize(text.lower())
        
        # Remover stopwords e palavras curtas
        stopwords = set(nltk.corpus.stopwords.words('portuguese') + 
                       nltk.corpus.stopwords.words('english'))
        keywords = set([token for token in tokens 
                      if token not in stopwords and len(token) > 3])
        
        # Encontrar notas que compartilham estas palavras-chave
        note_matches = {}
        for keyword in keywords:
            if keyword in keyword_index:
                for related_id in keyword_index[keyword]:
                    if related_id != note_id:
                        note_matches[related_id] = note_matches.get(related_id, 0) + 1
        
        # Ordenar por número de palavras-chave em comum
        sorted_matches = sorted(note_matches.items(), key=lambda x: x[1], reverse=True)
        
        # Armazenar as melhores correspondências
        if sorted_matches:
            related_notes[note_id] = sorted_matches[:10]  # Limitar a 10 por nota
    
    return related_notes

def find_backlinks(notes):
    """Encontra backlinks entre as notas."""
    backlinks = {}
    
    # Regex para encontrar links no formato [[path/to/file|display text]]
    link_pattern = re.compile(r'\[\[(.*?)(?:\|.*?)?\]\]')
    
    for note_id, note in notes.items():
        # Analisar o conteúdo em busca de links
        for match in link_pattern.finditer(note.content):
            link_path = match.group(1)
            
            # Extrair o nome do arquivo do link
            if '/' in link_path:
                linked_file = link_path.split('/')[-1]
            else:
                linked_file = link_path
            
            # Remover a extensão se existir
            if linked_file.endswith('.md'):
                linked_file = linked_file[:-3]
            
            # Encontrar a nota correspondente
            for linked_id, linked_note in notes.items():
                # Verificar se o nome do arquivo corresponde
                linked_basename = os.path.basename(linked_id)
                
                if linked_basename == linked_file or normalize_for_obsidian(linked_note.title.lower()) == linked_file:
                    # Adicionar backlink
                    if linked_id not in backlinks:
                        backlinks[linked_id] = []
                    
                    if note_id not in backlinks[linked_id]:
                        backlinks[linked_id].append(note_id)
    
    return backlinks

# Sugerir links para adicionar às notas
def suggest_links(notes, related_notes, backlinks):
    """Sugere links para adicionar nas notas."""
    suggestions = {}
    
    for note_id, note in notes.items():
        # Combinar notas relacionadas e backlinks para este documento
        note_suggestions = []
        
        # Adicionar notas relacionadas por palavras-chave
        if note_id in related_notes:
            for related_id, _ in related_notes[note_id]:
                # Evitar auto-referência
                if related_id != note_id:
                    note_suggestions.append(notes[related_id])
        
        # Adicionar backlinks encontrados
        if note_id in backlinks:
            for backlink_id in backlinks[note_id]:
                # Evitar duplicatas
                if notes[backlink_id] not in note_suggestions and backlink_id != note_id:
                    note_suggestions.append(notes[backlink_id])
        
        # Ordenar por título para consistência
        note_suggestions.sort(key=lambda n: n.title)
        
        if note_suggestions:
            suggestions[note_id] = note_suggestions
    
    return suggestions

# Atualizar o MOC com novos links e seções
def update_moc(moc_file, all_notes):
    """Update the Map of Content with links to all notes."""
    # Regex for extracting section numbers from titles
    section_pattern = r'^(\d+(?:\.\d+)*)\s*[-–—]\s*(.+)$'
    
    def extract_section_number(title):
        match = re.match(section_pattern, title)
        if match:
            num_parts = match.group(1).split('.')
            # Convert each part to integer for proper numerical sorting
            return tuple(int(part) for part in num_parts)
        return None

    # Group notes by their main section number
    sections_by_main_number = {}
    additional_topics = []
    
    for note in all_notes:
        section_tuple = extract_section_number(note.title)
        if section_tuple:
            main_number = section_tuple[0]  # Get the first number as the main section
            if main_number not in sections_by_main_number:
                sections_by_main_number[main_number] = []
            sections_by_main_number[main_number].append(note)
        else:
            additional_topics.append(note)
    
    # Sort the main sections numerically
    main_sections = []
    for main_number in sorted(sections_by_main_number.keys()):
        # Sort subsections within each main section
        notes = sorted(sections_by_main_number[main_number], 
                      key=lambda note: extract_section_number(note.title) or (0,))
        main_sections.append(notes[0])  # Add the main section note
        
        # Collect subsections (those with more than one number part)
        subsections = [note for note in notes if len((extract_section_number(note.title) or (0,))) > 1]
        if subsections:
            sections_by_main_number[main_number] = subsections
        else:
            sections_by_main_number[main_number] = []
    
    # Extract subsections from note content for enhanced linking
    note_subsections = {}
    
    # Parse all notes to find subsections (### headers)
    for note in all_notes:
        subsection_pattern = re.compile(r'###\s+(.*?)(?=\n#|\Z)', re.DOTALL | re.MULTILINE)
        subsections = subsection_pattern.findall(note.content)
        if subsections:
            note_subsections[note.id] = [subsec.strip() for subsec in subsections]
    
    # Now create the MOC content
    content = []
    content.append("---")
    content.append("id: YogaMOC")
    content.append('title: "Mapa de Conteúdo: Trato de Yôga"')
    content.append("tags:")
    content.append("  - type/moc")
    content.append("  - theme/yoga")
    content.append("created: 2025-04-18")
    content.append(f"updated: {datetime.now().strftime('%Y-%m-%dT%H:%M')}")
    content.append("---")
    content.append("")
    content.append("# 🧘 Mapa de Conteúdo: Trato de Yôga")
    content.append("")
    content.append("Este MOC (Map of Content) organiza as notas do Trato de Yôga do Mestre De Rose.")
    content.append("")
    content.append("## 📚 Seções Principais")
    content.append("")
    
    # Add main sections in numerical order
    sorted_main_sections = sorted(main_sections, key=lambda note: extract_section_number(note.title) or (0,))
    for note in sorted_main_sections:
        normalized_title = normalize_for_obsidian(note.title.lower())
        link = f"- [[10 - PERMANENT/Zettels/Yoga/{normalized_title}|{note.title}]]"
        content.append(link)
    
    content.append("")
    content.append("## 🔍 Subseções por Tópico")
    content.append("")
    
    # Add subsections grouped by their main section
    for main_number in sorted(sections_by_main_number.keys()):
        if sections_by_main_number[main_number]:  # If there are subsections
            # Find the main section note to get its title
            main_section = next((note for note in main_sections if extract_section_number(note.title)[0] == main_number), None)
            if main_section:
                main_section_normalized = normalize_for_obsidian(main_section.title.lower())
                main_section_link = f"### [[10 - PERMANENT/Zettels/Yoga/{main_section_normalized}|{main_section.title}]]"
                content.append("")
                content.append(main_section_link)
                content.append("")
                
                # Add all subsections for this main section with proper Obsidian links
                for note in sorted(sections_by_main_number[main_number], 
                                  key=lambda note: extract_section_number(note.title) or (0,)):
                    normalized_title = normalize_for_obsidian(note.title.lower())
                    link = f"- [[10 - PERMANENT/Zettels/Yoga/{normalized_title}|{note.title}]]"
                    content.append(link)
                
                # Also add any subsections (### headers) found in the main section note's content
                if main_section.id in note_subsections and note_subsections[main_section.id]:
                    content.append("")
                    content.append("#### Tópicos internos:")
                    content.append("")
                    for subsection in note_subsections[main_section.id]:
                        # Create a link to the main section with a heading anchor
                        anchor = subsection.lower().replace(' ', '-').replace(',', '').replace('(', '').replace(')', '')
                        anchor = ''.join(c for c in unicodedata.normalize('NFD', anchor) if not unicodedata.combining(c))
                        link = f"- [[10 - PERMANENT/Zettels/Yoga/{main_section_normalized}#{anchor}|{subsection}]]"
                        content.append(link)
    
    # Add other topics that don't have section numbers
    if additional_topics:
        content.append("")
        content.append("### Outros Tópicos")
        content.append("")
        for note in sorted(additional_topics, key=lambda note: note.title):
            normalized_title = normalize_for_obsidian(note.title.lower())
            link = f"- [[10 - PERMANENT/Zettels/Yoga/{normalized_title}|{note.title}]]"
            content.append(link)
    
    # Write the content to the MOC file
    with open(moc_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    print(f"MOC atualizado com {len(sections_by_main_number)} seções principais organizadas")
    print(f"MOC atualizado com {len(all_notes)} notas organizadas")
    print("Links nas seções principais e subseções atualizados.")

# Atualizar notas com links sugeridos
def update_notes_with_links(notes, suggestions):
    """Atualiza as notas com links sugeridos."""
    updated_count = 0
    
    for note_id, suggested_links in suggestions.items():
        if not suggested_links:
            continue
        
        note = notes[note_id]
        note_path = f"{NOTES_DIR}/{note_id}.md"
        
        try:
            # Ler o conteúdo atual
            with open(note_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Verificar se já tem uma seção de links sugeridos
            section_marker = "## Links Sugeridos"
            
            # Preparar os novos links
            new_links = [f"- [[10 - PERMANENT/Zettels/Yoga/{normalize_for_obsidian(related_note.title.lower())}.md|{related_note.title}]]" 
                         for related_note in suggested_links]
            
            if section_marker in content:
                # Atualizar a seção existente
                before_section = content.split(section_marker)[0]
                new_content = f"{before_section}{section_marker}\n\n" + "\n".join(new_links)
            else:
                # Adicionar nova seção no final
                new_content = f"{content}\n\n{section_marker}\n\n" + "\n".join(new_links)
            
            # Escrever o conteúdo atualizado
            with open(note_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            updated_count += 1
            
        except Exception as e:
            print(f"Erro ao atualizar links para {note_id}: {e}")
    
    return updated_count

def update_section_links(moc_file):
    """Atualiza os links nas seções principais do MOC para o formato wiki completo."""
    try:
        # Ler o conteúdo atual do MOC
        with open(moc_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Encontrar a seção "Seções Principais"
        sections_match = re.search(r'## 🔍 Por Categorias\s+(.*?)(?=##|\Z)', content, re.DOTALL)
        if not sections_match:
            sections_match = re.search(r'## 📚 Seções Principais\s+(.*?)(?=##|\Z)', content, re.DOTALL)
            if not sections_match:
                print(f"Aviso: Seção 'Seções Principais' não encontrada no MOC {moc_file}")
                return False
        
        sections_content = sections_match.group(1).strip()
        
        # Padrão para encontrar links de texto simples
        # Formato: * Título ou • Título
        text_link_pattern = re.compile(r'[•\*]\s+([^*•\[\]]+)(?=$|\n)')
        
        # Substituir links de texto por links wiki
        def replace_text_with_wiki_link(match):
            text = match.group(1).strip()
            
            # Converter o texto para o formato de arquivo
            file_name = text.lower().replace(' ', '-').replace(',', '').replace('(', '').replace(')', '').replace('*', '')
            
            # Normalizar para remover acentos
            file_name = ''.join(c for c in unicodedata.normalize('NFD', file_name) if not unicodedata.combining(c))
            
            return f"* [[10 - PERMANENT/Zettels/Yoga/{file_name}|{text}]]"
        
        updated_sections = text_link_pattern.sub(replace_text_with_wiki_link, sections_content)
        
        # Atualizar o conteúdo do MOC
        new_content = content.replace(sections_content, updated_sections)
        
        # Escrever o conteúdo atualizado no arquivo
        with open(moc_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    
    except Exception as e:
        print(f"Erro ao atualizar links das seções: {e}")
        return False

def normalize_for_obsidian(text):
    """Normalize text for Obsidian filename compatibility."""
    # Remove special characters that might cause issues in filenames
    # Keep hyphens, numbers, and letters
    normalized = re.sub(r'[^a-zA-Z0-9\u00C0-\u00FF\s\-]', '', text)
    
    # Replace spaces with hyphens
    normalized = re.sub(r'\s+', '-', normalized.strip())
    
    # Convert to lowercase
    normalized = normalized.lower()
    
    # Replace accented characters
    normalized = unidecode.unidecode(normalized)
    
    return normalized

# Função principal
def main():
    """Função principal para processar notas e sugerir links."""
    try:
        # Carregar notas
        print(f"Carregando notas de {NOTES_DIR}...")
        notes = load_notes(NOTES_DIR)
        
        # Extrair palavras-chave
        print("Extraindo palavras-chave...")
        keyword_index = build_keyword_index(notes)
        
        # Encontrar notas relacionadas
        print("Encontrando notas relacionadas...")
        related_notes = find_related_notes(notes, keyword_index)
        
        # Encontrar backlinks
        print("Encontrando backlinks...")
        backlinks = find_backlinks(notes)
        
        # Sugerir links
        print("Sugerindo links para adicionar...")
        suggestions = suggest_links(notes, related_notes, backlinks)
        
        # Contar quantas notas têm sugestões
        notes_with_suggestions = sum(1 for note_id in suggestions if suggestions[note_id])
        print(f"Foram encontradas sugestões para {notes_with_suggestions} notas.")
        
        # Atualizar o MOC
        print("Atualizando MOC...")
        update_moc(MOC_FILE, list(notes.values()))
        
        # Atualizar notas com links sugeridos
        print("Atualizando notas com links sugeridos...")
        updated_count = update_notes_with_links(notes, suggestions)
        print(f"Atualizadas {updated_count} notas com novos links sugeridos.")
        
        print("Processo concluído!")
        return True
        
    except Exception as e:
        print(f"Erro durante o processamento: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main() 