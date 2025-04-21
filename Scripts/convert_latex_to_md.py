from pathlib import Path
import re

# Caminho do arquivo LaTeX convertido em markdown (mas ainda com comandos LaTeX)
input_file = Path("00 - INBOX/02 - LITERATURE/Yoga_R00.md")
output_file = Path("00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned.md")

def convert_latex_to_markdown(text):
    """Converte comandos LaTeX para Markdown"""
    # Remove preâmbulo LaTeX
    text = re.sub(r'\\documentclass.*?\\begin{document}', '', text, flags=re.DOTALL)
    text = re.sub(r'\\end{document}', '', text)
    
    # Conversão de formatação básica
    text = re.sub(r'\\textbf\{([^}]+)\}', r'**\1**', text)  # Negrito
    text = re.sub(r'\\textit\{([^}]+)\}', r'*\1*', text)    # Itálico
    text = re.sub(r'\\underline\{([^}]+)\}', r'<u>\1</u>', text)  # Sublinhado
    
    # Conversão de cabeçalhos
    text = re.sub(r'\\section\*?\{([^}]+)\}', r'# \1', text)
    text = re.sub(r'\\subsection\*?\{([^}]+)\}', r'## \1', text)
    text = re.sub(r'\\subsubsection\*?\{([^}]+)\}', r'### \1', text)
    
    # Conversão de listas
    text = re.sub(r'\\begin\{itemize\}', '', text)
    text = re.sub(r'\\end\{itemize\}', '', text)
    text = re.sub(r'\\begin\{enumerate\}', '', text)
    text = re.sub(r'\\end\{enumerate\}', '', text)
    text = re.sub(r'\\item\s*\[([^]]+)\]', r'- **\1**:', text)  # Item com label
    text = re.sub(r'\\item', r'- ', text)  # Item normal
    
    # Tratamento de notas de rodapé
    text = re.sub(r'\\footnote\{([^}]+)\}', r' [^1]: \1', text)
    
    # Remover comandos de formatação e layout
    text = re.sub(r'\\begin\{center\}', '', text)
    text = re.sub(r'\\end\{center\}', '', text)
    text = re.sub(r'\\newline', r'\n', text)
    text = re.sub(r'\\\\', r'\n', text)  # Quebra de linha LaTeX
    text = re.sub(r'~', ' ', text)  # Espaço não-quebrável
    
    # Caracteres especiais
    text = re.sub(r'\\%', '%', text)
    text = re.sub(r'\\"o', 'ö', text)
    text = re.sub(r'\\"a', 'ä', text)
    text = re.sub(r'\\"u', 'ü', text)
    text = re.sub(r'\\\'a', 'á', text)
    text = re.sub(r'\\\'e', 'é', text)
    text = re.sub(r'\\\'i', 'í', text)
    text = re.sub(r'\\\'o', 'ó', text)
    text = re.sub(r'\\\'u', 'ú', text)
    text = re.sub(r'\\\^a', 'â', text)
    text = re.sub(r'\\\^e', 'ê', text)
    text = re.sub(r'\\\^i', 'î', text)
    text = re.sub(r'\\\^o', 'ô', text)
    text = re.sub(r'\\\^u', 'û', text)
    
    # Remover outros comandos LaTeX
    text = re.sub(r'\\tableofcontents', '', text)
    text = re.sub(r'\\maketitle', '', text)
    text = re.sub(r'\\newpage', '\n\n---\n\n', text)
    text = re.sub(r'\\noindent', '', text)
    
    # Remover comandos LaTeX genéricos não tratados acima
    text = re.sub(r'\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{[^}]*\})*', '', text)
    
    # Limpar linhas vazias excessivas
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text.strip()

def main():
    print(f"Lendo arquivo: {input_file}")
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Converter LaTeX para Markdown
        converted_content = convert_latex_to_markdown(content)
        
        # Salvar o resultado
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(converted_content)
        
        print(f"Conversão concluída! Arquivo salvo em: {output_file}")
        print(f"O documento contém {len(converted_content.split('# '))-1} seções principais")
    
    except Exception as e:
        print(f"Erro durante a conversão: {e}")

if __name__ == "__main__":
    main() 