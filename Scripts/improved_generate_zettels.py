#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def extract_sections_improved(content):
    """
    Extrai seções do conteúdo com base na estrutura de cabeçalhos, preservando hierarquia.
    Identifica corretamente os limites de cada seção e subseção.
    """
    # Separar YAML frontmatter
    frontmatter_pattern = re.compile(r'^---\n.*?\n---\n', re.DOTALL)
    frontmatter_match = frontmatter_pattern.match(content)
    frontmatter = ""
    
    if frontmatter_match:
        frontmatter = frontmatter_match.group(0)
        content = content[len(frontmatter):]

    # Padrão para identificar cabeçalhos em markdown
    header_pattern = re.compile(r'^(#+)\s+(.*?)$', re.MULTILINE)
    
    # Encontrar todos os cabeçalhos
    headers = []
    for match in header_pattern.finditer(content):
        level = len(match.group(1))  # Número de # no cabeçalho
        title = match.group(2).strip()
        position = match.start()
        headers.append((level, title, position))
    
    # Adicionar posição final (fim do documento)
    headers.append((0, "", len(content)))
    
    # Extrair numeração e título limpo
    number_pattern = re.compile(r'^(\d+(\.\d+)*)\s*(.*?)$')
    
    # Construir seções
    sections = []
    for i in range(len(headers) - 1):
        level, title, start = headers[i]
        next_level, _, end = headers[i+1]
        
        # Verificar se tem numeração
        number_match = number_pattern.match(title)
        if number_match:
            section_number = number_match.group(1)  # Capturar a numeração (ex: "5.1.2")
            clean_title = number_match.group(3).strip()  # Capturar o título sem a numeração
        else:
            section_number = None
            clean_title = title.strip()
        
        # Determinar tipo de seção
        section_type = ""
        if level == 1:
            section_type = "section"
        elif level == 2:
            section_type = "subsection"
        elif level == 3:
            section_type = "subsubsection"
        
        # Extrair o conteúdo completo (incluindo o cabeçalho)
        header_line_length = len(f"{'#' * level} {title}") + 1  # +1 para o \n
        section_content = content[start:end]
        
        sections.append({
            'title': clean_title,
            'number': section_number,
            'full_title': title,
            'level': level,
            'start': start,
            'end': end,
            'content': section_content,
            'type': section_type
        })
    
    return sections, frontmatter

def enhance_markdown_content(content, section):
    """
    Melhora o conteúdo do markdown com formatação adicional,
    links para seções relacionadas, etc.
    """
    # Extrair links mencionados no texto
    link_pattern = re.compile(r'\b(Yôga|Pránáyáma|Ásana|Mantra|Tantra|SwáSthya|Súrya|Chandra|Samádhi)\b')
    
    # Adicionar tags relacionadas ao conteúdo
    related_tags = []
    if re.search(r'\bpránáyáma\b|\brespiração\b|\brespiratório\b', content.lower()):
        related_tags.append("theme/pranayama")
    if re.search(r'\básana\b|\bpostura\b', content.lower()):
        related_tags.append("theme/asana")
    if re.search(r'\bmeditação\b|\bdhyána\b|\bconcentração\b', content.lower()):
        related_tags.append("theme/meditacao")
    if re.search(r'\bmantra\b|\bsom\b|\bvocalização\b', content.lower()):
        related_tags.append("theme/mantra")
    if re.search(r'\bchakra\b|\benergia\b|\bkundaliní\b', content.lower()):
        related_tags.append("theme/energia")
    
    return content, related_tags

