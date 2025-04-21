import os
import argparse
import subprocess
from pathlib import Path
import sys

# Cores para saída
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(msg):
    print(f"\n{Colors.HEADER}{Colors.BOLD}=== {msg} ==={Colors.ENDC}\n")

def print_success(msg):
    print(f"{Colors.GREEN}✓ {msg}{Colors.ENDC}")

def print_warning(msg):
    print(f"{Colors.WARNING}⚠ {msg}{Colors.ENDC}")

def print_error(msg):
    print(f"{Colors.FAIL}✗ {msg}{Colors.ENDC}")

def run_command(command):
    """Executa um comando e retorna o resultado."""
    print(f"Executando: {command}")
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(f"ERRO: {result.stderr}")
    return result.returncode == 0

def ensure_directories_exist():
    """Garante que todos os diretórios necessários existem"""
    directories = [
        "00 - INBOX/02 - LITERATURE",
        "10 - PERMANENT/Zettels/Yoga",
        "30 - MPS OF CONTENTS",
        "99 - RESOURCES/Templates",
        "Scripts"
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    print_success("Diretórios verificados e criados se necessário")

def main():
    parser = argparse.ArgumentParser(description="Pipeline para processamento do Trato de Yôga.")
    parser.add_argument("--skip-conversion", action="store_true", help="Pular a conversão de LaTeX para Markdown.")
    parser.add_argument("--skip-zettels", action="store_true", help="Pular a geração de Zettels.")
    parser.add_argument("--regenerate", action="store_true", help="Regenerar Zettels com estrutura hierárquica correta.")
    parser.add_argument("--update-links", action="store_true", help="Atualizar links entre notas e no MOC.")
    args = parser.parse_args()
    
    # Configurações
    input_file = "00 - INBOX/02 - LITERATURE/Yoga_R00.md"
    cleaned_file = "00 - INBOX/02 - LITERATURE/Yoga_R00_cleaned.md"
    zettels_dir = "10 - PERMANENT/Zettels/Yoga"
    
    # Verificar existência do diretório base
    for dir_path in ["00 - INBOX/02 - LITERATURE", "10 - PERMANENT/Zettels", "30 - MPS OF CONTENTS"]:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    
    # 1. Converter LaTeX para Markdown
    if not args.skip_conversion and not args.regenerate:
        if not Path(input_file).exists():
            print(f"ERRO: Arquivo de entrada '{input_file}' não encontrado.")
            return False
        
        print(f"Convertendo LaTeX para Markdown limpo...")
        success = run_command(f"python Scripts/convert_latex_to_md.py --input {input_file} --output {cleaned_file}")
        if not success:
            print("Conversão falhou.")
            return False
    
    # 2. Gerar Zettels
    if not args.skip_zettels or args.regenerate:
        if not Path(cleaned_file).exists():
            print(f"ERRO: Arquivo Markdown limpo '{cleaned_file}' não encontrado.")
            return False
        
        # Se estamos regenerando, primeiro limpamos o diretório de zettels
        if args.regenerate:
            print("Regenerando Zettels com estrutura hierárquica correta...")
            
            # Backup dos arquivos existentes (opcional)
            if Path(zettels_dir).exists():
                backup_dir = f"{zettels_dir}_backup"
                print(f"Fazendo backup dos zettels existentes para {backup_dir}...")
                import shutil
                if Path(backup_dir).exists():
                    shutil.rmtree(backup_dir)
                shutil.copytree(zettels_dir, backup_dir)
                
                # Limpar diretório existente
                for file in Path(zettels_dir).glob("*.md"):
                    file.unlink()
        
        print(f"Gerando Zettels a partir do Markdown limpo...")
        success = run_command(f"python Scripts/generate_zettels.py --input {cleaned_file} --output {zettels_dir}")
        if not success:
            print("Geração de Zettels falhou.")
            return False
    
    # 3. Atualizar links entre notas
    if args.update_links:
        print("Atualizando links entre notas e no MOC...")
        success = run_command(f"python Scripts/update_connections.py")
        if not success:
            print("Atualização de links falhou.")
            return False
    
    print("Pipeline concluído com sucesso!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 