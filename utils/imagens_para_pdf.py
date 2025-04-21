import os
from PIL import Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Image as ReportLabImage
from reportlab.lib.units import inch

def imagens_para_pdf():
    # Obter o diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Listar todos os arquivos no diretório
    arquivos = os.listdir(diretorio_atual)
    
    # Filtrar apenas imagens JPG, JPEG e PNG
    extensoes_validas = ['.jpg', '.jpeg', '.png']
    imagens = [arquivo for arquivo in arquivos if os.path.splitext(arquivo.lower())[1] in extensoes_validas]
    
    if not imagens:
        print("Nenhuma imagem encontrada no diretório atual.")
        return
    
    # Processar cada imagem
    for imagem in imagens:
        try:
            nome_base = os.path.splitext(imagem)[0]
            caminho_imagem = os.path.join(diretorio_atual, imagem)
            caminho_pdf = os.path.join(diretorio_atual, f"{nome_base}.pdf")
            
            # Verificar o tamanho da imagem
            with Image.open(caminho_imagem) as img:
                largura, altura = img.size
            
            # Criar documento PDF
            doc = SimpleDocTemplate(
                caminho_pdf,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            # Calcular dimensões para caber na página (mantendo a proporção)
            page_width, page_height = A4
            max_width = page_width - 2 * 72  # Margem esquerda + direita
            max_height = page_height - 2 * 72  # Margem superior + inferior
            
            # Calcular escala para manter proporção
            width_ratio = max_width / largura
            height_ratio = max_height / altura
            scale = min(width_ratio, height_ratio)
            
            nova_largura = largura * scale
            nova_altura = altura * scale
            
            # Criar a imagem para o PDF
            img_relatorio = ReportLabImage(caminho_imagem, width=nova_largura, height=nova_altura)
            
            # Construir o PDF
            doc.build([img_relatorio])
            print(f"PDF criado com sucesso: {nome_base}.pdf")
            
        except Exception as e:
            print(f"Erro ao processar a imagem {imagem}: {str(e)}")

if __name__ == "__main__":
    imagens_para_pdf() 