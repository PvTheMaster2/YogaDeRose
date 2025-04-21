#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from pathlib import Path
import sys

def convert_latex_to_markdown(text):
    """
    Converte um documento LaTeX para Markdown preservando a estrutura e o conteúdo.
    """
    # Preservar o YAML frontmatter se existir
    yaml_match = re.match(r'^---\n(.*?\n)---\n', text, re.DOTALL)
    frontmatter = yaml_match.group(0) if yaml_match else ""
    
    if yaml_match:
        # Remover o frontmatter do texto para processamento
        text = text[len(frontmatter):]
    
    # Remover preâmbulo LaTeX
    text = re.sub(r'\\documentclass.*?\\begin{document}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\end{document}', '', text)
    text = re.sub(r'\\maketitle', '', text)
    text = re.sub(r'\\tableofcontents', '', text)
    text = re.sub(r'\\newpage', '\n\n', text)
    
    # Converter headers (preservando numeração)
    text = re.sub(r'\\section\{(.*?)\}', r'# \1', text)
    text = re.sub(r'\\subsection\{(.*?)\}', r'## \1', text)
    text = re.sub(r'\\subsubsection\{(.*?)\}', r'### \1', text)
    
    # Converter formatação de texto
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)  # Negrito
    text = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', text)    # Itálico
    text = re.sub(r'\\underline\{([^}]+)\}', r'<u>\1</u>', text)  # Sublinhado
    text = re.sub(r'\\emph\{([^}]+)\}', r'*\1*', text)      # Ênfase
    
    # Converter listas
    text = re.sub(r'\\begin\{itemize\}', '', text)
    text = re.sub(r'\\end\{itemize\}', '', text)
    text = re.sub(r'\\begin\{enumerate\}', '', text)
    text = re.sub(r'\\end\{enumerate\}', '', text)
    
    # Converter items de lista (com especial atenção aos itens com labels)
    text = re.sub(r'\\item\s*\[(.*?)\]', r'- **\1**:', text)
    text = re.sub(r'\\item', r'- ', text)
    
    # Tratar notas de rodapé
    footnote_count = 0
    footnotes = []
    
    def footnote_replace(match):
        nonlocal footnote_count
        footnote_count += 1
        footnote_text = match.group(1)
        footnotes.append(f"[^{footnote_count}]: {footnote_text}")
        return f" [^{footnote_count}]"
    
    text = re.sub(r'\\footnote\{(.*?)\}', footnote_replace, text)
    
    # Remover comandos de layout
    text = re.sub(r'\\begin\{center\}', '', text)
    text = re.sub(r'\\end\{center\}', '', text)
    text = re.sub(r'\\centering', '', text)
    text = re.sub(r'\\noindent', '', text)
    
    # Converter quebras de linha
    text = re.sub(r'\\\\', '\n', text)
    text = re.sub(r'\\newline', '\n', text)
    
    # Converter caracteres especiais e acentos
    char_map = {
        r'\\\'a': 'á', r'\\\'e': 'é', r'\\\'i': 'í', r'\\\'o': 'ó', r'\\\'u': 'ú',
        r'\\\^a': 'â', r'\\\^e': 'ê', r'\\\^i': 'î', r'\\\^o': 'ô', r'\\\^u': 'û',
        r'\\"a': 'ä', r'\\"e': 'ë', r'\\"i': 'ï', r'\\"o': 'ö', r'\\"u': 'ü',
        r'\\`a': 'à', r'\\`e': 'è', r'\\`i': 'ì', r'\\`o': 'ò', r'\\`u': 'ù',
        r'\\c{c}': 'ç', r'\\c{C}': 'Ç',
        r'\\~a': 'ã', r'\\~o': 'õ', r'\\~n': 'ñ',
        r'\\\&': '&', r'\\%': '%', r'\\#': '#', r'\\$': '$',
        r'\\textbackslash': '\\', r'\\{': '{', r'\\}': '}',
        r'\\textasciitilde': '~', r'\\textasciicircum': '^',
        r'\\ldots': '...', r'\\dots': '...', r'\\cdots': '...'
    }
    
    for latex_char, md_char in char_map.items():
        text = text.replace(latex_char, md_char)
    
    # Remover comandos que podem ter ficado
    text = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^}]*\})*', '', text)
    
    # Limpar excesso de linhas em branco
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Adicionar notas de rodapé ao final
    if footnotes:
        text += "\n\n" + "\n".join(footnotes)
    
    # Recolocar o frontmatter se existia
    result = frontmatter + text.strip()
    
    return result

def main():
    # Definir arquivos de entrada e saída
    input_file = "00 - INBOX/02 - LITERATURE/Yoga_R00.md"
    output_file = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned_utf8.md"
    
    print(f"Convertendo LaTeX para Markdown: {input_file}")
    
    try:
        # Ler o arquivo de entrada
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Converter
        converted = convert_latex_to_markdown(content)
        
        # Salvar o resultado
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(converted)
        
        print(f"Conversão concluída! Arquivo salvo em: {output_file}")
        print(f"Tamanho do arquivo original: {len(content)} bytes")
        print(f"Tamanho do arquivo convertido: {len(converted)} bytes")
        
        # Contar cabeçalhos para verificar
        h1_count = len(re.findall(r'^# ', converted, re.MULTILINE))
        h2_count = len(re.findall(r'^## ', converted, re.MULTILINE))
        h3_count = len(re.findall(r'^### ', converted, re.MULTILINE))
        
        print(f"Conversão gerou {h1_count} cabeçalhos de nível 1")
        print(f"Conversão gerou {h2_count} cabeçalhos de nível 2") 
        print(f"Conversão gerou {h3_count} cabeçalhos de nível 3")
        
    except Exception as e:
        print(f"Erro durante a conversão: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 