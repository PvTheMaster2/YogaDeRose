#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path
import unicodedata

# Configurações padrão
INPUT_FILE = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned_utf8.md"
OUTPUT_DIR = "10 - PERMANENT/Zettels/Yoga"

def normalize_filename(text):
    """Normaliza o texto para ser usado como nome de arquivo"""
    # Remover caracteres especiais e acentos
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    # Substituir espaços por hífens e remover caracteres inválidos
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s]+', '-', text)
    return text

def extract_headers(content):
    """Extrai todos os cabeçalhos do documento em ordem, preservando a hierarquia"""
    lines = content.split('\n')
    headers = []
    current_line = 0
    
    while current_line < len(lines):
        line = lines[current_line].strip()
        
        # Verificar se é um cabeçalho
        header_match = re.match(r'^(#+)\s+(.*?)$', line)
        if header_match:
            level = len(header_match.group(1))
            title = header_match.group(2).strip()
            
            # Extrair numeração original se existir
            num_match = re.match(r'^(\d+(?:\.\d+)*)\s+(.*?)$', title)
            original_number = None
            clean_title = title
            
            if num_match:
                original_number = num_match.group(1)
                clean_title = num_match.group(2).strip()
            
            start_line = current_line
            
            # Encontrar o conteúdo da seção até o próximo cabeçalho do mesmo nível ou superior
            end_line = current_line + 1
            while end_line < len(lines):
                next_line = lines[end_line].strip()
                next_header_match = re.match(r'^(#+)\s+', next_line)
                if next_header_match and len(next_header_match.group(1)) <= level:
                    break
                end_line += 1
            
            # Extrair o conteúdo da seção (excluindo o cabeçalho)
            section_content = '\n'.join(lines[current_line+1:end_line]).strip()
            
            # Extrair e armazenar subseções
            subheaders = []
            if level < 3:  # Se for # ou ##, procure por subseções
                subheader_pattern = r'^(#{' + str(level+1) + '})\s+(.*?)$'
                sub_lines = section_content.split('\n')
                current_sub_idx = 0
                
                while current_sub_idx < len(sub_lines):
                    sub_line = sub_lines[current_sub_idx].strip()
                    sub_match = re.match(subheader_pattern, sub_line)
                    
                    if sub_match:
                        sub_title = sub_match.group(2).strip()
                        sub_start = current_sub_idx
                        
                        # Encontrar o fim da subseção
                        sub_end = current_sub_idx + 1
                        while sub_end < len(sub_lines):
                            next_sub = sub_lines[sub_end].strip()
                            next_sub_match = re.match(subheader_pattern, next_sub)
                            if next_sub_match:
                                break
                            sub_end += 1
                        
                        sub_content = '\n'.join(sub_lines[sub_start+1:sub_end]).strip()
                        
                        sub_header = {
                            'level': level + 1,
                            'title': sub_title,
                            'content': sub_content,
                            'parent_title': clean_title,
                            'original_number': None,
                            'subheaders': []
                        }
                        
                        # Se for uma subseção (##), procurar por subsubseções (###)
                        if level + 1 < 3:  # Se for nível ## (level=2)
                            subsubheader_pattern = r'^(#{' + str(level+2) + '})\s+(.*?)$'
                            subsub_lines = sub_content.split('\n')
                            current_subsub_idx = 0
                            
                            while current_subsub_idx < len(subsub_lines):
                                subsub_line = subsub_lines[current_subsub_idx].strip()
                                subsub_match = re.match(subsubheader_pattern, subsub_line)
                                
                                if subsub_match:
                                    subsub_title = subsub_match.group(2).strip()
                                    subsub_start = current_subsub_idx
                                    
                                    # Encontrar o fim da subsubseção
                                    subsub_end = current_subsub_idx + 1
                                    while subsub_end < len(subsub_lines):
                                        next_subsub = subsub_lines[subsub_end].strip()
                                        next_subsub_match = re.match(subsubheader_pattern, next_subsub)
                                        if next_subsub_match:
                                            break
                                        subsub_end += 1
                                    
                                    subsub_content = '\n'.join(subsub_lines[subsub_start+1:subsub_end]).strip()
                                    
                                    subsub_header = {
                                        'level': level + 2,
                                        'title': subsub_title,
                                        'content': subsub_content,
                                        'parent_title': sub_title,
                                        'grandparent_title': clean_title,
                                        'original_number': None
                                    }
                                    
                                    sub_header['subheaders'].append(subsub_header)
                                    current_subsub_idx = subsub_end
                                else:
                                    current_subsub_idx += 1
                        
                        subheaders.append(sub_header)
                        current_sub_idx = sub_end
                    else:
                        current_sub_idx += 1
            
            headers.append({
                'level': level,
                'title': clean_title,
                'content': section_content,
                'start_line': start_line,
                'end_line': end_line,
                'original_number': original_number,
                'subheaders': subheaders
            })
            
            current_line = end_line
        else:
            current_line += 1
    
    return headers

