import markdown
import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import re

def markdown_to_pdf(markdown_file, output_pdf):
    # Ler o conteúdo do arquivo markdown
    with open(markdown_file, 'r', encoding='utf-8') as file:
        markdown_text = file.read()
    
    # Converter markdown para HTML
    html_content = markdown.markdown(markdown_text, extensions=['tables', 'fenced_code'])
    
    # Criar o documento PDF
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Definir estilos personalizados com nomes diferentes para evitar conflitos
    heading1_style = ParagraphStyle(
        name='CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12
    )
    
    heading2_style = ParagraphStyle(
        name='CustomHeading2',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=10
    )
    
    heading3_style = ParagraphStyle(
        name='CustomHeading3',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8
    )
    
    code_style = ParagraphStyle(
        name='CustomCode',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=9,
        leading=12,
        backColor=colors.lightgrey
    )
    
    # Quebrar o HTML em parágrafos e processá-los
    story = []
    
    # Dividir o conteúdo HTML em elementos
    # Remover as tags HTML, mantendo somente o texto
    clean_text = re.sub(r'<.*?>', '', html_content)
    paragraphs = clean_text.split('\n\n')
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
            
        if para.startswith('# '):
            # Cabeçalho nível 1
            text = para[2:]
            story.append(Paragraph(text, heading1_style))
        elif para.startswith('## '):
            # Cabeçalho nível 2
            text = para[3:]
            story.append(Paragraph(text, heading2_style))
        elif para.startswith('### '):
            # Cabeçalho nível 3
            text = para[4:]
            story.append(Paragraph(text, heading3_style))
        elif para.startswith('```'):
            # Bloco de código
            code_content = para.strip('`')
            story.append(Paragraph(code_content, code_style))
        else:
            # Parágrafo normal
            story.append(Paragraph(para, styles['Normal']))
            
        story.append(Spacer(1, 0.2 * inch))
    
    # Construir o PDF
    doc.build(story)
    print(f"PDF gerado com sucesso: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python converter_para_pdf.py arquivo_markdown.md [arquivo_saida.pdf]")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    
    if len(sys.argv) >= 3:
        output_pdf = sys.argv[2]
    else:
        # Gerar nome do arquivo de saída baseado no nome do arquivo de entrada
        base_name = os.path.splitext(markdown_file)[0]
        output_pdf = f"{base_name}.pdf"
    
    markdown_to_pdf(markdown_file, output_pdf) 