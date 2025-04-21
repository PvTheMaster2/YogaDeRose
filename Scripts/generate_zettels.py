from pathlib import Path
import re
import os
from datetime import datetime
import unicodedata
import argparse
import yaml
import sys

# Configurações padrão
DEFAULT_INPUT_FILE = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned_utf8.md"
DEFAULT_OUTPUT_DIR = "10 - PERMANENT/Zettels/Yoga"
DEFAULT_MOC_FILE = "30 - MPS OF CONTENT/Yoga MOC.md"

def normalize_filename(text):
    """Normaliza o texto para criar um nome de arquivo válido."""
    # Converter para minúsculas e remover acentos
    text = text.lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if not unicodedata.combining(c))
    
    # Substituir espaços por hífens e remover caracteres especiais
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    
    return text

def extract_sections(content):
    """Extrai seções do conteúdo com base na estrutura de cabeçalhos."""
    # Padrão para identificar seções numeradas no formato LaTeX
    section_pattern = re.compile(r'\\section\{(.*?)\}|\\subsection\{(.*?)\}|\\subsubsection\{(.*?)\}|^#+\s*(.*?)$', re.MULTILINE)
    
    # Padrão para capturar a numeração original da seção (ex: 5.1.2)
    number_pattern = re.compile(r'^(\d+(\.\d+)*)\s*(.*?)$')
    
    sections = []
    current_position = 0
    
    # Encontrar todos os cabeçalhos
    for match in section_pattern.finditer(content):
        # Determinar o título da seção
        title = None
        for group in match.groups():
            if group:
                title = group
                break
        
        if not title:
            continue
            
        # Verificar se o título possui numeração no formato "X.Y.Z Título"
        number_match = number_pattern.match(title)
        if number_match:
            section_number = number_match.group(1)  # Capturar a numeração (ex: "5.1.2")
            clean_title = number_match.group(3).strip()  # Capturar o título sem a numeração
        else:
            section_number = None
            clean_title = title.strip()
        
        # Registrar a seção encontrada
        start_pos = match.end()
        sections.append({
            'title': clean_title,
            'number': section_number,
            'start': start_pos,
            'full_title': title.strip()
        })
    
    # Definir os limites de cada seção
    for i in range(len(sections) - 1):
        sections[i]['end'] = sections[i + 1]['start']
    
    # A última seção vai até o final do conteúdo
    if sections:
        sections[-1]['end'] = len(content)
    
    return sections

def generate_frontmatter(title, section_number=None):
    """Gera o frontmatter YAML para o arquivo markdown."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    date_str = now.strftime("%Y-%m-%d")
    
    # Determinar tags com base no título e conteúdo
    tags = ["source/trato-yoga"]
    
    # Adicionar tag de tipo com base em heurísticas simples
    if any(keyword in title.lower() for keyword in ["definição", "o que é", "conceito"]):
        tags.append("type/concept")
    elif any(keyword in title.lower() for keyword in ["técnica", "prática", "exercício", "como"]):
        tags.append("type/practice")
    else:
        tags.append("type/concept")
    
    # Adicionar tags temáticas com base em heurísticas
    if any(keyword in title.lower() for keyword in ["pranayama", "respiração", "respiratório"]):
        tags.append("theme/pranayama")
    elif any(keyword in title.lower() for keyword in ["asana", "postura"]):
        tags.append("theme/asana")
    elif any(keyword in title.lower() for keyword in ["meditação", "dhyana", "concentração"]):
        tags.append("theme/meditacao")
    elif any(keyword in title.lower() for keyword in ["mantra", "som"]):
        tags.append("theme/mantra")
    elif any(keyword in title.lower() for keyword in ["chakra", "energia", "kundalini"]):
        tags.append("theme/energia")
    else:
        tags.append("theme/yoga")
    
    # Formatar as tags corretamente para YAML
    tags_str = ", ".join([f'"{tag}"' for tag in tags])
    
    # Adicionar a numeração original ao título se disponível
    display_title = title
    if section_number:
        display_title = f"{section_number} – {title}"
    
    return f"""---
id: {timestamp}
title: "{display_title}"
tags: [{tags_str}]
zettel-type: literature
source: "Trato de Yôga do Mestre De Rose"
created: {date_str}
---

# {display_title}

