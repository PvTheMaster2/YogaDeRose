#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path
import unicodedata
import argparse

# Configurações padrão
DEFAULT_INPUT_FILE = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned_utf8.md"
DEFAULT_OUTPUT_DIR = "10 - PERMANENT/Zettels/Yoga"

def normalize_filename(text):
    """Normaliza o texto para ser usado como nome de arquivo"""
    # Remover caracteres especiais e acentos
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    # Substituir espaços por hífens e remover caracteres inválidos
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text

def generate_frontmatter(title, section_number=None, tags=None):
    """Gera o frontmatter YAML para o arquivo markdown."""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    date_str = now.strftime("%Y-%m-%d")
    
    # Determinar tags com base no título e conteúdo
    if tags is None:
        tags = ["source/trato-yoga", "type/concept", "theme/yoga"]
    
    # Formatar as tags corretamente para YAML
    tags_str = ", ".join([f'"{tag}"' for tag in tags])
    
    # Adicionar a numeração ao título se disponível
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

def extract_hierarchical_sections(content):
    """Extrai seções do conteúdo preservando a estrutura hierárquica."""
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
        
        # Extrair o conteúdo da seção (sem o cabeçalho)
        section_content = content[start:end]
        
        sections.append({
            'title': clean_title,
            'number': section_number,
            'full_title': title,
            'level': level,
            'start': start,
            'end': end,
            'content': section_content
        })
    
    return sections

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

def extract_specific_concepts(input_file, output_dir):
    """Extrai conceitos específicos do arquivo de entrada"""
    try:
        # Criar diretório de saída se não existir
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Ler o conteúdo do arquivo
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrair todas as seções preservando a hierarquia
        sections = extract_hierarchical_sections(content)
        
        # Lista de conceitos específicos para extrair
        # Mapeamento título -> tags adicionais
        concept_mapping = {
            "Mudrá": ["theme/meditacao"],
            "Pújá": ["theme/meditacao"],
            "Mantra": ["theme/mantra"],
            "Pránáyáma": ["theme/pranayama"],
            "Ásana": ["theme/asana"],
            "Chakras": ["theme/energia"],
            "Kundaliní": ["theme/energia"],
            "Samádhi": ["theme/meditacao"],
            "Tipos de Yôga": ["type/reference"],
            "Yôga Clássico": ["type/reference"],
            "Karma": ["theme/filosofia"],
            "Dhyána": ["theme/meditacao"],
            "Yama e Niyama": ["theme/filosofia"],
        }
        
        # Adicionar também números de seção que queremos capturar explicitamente
        section_numbers = ["1", "2", "3", "4", "5", "6", "7", "5.1", "5.1.1", "5.1.2", "5.1.3", "5.1.4", 
                          "7.1", "7.1.1", "7.1.2", "7.1.3", "7.1.4", "7.1.5", "7.1.6", "7.1.7", "7.1.8"]
        
        created_zettels = []
        
        # Processar seções
        for section in sections:
            should_process = False
            extra_tags = []
            
            # Verificar se é uma seção por número
            if section['number'] and section['number'] in section_numbers:
                should_process = True
            
            # Verificar se é uma seção por título
            for concept_title, tags in concept_mapping.items():
                if concept_title.lower() in section['title'].lower():
                    should_process = True
                    extra_tags.extend(tags)
                    break
            
            if should_process:
                # Processar o conteúdo
                processed_content = process_content(section['content'])
                
                # Gerar tags
                tags = ["source/trato-yoga", "type/concept"] + extra_tags
                
                # Gerar frontmatter
                frontmatter = generate_frontmatter(section['title'], section['number'], tags)
                
                # Criar nome de arquivo
                filename = create_zettel_filename(section['title'], section['number'])
                output_path = os.path.join(output_dir, filename)
                
                # Escrever o arquivo
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(frontmatter + processed_content + "\n\n## 🔗 Links e Referências")
                
                created_zettels.append({
                    'title': section['title'],
                    'number': section['number'],
                    'filename': filename
                })
                
                print(f"Criado zettel: {filename}")
        
        return created_zettels
    except Exception as e:
        print(f"ERRO ao processar arquivo {input_file}: {str(e)}")
        import traceback
        traceback.print_exc()
        return []

def main():
    try:
        parser = argparse.ArgumentParser(description="Gera notas Zettelkasten específicas a partir de arquivo Markdown.")
        
        parser.add_argument("input_file", nargs="?", default=DEFAULT_INPUT_FILE,
                          help=f"Caminho para o arquivo de entrada (padrão: {DEFAULT_INPUT_FILE})")
        
        parser.add_argument("--output", "-o", 
                          default=DEFAULT_OUTPUT_DIR,
                          help=f"Diretório de saída para os Zettels (padrão: {DEFAULT_OUTPUT_DIR})")
        
        args = parser.parse_args()
        
        # Verificar se o arquivo de entrada existe
        input_file = args.input_file
        if not os.path.exists(input_file):
            print(f"ERRO: Arquivo de entrada '{input_file}' não encontrado.")
            sys.exit(1)
            
        print(f"Processando arquivo: {input_file}")
        print(f"Diretório de saída: {args.output}")
        
        # Extrair conceitos específicos
        zettels = extract_specific_concepts(input_file, args.output)
        
        print(f"Processo concluído! Criados {len(zettels)} zettels.")
        
    except Exception as e:
        print(f"ERRO: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 