def generate_frontmatter(title, section_number=None, section_type="concept", additional_tags=None):
    """Gera o frontmatter YAML para o arquivo markdown."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%dT%H:%M")
    
    # Determinar tags com base no título e conteúdo
    tags = ["source/trato-yoga"]
    
    # Adicionar tag de tipo com base em heurísticas simples
    if section_type == "concept" or any(keyword in title.lower() for keyword in ["definição", "o que é", "conceito", "tipos"]):
        tags.append("type/concept")
    elif section_type == "practice" or any(keyword in title.lower() for keyword in ["técnica", "prática", "exercício", "como"]):
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
    
    # Adicionar tags adicionais encontradas no conteúdo
    if additional_tags:
        for tag in additional_tags:
            if tag not in tags:
                tags.append(tag)
    
    # Adicionar a numeração original ao título se disponível
    display_title = title
    if section_number:
        display_title = f"{section_number} – {title}"
    
    # Formatar as tags como YAML
    tags_formatted = "\n  - ".join(tags)
    tags_formatted = "  - " + tags_formatted
    
    return f"""---
id: {timestamp}
title: {display_title}
tags:
{tags_formatted}
zettel-type: literature
source: Trato de Yôga do Mestre De Rose
created: {date_str}
updated: {time_str}
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
    """Processa e formata o conteúdo markdown."""
    # Melhorar a formatação de listas
    content = re.sub(r'    - ', r'- ', content)
    
    # Limpar linhas vazias excessivas
    content = re.sub(r'\n{3,}', r'\n\n', content)
    
    # Adicionar seção para links e referências se não estiver vazia
    if not re.search(r'## 🔗 Links e Referências', content):
        content += "\n\n## 🔗 Links e Referências"
    
    return content

def split_into_zettels_improved(input_file, output_dir):
    """Divide o documento em zettels individuais preservando o conteúdo completo."""
    try:
        # Criar diretório de saída se não existir
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Ler o conteúdo do arquivo
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrair seções
        sections, frontmatter = extract_sections_improved(content)
        
        if not sections:
            print(f"AVISO: Nenhuma seção encontrada no arquivo {input_file}")
            return []
        
        # Criar um zettel para cada seção
        created_zettels = []
        for section in sections:
            if not section['title']:
                continue
                
            # Extrair e melhorar conteúdo da seção
            section_content = section['content']
            enhanced_content, additional_tags = enhance_markdown_content(section_content, section)
            processed_content = process_content(enhanced_content)
            
            # Determinar tipo de seção
            section_type = "concept"
            if re.search(r'técnica|prática|exercício|como', section['title'].lower()) or section['title'].lower().startswith('como'):
                section_type = "practice"
            
            # Gerar frontmatter
            frontmatter = generate_frontmatter(
                section['title'], 
                section['number'], 
                section_type,
                additional_tags
            )
            
            # Criar nome de arquivo
            filename = create_zettel_filename(section['title'], section['number'])
            output_path = os.path.join(output_dir, filename)
            
            # Escrever o arquivo
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter + processed_content)
                
            created_zettels.append({
                'title': section['title'],
                'number': section['number'],
                'filename': filename,
                'full_title': section['full_title'],
                'level': section['level']
            })
            
            print(f"Criado zettel: {filename}")
        
        return created_zettels
    except Exception as e:
        print(f"ERRO ao processar arquivo {input_file}: {str(e)}")
        import traceback
        traceback.print_exc()
        return []