"""

def create_zettel_filename(title, section_number=None):
    """Cria um nome de arquivo adequado para o zettel."""
    # Se houver numeração de seção, incluí-la no nome do arquivo
    if section_number:
        # Substituir pontos por hífen para manter a estrutura
        clean_number = section_number.replace('.', '-')
        normalized_title = normalize_filename(title)
        return f"{clean_number}-{normalized_title}.md"
    else:
        return f"{normalize_filename(title)}.md"

def process_content(content):
    """Processa o conteúdo para formatação markdown adequada."""
    # Limpar formatação LaTeX
    content = re.sub(r'\\textit\{(.*?)\}', r'*\1*', content)  # Itálico
    content = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', content)  # Negrito
    content = re.sub(r'\\section\{(.*?)\}', r'## \1', content)  # Seção -> h2
    content = re.sub(r'\\subsection\{(.*?)\}', r'### \1', content)  # Subseção -> h3
    content = re.sub(r'\\subsubsection\{(.*?)\}', r'#### \1', content)  # Subsubseção -> h4
    
    # Outras limpezas de LaTeX
    content = re.sub(r'\\begin\{.*?\}|\\end\{.*?\}', '', content)
    content = re.sub(r'\\item', '-', content)
    
    return content

def split_into_zettels(input_file, output_dir):
    """Divide o documento em zettels individuais."""
    try:
        # Criar diretório de saída se não existir
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Ler o conteúdo do arquivo
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrair seções
        sections = extract_sections(content)
        
        if not sections:
            print(f"AVISO: Nenhuma seção encontrada no arquivo {input_file}")
            return []
        
        # Criar um zettel para cada seção
        created_zettels = []
        for section in sections:
            if not section['title']:
                continue
                
            # Extrair conteúdo da seção
            section_content = content[section['start']:section['end']]
            section_content = process_content(section_content)
            
            # Gerar frontmatter
            frontmatter = generate_frontmatter(section['title'], section['number'])
            
            # Criar nome de arquivo
            filename = create_zettel_filename(section['title'], section['number'])
            output_path = os.path.join(output_dir, filename)
            
            # Escrever o arquivo
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter + section_content)
                
            created_zettels.append({
                'title': section['title'],
                'number': section['number'],
                'filename': filename,
                'full_title': section['full_title']
            })
            
            print(f"Criado zettel: {filename}")
        
        return created_zettels
    except Exception as e:
        print(f"ERRO ao processar arquivo {input_file}: {str(e)}")
        return []

def create_moc(zettels, moc_file):
    """Cria um Mapa de Conteúdo (MOC) para os zettels."""
    try:
        # Preparar conteúdo do MOC
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        datetime_str = now.strftime("%Y-%m-%dT%H:%M")
        
        moc_content = f"""---
id: YogaMOC
title: "Mapa de Conteúdo: Trato de Yôga"
tags:
  - type/moc
  - theme/yoga
created: {date_str}
updated: {datetime_str}
---

# 🧘 Mapa de Conteúdo: Trato de Yôga

Este MOC (Map of Content) organiza as notas do Trato de Yôga do Mestre De Rose.

## 📚 Seções Principais

"""
        
        # Organizar zettels por numeração para manter a hierarquia original
        # Primeiro, vamos separar os que têm numeração dos que não têm
        numbered_zettels = [z for z in zettels if z['number']]
        unnumbered_zettels = [z for z in zettels if not z['number']]
        
        # Ordenar zettels numerados pela numeração
        # Converter a numeração para uma lista de inteiros para comparação correta
        def number_key(zettel):
            if not zettel['number']:
                return []
            return [int(n) for n in zettel['number'].split('.')]
        
        numbered_zettels.sort(key=number_key)
        
        # Adicionar zettels numerados ao MOC
        for zettel in numbered_zettels:
            # Calcular a indentação com base na profundidade da numeração
            depth = len(zettel['number'].split('.')) - 1
            indent = "  " * depth
            
            filename = zettel['filename'].replace('.md', '')
            moc_content += f"{indent}- [[10 - PERMANENT/Zettels/Yoga/{filename}|{zettel['full_title']}]]\n"
        
        # Adicionar zettels não numerados ao final
        if unnumbered_zettels:
            moc_content += "\n## 📌 Tópicos Adicionais\n\n"
            
            # Ordenar alfabeticamente
            unnumbered_zettels.sort(key=lambda z: z['title'])
            
            for zettel in unnumbered_zettels:
                filename = zettel['filename'].replace('.md', '')
                moc_content += f"- [[10 - PERMANENT/Zettels/Yoga/{filename}|{zettel['title']}]]\n"
        
        # Adicionar seção para dataview
        moc_content += """

## 🔍 Todas as Notas

```dataview
TABLE tags AS "Tags", source AS "Fonte"
FROM [[#]]
WHERE contains(tags, "source/trato-yoga")
SORT file.name ASC
```
"""
        
        # Escrever o arquivo MOC
        Path(os.path.dirname(moc_file)).mkdir(parents=True, exist_ok=True)
        with open(moc_file, 'w', encoding='utf-8') as f:
            f.write(moc_content)
            
        print(f"Criado MOC: {moc_file}")
    except Exception as e:
        print(f"ERRO ao criar MOC {moc_file}: {str(e)}")

def main():
    try:
        parser = argparse.ArgumentParser(description="Gera notas Zettelkasten a partir de arquivo Markdown/LaTeX.")
        
        parser.add_argument("input_file", nargs="?", default=DEFAULT_INPUT_FILE,
                          help=f"Caminho para o arquivo de entrada (padrão: {DEFAULT_INPUT_FILE})")
        
        parser.add_argument("--output", "-o", 
                          default=DEFAULT_OUTPUT_DIR,
                          help=f"Diretório de saída para os Zettels (padrão: {DEFAULT_OUTPUT_DIR})")
        
        parser.add_argument("--moc", "-m", 
                          default=DEFAULT_MOC_FILE,
                          help=f"Caminho para o arquivo MOC de saída (padrão: {DEFAULT_MOC_FILE})")
        
        args = parser.parse_args()
        
        # Verificar se o arquivo de entrada existe
        input_file = args.input_file
        if not os.path.exists(input_file):
            print(f"ERRO: Arquivo de entrada '{input_file}' não encontrado.")
            sys.exit(1)
            
        print(f"Processando arquivo: {input_file}")
        print(f"Diretório de saída: {args.output}")
        print(f"Arquivo MOC: {args.moc}")
        
        # Dividir em zettels
        zettels = split_into_zettels(input_file, args.output)
        
        if not zettels:
            print("ERRO: Nenhum zettel foi criado.")
            sys.exit(1)
        
        # Criar MOC
        create_moc(zettels, args.moc)
        
        print(f"Processo concluído! Criados {len(zettels)} zettels.")
        
    except Exception as e:
        print(f"ERRO: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 