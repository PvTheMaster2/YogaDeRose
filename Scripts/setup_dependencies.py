import subprocess
import sys
import os

def check_and_install_package(package_name):
    """Verifica se um pacote está instalado e instala se necessário"""
    try:
        __import__(package_name)
        print(f"✓ {package_name} já está instalado")
        return True
    except ImportError:
        print(f"! {package_name} não encontrado. Instalando...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"✓ {package_name} instalado com sucesso")
            return True
        except subprocess.CalledProcessError:
            print(f"✗ Falha ao instalar {package_name}")
            return False

def main():
    print("=== Configurando dependências para scripts de manutenção Yoga Zettelkasten ===\n")
    
    # Lista de pacotes necessários
    packages = [
        "nltk",
        "pyyaml",
    ]
    
    # Verificar e instalar pacotes
    all_installed = True
    for package in packages:
        if not check_and_install_package(package):
            all_installed = False
    
    # Verificar NLTK data
    print("\n=== Configurando recursos do NLTK ===\n")
    
    try:
        import nltk
        nltk_resources = [
            "punkt",
            "stopwords",
        ]
        
        for resource in nltk_resources:
            try:
                nltk.data.find(f"tokenizers/{resource}" if resource == "punkt" else f"corpora/{resource}")
                print(f"✓ Recurso NLTK '{resource}' já está disponível")
            except LookupError:
                print(f"! Recurso NLTK '{resource}' não encontrado. Baixando...")
                nltk.download(resource)
                print(f"✓ Recurso NLTK '{resource}' baixado com sucesso")
    except Exception as e:
        print(f"✗ Erro ao configurar recursos NLTK: {e}")
        all_installed = False
    
    # Verificar se o script de atualização existe
    update_script = "Scripts/update_connections.py"
    if os.path.exists(update_script):
        print(f"\n✓ Script de atualização encontrado em '{update_script}'")
    else:
        print(f"\n✗ Script de atualização não encontrado em '{update_script}'")
        all_installed = False
    
    if all_installed:
        print("\n✓ Todas as dependências foram instaladas com sucesso!")
        print("\nPara atualizar as conexões das notas, execute:")
        print(f"    python {update_script}")
    else:
        print("\n! Algumas dependências não puderam ser instaladas.")
        print("  Por favor, resolva os problemas acima e tente novamente.")
    
    return all_installed

if __name__ == "__main__":
    main() 