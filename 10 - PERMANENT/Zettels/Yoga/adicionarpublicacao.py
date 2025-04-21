import os
import re

def adicionar_frontmatter():
    # Obtém o diretório atual onde o script está sendo executado
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Conteúdo a ser adicionado quando não há frontmatter
    frontmatter_padrao = "---\ndg-publish: true\n---\n\n"
    
    # Contador de arquivos modificados
    arquivos_modificados = 0
    arquivos_ignorados = 0
    
    # Percorre todos os arquivos no diretório
    for arquivo in os.listdir(diretorio_atual):
        # Verifica se é um arquivo Markdown
        if arquivo.endswith('.md'):
            caminho_completo = os.path.join(diretorio_atual, arquivo)
            
            # Lê o conteúdo do arquivo
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Verifica se tem frontmatter
            if conteudo.startswith('---\n'):
                # Localiza o fim do frontmatter existente
                fim_frontmatter = conteudo.find('\n---', 4)
                if fim_frontmatter > 0:  # Encontrou o final do frontmatter
                    # Extrai o frontmatter e o resto do conteúdo
                    frontmatter = conteudo[4:fim_frontmatter]  # Remove o "---\n" inicial
                    resto_conteudo = conteudo[fim_frontmatter + 4:]  # Resto do conteúdo após o frontmatter
                    
                    # Remove qualquer dg-publish existente
                    frontmatter = re.sub(r'dg-publish:\s*true\s*\n', '', frontmatter)
                    
                    # Garante que o frontmatter não comece com uma linha em branco
                    frontmatter = frontmatter.lstrip()
                    
                    # Cria o novo frontmatter com dg-publish: true como primeiro campo
                    novo_frontmatter = "---\ndg-publish: true\n" + frontmatter
                    
                    # Verifica se o último caractere é uma quebra de linha
                    if not novo_frontmatter.endswith('\n'):
                        novo_frontmatter += '\n'
                        
                    novo_frontmatter += "---"
                    
                    # Garante uma linha em branco após o frontmatter
                    if not resto_conteudo.startswith('\n\n'):
                        if resto_conteudo.startswith('\n'):
                            resto_conteudo = '\n' + resto_conteudo[1:]
                        else:
                            resto_conteudo = '\n\n' + resto_conteudo
                    
                    # Junta tudo
                    novo_conteudo = novo_frontmatter + resto_conteudo
                    
                    # Verifica se houve mudança
                    if novo_conteudo != conteudo:
                        with open(caminho_completo, 'w', encoding='utf-8') as f:
                            f.write(novo_conteudo)
                        print(f"Atualizado frontmatter em '{arquivo}'")
                        arquivos_modificados += 1
                    else:
                        print(f"Ignorando '{arquivo}': já está no formato correto")
                        arquivos_ignorados += 1
                    continue
            
            # Se não tem frontmatter ou o formato não foi reconhecido, adiciona um novo
            if not conteudo.startswith('---\n'):
                novo_conteudo = frontmatter_padrao + conteudo
                with open(caminho_completo, 'w', encoding='utf-8') as f:
                    f.write(novo_conteudo)
                print(f"Adicionado frontmatter em '{arquivo}'")
                arquivos_modificados += 1
            
    print(f"\nProcesso concluído.")
    print(f"Arquivos modificados: {arquivos_modificados}")
    print(f"Arquivos ignorados: {arquivos_ignorados}")
    print(f"Total de arquivos analisados: {arquivos_modificados + arquivos_ignorados}")

if __name__ == "__main__":
    adicionar_frontmatter() 