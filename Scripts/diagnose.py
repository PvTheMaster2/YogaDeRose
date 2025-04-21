import os
import sys
from pathlib import Path

def main():
    """Script de diagnóstico para verificar problemas com a leitura de arquivo."""
    print("Script de diagnóstico iniciado")
    
    # Caminho do arquivo
    file_path = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned.md"
    abs_path = os.path.abspath(file_path)
    
    # Verificar se o arquivo existe
    print(f"Verificando arquivo: {file_path}")
    print(f"Caminho absoluto: {abs_path}")
    
    if not Path(file_path).exists():
        print(f"ERRO: Arquivo não encontrado: {file_path}")
        return False
    
    # Verificar tamanho do arquivo
    file_size = os.path.getsize(file_path)
    print(f"Tamanho do arquivo: {file_size} bytes")
    
    if file_size == 0:
        print("ALERTA: Arquivo está vazio!")
        return False
    
    # Tentar ler o arquivo
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print("Arquivo aberto com sucesso usando codificação UTF-8")
            
            # Ler primeiras linhas
            print("\nPrimeiras 20 linhas:")
            lines = []
            for i, line in enumerate(f):
                if i < 20:
                    lines.append(line)
                    print(f"{i+1}: {line.rstrip()}")
                else:
                    break
            
            # Voltar ao início do arquivo
            f.seek(0)
            
            # Contar seções
            section_count = 0
            subsection_count = 0
            
            for line in f:
                if line.startswith('# '):
                    section_count += 1
                elif line.startswith('## '):
                    subsection_count += 1
            
            print(f"\nEncontradas {section_count} seções e {subsection_count} subseções")
            
            # Verificar padrões de numeração
            f.seek(0)
            print("\nProcurando padrões de numeração em seções:")
            
            number_patterns = []
            import re
            number_pattern = re.compile(r'^#+\s+(\d+(\.\d+)*)\s*(.*?)$')
            
            for i, line in enumerate(f):
                if line.startswith('#'):
                    match = number_pattern.match(line)
                    if match:
                        number = match.group(1)
                        title = match.group(3)
                        number_patterns.append((number, title))
                        if len(number_patterns) < 10:  # Mostrar apenas as 10 primeiras
                            print(f"  - Encontrado: {number} - {title}")
            
            print(f"\nTotal de seções numeradas: {len(number_patterns)}")
            
            # Verificar seções em formato LaTeX
            f.seek(0)
            latex_section = 0
            latex_pattern = re.compile(r'\\section\{|\\subsection\{|\\subsubsection\{')
            
            for line in f:
                if latex_pattern.search(line):
                    latex_section += 1
            
            if latex_section > 0:
                print(f"\nEncontradas {latex_section} seções no formato LaTeX")
                print("Formato do arquivo parece ser LaTeX")
            else:
                print("\nNenhuma seção no formato LaTeX encontrada")
                print("Formato do arquivo parece ser Markdown")
            
    except UnicodeDecodeError:
        print("ERRO: Não foi possível ler o arquivo com codificação UTF-8")
        
        # Tentar outras codificações
        for encoding in ['latin-1', 'cp1252', 'iso-8859-1']:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    f.read(100)  # Tentar ler os primeiros 100 caracteres
                    print(f"Arquivo pode ser lido com codificação {encoding}")
            except UnicodeDecodeError:
                print(f"Não foi possível ler o arquivo com codificação {encoding}")
    
    except Exception as e:
        print(f"ERRO ao ler o arquivo: {str(e)}")
        return False
    
    print("\nDiagnóstico concluído")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 