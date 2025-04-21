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
            
            # Capturar a numeração se existir
            number_match = re.match(r'^(\d+(?:\.\d+)*)\s+(.*?)$', title)
            if number_match:
                section_number = number_match.group(1)
                clean_title = number_match.group(2).strip()
            else:
                section_number = None
                clean_title = title
            
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
            
            headers.append({
                'level': level,
                'title': clean_title,
                'number': section_number,
                'full_title': title,
                'content': section_content,
                'start_line': start_line,
                'end_line': end_line
            })
            
            current_line = end_line
        else:
            current_line += 1
    
    return headers

def generate_frontmatter(title, section_number=None):
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

def create_zettel_filename(title, section_number=None):
    """Cria um nome de arquivo adequado para o zettel"""
    # Se houver numeração de seção, incluí-la no nome do arquivo
    if section_number:
        # Substituir pontos por hífen para manter a estrutura
        clean_number = section_number.replace('.', '-')
        normalized_title = normalize_filename(title)
        return f"{clean_number}-{normalized_title}.md"
    else:
        return f"{normalize_filename(title)}.md"

def process_content(content):
    """Processa o conteúdo para formatação markdown adequada"""
    # Limpar formatação LaTeX
    content = re.sub(r'\\textit\{(.*?)\}', r'*\1*', content)  # Itálico
    content = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', content)  # Negrito
    
    # Outras limpezas de LaTeX
    content = re.sub(r'\\begin\{.*?\}|\\end\{.*?\}', '', content)
    content = re.sub(r'\\item', '-', content)
    
    return content

def create_zettels_from_headers(headers, output_dir):
    """Cria arquivos de zettel a partir dos cabeçalhos extraídos"""
    created_zettels = []
    
    # Garantir que o diretório de saída existe
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for header in headers:
        # Ignorar seções sem conteúdo ou com títulos vazios
        if not header['content'] or not header['title']:
            continue
        
        # Processar o conteúdo
        processed_content = process_content(header['content'])
        
        # Gerar frontmatter
        frontmatter = generate_frontmatter(header['title'], header['number'])
        
        # Criar nome de arquivo
        filename = create_zettel_filename(header['title'], header['number'])
        output_path = os.path.join(output_dir, filename)
        
        # Escrever o arquivo
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(frontmatter + processed_content + "\n\n## 🔗 Links e Referências")
        
        created_zettels.append({
            'title': header['title'],
            'number': header['number'],
            'filename': filename
        })
        
        print(f"Criado zettel: {filename}")
    
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
        
        # Criar zettels
        zettels = create_zettels_from_headers(headers, OUTPUT_DIR)
        
        print(f"Processo concluído! Criados {len(zettels)} zettels na ordem original do documento.")
        
    except Exception as e:
        print(f"ERRO: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main() 