def assign_numbers_to_headers(headers):
    """Atribui números sequenciais aos cabeçalhos de acordo com a hierarquia, respeitando numeração original quando presente"""
    # Lista para armazenar cabeçalhos numerados
    numbered_headers = []
    
    # Manter registro dos títulos originais para referência
    title_to_number = {}
    
    # Primeiro passe: atribuir números sequenciais a cabeçalhos principais
    section_counter = 1
    
    # Verificar se devemos usar numeração original ou criar nova
    use_original_numbering = any(header.get('original_number') for header in headers)
    
    for header in headers:
        if header['level'] == 1:  # Se for cabeçalho de nível 1 (#)
            if use_original_numbering and header.get('original_number'):
                section_number = header['original_number']
            else:
                section_number = str(section_counter)
                section_counter += 1
            
            header['section_number'] = section_number
            title_to_number[header['title']] = section_number
            numbered_headers.append(header)
            
            # Processar subseções dentro deste cabeçalho
            subsection_counter = 1
            for subheader in header.get('subheaders', []):
                if use_original_numbering and subheader.get('original_number'):
                    subsection_number = subheader['original_number']
                else:
                    subsection_number = f"{section_number}.{subsection_counter}"
                    subsection_counter += 1
                
                subheader['section_number'] = subsection_number
                title_to_number[subheader['title']] = subsection_number
                numbered_headers.append(subheader)
                
                # Processar subsubseções dentro desta subseção
                subsubsection_counter = 1
                for subsubheader in subheader.get('subheaders', []):
                    if use_original_numbering and subsubheader.get('original_number'):
                        subsubsection_number = subsubheader['original_number']
                    else:
                        subsubsection_number = f"{subsection_number}.{subsubsection_counter}"
                        subsubsection_counter += 1
                    
                    subsubheader['section_number'] = subsubsection_number
                    title_to_number[subsubheader['title']] = subsubsection_number
                    numbered_headers.append(subsubheader)
    
    # Certificar-se de que todos os cabeçalhos estejam incluídos
    for header in headers:
        if header['level'] != 1 and header not in numbered_headers:
            # Este é um cabeçalho de nível mais baixo que não foi processado como subseção
            if use_original_numbering and header.get('original_number'):
                section_number = header['original_number']
            else:
                section_number = str(section_counter)
                section_counter += 1
            
            header['section_number'] = section_number
            title_to_number[header['title']] = section_number
            numbered_headers.append(header)
    
    # Ordenar cabeçalhos para garantir ordem crescente por número
    def get_numeric_parts(section_number):
        # Converter string de numeração para lista numérica para ordenação
        return [int(part) if part.isdigit() else part for part in section_number.split('.')]
    
    numbered_headers.sort(key=lambda h: get_numeric_parts(h['section_number']))
    
    # Verificar se há lacunas na numeração e corrigir se necessário
    section_numbers = [header['section_number'] for header in numbered_headers]
    main_sections = [num for num in section_numbers if '.' not in num]
    
    # Garantir que os números principais estão em sequência (1, 2, 3...)
    if all(num.isdigit() for num in main_sections):
        expected_nums = list(range(1, len(main_sections) + 1))
        actual_nums = sorted([int(num) for num in main_sections])
        
        if expected_nums != actual_nums:
            # Há lacunas, reorganizar para números sequenciais
            num_map = {str(old): str(new) for old, new in zip(actual_nums, expected_nums)}
            
            for header in numbered_headers:
                parts = header['section_number'].split('.')
                if parts[0] in num_map:
                    parts[0] = num_map[parts[0]]
                    header['section_number'] = '.'.join(parts)
    
    return numbered_headers

