import os
import re
import glob
from datetime import datetime
import yaml
import shutil

# Configurações
NOTES_DIR = "10 - PERMANENT/Zettels/Yoga"
MOC_FILE = "30 - MPS OF CONTENT/Yoga MOC.md"

def normalize_for_obsidian(text):
    """Normalize text for Obsidian filename compatibility."""
    # Remove special characters that might cause issues in filenames
    normalized = re.sub(r'[^a-zA-Z0-9\u00C0-\u00FF\s\-]', '', text)
    
    # Replace spaces with hyphens
    normalized = re.sub(r'\s+', '-', normalized.strip())
    
    # Convert to lowercase
    normalized = normalized.lower()
    
    return normalized

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
            
            # Criar objeto Note simples
            note = type('Note', (), {})
            note.title = title
            note.content = content
            note.frontmatter = frontmatter
            note.file_path = file_path
            
            # Adicionar ao dicionário de notas
            notes[os.path.basename(file_path).replace('.md', '')] = note
            
        except Exception as e:
            print(f"Erro ao carregar {file_path}: {e}")
    
    print(f"Carregadas {len(notes)} notas.")
    return notes

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
    
    for note in all_notes.values():
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
        file_name = os.path.basename(note.file_path)
        link = f"- [[10 - PERMANENT/Zettels/Yoga/{file_name}|{note.title}]]"
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
                content.append("")
                content.append(f"### {main_section.title}")
                content.append("")
                
                # Add all subsections for this main section
                sorted_subsections = sorted(sections_by_main_number[main_number], 
                                           key=lambda note: extract_section_number(note.title) or (0,))
                for note in sorted_subsections:
                    file_name = os.path.basename(note.file_path)
                    link = f"- [[10 - PERMANENT/Zettels/Yoga/{file_name}|{note.title}]]"
                    content.append(link)
    
    # Add other topics that don't have section numbers
    if additional_topics:
        content.append("")
        content.append("### Outros Tópicos")
        content.append("")
        for note in sorted(additional_topics, key=lambda note: note.title):
            file_name = os.path.basename(note.file_path)
            link = f"- [[10 - PERMANENT/Zettels/Yoga/{file_name}|{note.title}]]"
            content.append(link)
    
    # Write the content to the MOC file
    with open(moc_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))
    
    print(f"MOC atualizado com {len(sections_by_main_number)} seções principais organizadas")
    print(f"MOC atualizado com {len(all_notes)} notas organizadas")
    print("Links nas seções principais atualizados.")

def main():
    """Função principal."""
    try:
        # Carregar notas
        print(f"Carregando notas de {NOTES_DIR}...")
        notes = load_notes(NOTES_DIR)
        
        # Atualizar o MOC
        print("Atualizando MOC...")
        update_moc(MOC_FILE, notes)
        
        print("Processo concluído!")
        return True
        
    except Exception as e:
        print(f"Erro durante o processamento: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main() 