def create_moc_improved(zettels, moc_file):
    """Cria um Mapa de Conteúdo (MOC) melhorado para os zettels."""
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
        
        # Organizar zettels por hierarquia
        by_level = {}
        for zettel in zettels:
            level = zettel.get('level', 1)  # Nível default é 1 se não foi especificado
            if level not in by_level:
                by_level[level] = []
            by_level[level].append(zettel)
        
        # Separar notas com e sem numeração
        numbered_zettels = [z for z in zettels if z['number']]
        unnumbered_zettels = [z for z in zettels if not z['number']]
        
        # Ordenar zettels numerados
        def number_key(zettel):
            if not zettel['number']:
                return []
            return [int(n) if n.isdigit() else n for n in re.split(r'[.-]', zettel['number'])]
        
        numbered_zettels.sort(key=number_key)
        
        # Adicionar zettels numerados ao MOC usando indentação baseada na hierarquia
        for zettel in numbered_zettels:
            depth = 0
            if zettel['number']:
                # Calcular profundidade pela quantidade de pontos na numeração
                depth = zettel['number'].count('.')
            
            indent = "  " * depth
            
            filename = zettel['filename'].replace('.md', '')
            moc_content += f"{indent}- [[10 - PERMANENT/Zettels/Yoga/{filename}|{zettel['full_title']}]]\n"
        
        # Adicionar zettels não numerados
        if unnumbered_zettels:
            moc_content += "\n## 📌 Tópicos Adicionais\n\n"
            
            # Ordenar alfabeticamente
            unnumbered_zettels.sort(key=lambda z: z['title'])
            
            for zettel in unnumbered_zettels:
                filename = zettel['filename'].replace('.md', '')
                moc_content += f"- [[10 - PERMANENT/Zettels/Yoga/{filename}|{zettel['title']}]]\n"
        
        # Adicionar seções temáticas
        moc_content += """
## 🔍 Por Temas

### Práticas e Técnicas
```dataview
TABLE tags as "Tags"
FROM [[#]] AND #theme/pranayama OR #theme/asana OR #theme/mantra
SORT file.name ASC
```

### Filosofia e Conceitos
```dataview
TABLE tags as "Tags" 
FROM [[#]] AND #type/concept AND NOT #theme/pranayama AND NOT #theme/asana
SORT file.name ASC
```

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
        return True
    except Exception as e:
        print(f"ERRO ao criar MOC {moc_file}: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def main():
    try:
        parser = argparse.ArgumentParser(description="Gera notas Zettelkasten a partir de arquivo Markdown.")
        
        parser.add_argument("input_file", nargs="?", default=DEFAULT_INPUT_FILE,
                          help=f"Caminho para o arquivo de entrada (padrão: {DEFAULT_INPUT_FILE})")
        
        parser.add_argument("--output", "-o", 
                          default=DEFAULT_OUTPUT_DIR,
                          help=f"Diretório de saída para os Zettels (padrão: {DEFAULT_OUTPUT_DIR})")
        
        parser.add_argument("--moc", "-m", 
                          default=DEFAULT_MOC_FILE,
                          help=f"Caminho para o arquivo MOC de saída (padrão: {DEFAULT_MOC_FILE})")
        
        parser.add_argument("--clean", "-c", action="store_true",
                          help="Limpar diretório de saída antes de gerar novos zettels")
        
        parser.add_argument("--verbose", "-v", action="store_true",
                          help="Mostrar informações detalhadas durante o processamento")
        
        args = parser.parse_args()
        
        # Verificar se o arquivo de entrada existe
        input_file = args.input_file
        if not os.path.exists(input_file):
            print(f"ERRO: Arquivo de entrada '{input_file}' não encontrado.")
            sys.exit(1)
            
        print(f"Processando arquivo: {input_file}")
        print(f"Diretório de saída: {args.output}")
        print(f"Arquivo MOC: {args.moc}")
        
        # Limpar diretório se solicitado
        if args.clean and os.path.exists(args.output):
            print(f"Limpando diretório de saída: {args.output}")
            for file in os.listdir(args.output):
                file_path = os.path.join(args.output, file)
                if os.path.isfile(file_path) and file.endswith('.md'):
                    os.remove(file_path)
                    if args.verbose:
                        print(f"  Removido: {file}")
        
        # Gerar zettels
        zettels = split_into_zettels_improved(input_file, args.output)
        
        if not zettels:
            print("ERRO: Nenhum zettel foi criado.")
            sys.exit(1)
        
        # Criar MOC
        moc_success = create_moc_improved(zettels, args.moc)
        
        if moc_success:
            print(f"Processo concluído! Criados {len(zettels)} zettels.")
        else:
            print("AVISO: Processo concluído, mas houve problemas ao criar o MOC.")
        
    except Exception as e:
        print(f"ERRO: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 