def generate_frontmatter(title, section_number, parent_title=None, grandparent_title=None):
    """Gera o frontmatter YAML para o arquivo markdown"""
    now = datetime.now()
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    date_str = now.strftime("%Y-%m-%d")
    
    # Determinar tags básicas
    tags = ["source/trato-yoga"]
    
    # Adicionar tag de tipo com base em heurísticas simples
    if any(keyword in title.lower() for keyword in ["definição", "o que é", "conceito"]):
        tags.append("type/concept")
    elif any(keyword in title.lower() for keyword in ["técnica", "prática", "exercício", "como"]):
        tags.append("type/practice")
    else:
        tags.append("type/concept")
    
    # Adicionar tag temática
    if "yoga" in title.lower() or "yôga" in title.lower():
        tags.append("theme/yoga")
    
    # Formatar as tags corretamente para YAML
    tags_str = ", ".join([f'"{tag}"' for tag in tags])
    
    # Título completo com numeração
    display_title = f"{section_number} – {title}"
    
    # Adicionar informação sobre o pai se for uma subseção
    parent_info = ""
    if parent_title:
        parent_info += f'\nparent: "{parent_title}"'
    if grandparent_title:
        parent_info += f'\ngrandparent: "{grandparent_title}"'
    
    return f"""---
id: {timestamp}
title: "{display_title}"
tags: [{tags_str}]
zettel-type: literature
source: "Trato de Yôga do Mestre De Rose"
created: {date_str}{parent_info}
---

# {display_title}

"""

def create_zettel_filename(title, section_number):
    """Cria um nome de arquivo adequado para o zettel"""
    # Substituir pontos por hífen para manter a estrutura
    clean_number = section_number.replace('.', '-')
    normalized_title = normalize_filename(title)
    return f"{clean_number}--{normalized_title}.md"

def process_content(content):
    """Processa o conteúdo para formatação markdown adequada"""
    # Limpar formatação LaTeX
    content = re.sub(r'\\textit\{(.*?)\}', r'*\1*', content)  # Itálico
    content = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', content)  # Negrito
    
    # Outras limpezas de LaTeX
    content = re.sub(r'\\begin\{.*?\}|\\end\{.*?\}', '', content)
    content = re.sub(r'\\item', '-', content)
    
    # Extrair e processar subseções
    subsections = re.finditer(r'###\s+(.*?)\n(.*?)(?=###|\Z)', content, re.DOTALL)
    for match in subsections:
        sub_title = match.group(1).strip()
        sub_content = match.group(2).strip()
        # Prepara o conteúdo para manter apenas um resumo para o MOC
        summary = sub_content.split('\n\n')[0] if '\n\n' in sub_content else sub_content
        if len(summary) > 150:
            summary = summary[:147] + "..."
        # Adiciona uma versão resumida para ser usada no MOC
        content = content.replace(match.group(0), f"### {sub_title}\n{sub_content}\n")
    
    return content

def create_zettels_from_headers(headers, output_dir):
    """Cria arquivos de zettel a partir dos cabeçalhos extraídos"""
    created_zettels = []
    
    # Garantir que o diretório de saída existe
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for header in headers:
        # Processar todos os níveis de cabeçalho (1, 2 e 3)
        if 'section_number' in header:
            # Processar o conteúdo
            processed_content = process_content(header['content'])
            
            # Gerar frontmatter
            parent_title = header.get('parent_title')
            grandparent_title = header.get('grandparent_title')
            frontmatter = generate_frontmatter(header['title'], header['section_number'], parent_title, grandparent_title)
            
            # Criar nome de arquivo
            filename = create_zettel_filename(header['title'], header['section_number'])
            output_path = os.path.join(output_dir, filename)
            
            # Escrever o arquivo
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter + processed_content + "\n\n## 🔗 Links e Referências")
            
            created_zettels.append({
                'title': header['title'],
                'section_number': header['section_number'],
                'filename': filename,
                'parent_title': parent_title,
                'grandparent_title': grandparent_title
            })
            
            print(f"Criado zettel: {filename}")
            
            # Processar subseções
            if 'subheaders' in header:
                for subheader in header['subheaders']:
                    if 'section_number' in subheader:
                        # Processar o conteúdo da subseção
                        sub_processed_content = process_content(subheader['content'])
                        
                        # Gerar frontmatter
                        sub_parent_title = subheader.get('parent_title')
                        sub_frontmatter = generate_frontmatter(subheader['title'], subheader['section_number'], sub_parent_title)
                        
                        # Criar nome de arquivo
                        sub_filename = create_zettel_filename(subheader['title'], subheader['section_number'])
                        sub_output_path = os.path.join(output_dir, sub_filename)
                        
                        # Escrever o arquivo
                        with open(sub_output_path, 'w', encoding='utf-8') as f:
                            f.write(sub_frontmatter + sub_processed_content + "\n\n## 🔗 Links e Referências")
                        
                        created_zettels.append({
                            'title': subheader['title'],
                            'section_number': subheader['section_number'],
                            'filename': sub_filename,
                            'parent_title': sub_parent_title
                        })
                        
                        print(f"Criado zettel (subseção): {sub_filename}")
                        
                        # Processar subsubseções
                        if 'subheaders' in subheader:
                            for subsubheader in subheader['subheaders']:
                                if 'section_number' in subsubheader:
                                    # Processar o conteúdo da subsubseção
                                    subsub_processed_content = process_content(subsubheader['content'])
                                    
                                    # Gerar frontmatter
                                    subsub_parent_title = subsubheader.get('parent_title')
                                    subsub_grandparent_title = subsubheader.get('grandparent_title')
                                    subsub_frontmatter = generate_frontmatter(
                                        subsubheader['title'], 
                                        subsubheader['section_number'], 
                                        subsub_parent_title,
                                        subsub_grandparent_title
                                    )
                                    
                                    # Criar nome de arquivo
                                    subsub_filename = create_zettel_filename(subsubheader['title'], subsubheader['section_number'])
                                    subsub_output_path = os.path.join(output_dir, subsub_filename)
                                    
                                    # Escrever o arquivo
                                    with open(subsub_output_path, 'w', encoding='utf-8') as f:
                                        f.write(subsub_frontmatter + subsub_processed_content + "\n\n## 🔗 Links e Referências")
                                    
                                    created_zettels.append({
                                        'title': subsubheader['title'],
                                        'section_number': subsubheader['section_number'],
                                        'filename': subsub_filename,
                                        'parent_title': subsub_parent_title,
                                        'grandparent_title': subsub_grandparent_title
                                    })
                                    
                                    print(f"Criado zettel (subsubseção): {subsub_filename}")
    
    return created_zettels

def main():
    try:
        # Verificar se o arquivo de entrada existe
        if not os.path.exists(INPUT_FILE):
            print(f"ERRO: Arquivo de entrada '{INPUT_FILE}' não encontrado.")
            sys.exit(1)
        
        print(f"Processando arquivo: {INPUT_FILE}")
        print(f"Diretório de saída: {OUTPUT_DIR}")
        
        # Ler o conteúdo do arquivo
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extrair cabeçalhos
        headers = extract_headers(content)
        
        if not headers:
            print("Nenhum cabeçalho encontrado no arquivo.")
            sys.exit(1)
        
        # Atribuir números sequenciais aos cabeçalhos
        headers = assign_numbers_to_headers(headers)
        
        # Criar zettels
        zettels = create_zettels_from_headers(headers, OUTPUT_DIR)
        
        print(f"Processo concluído! Criados {len(zettels)} zettels com numeração sequencial.")
        
    except Exception as e:
        print(f"ERRO: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 