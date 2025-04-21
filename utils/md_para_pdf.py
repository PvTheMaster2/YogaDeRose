import os
import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch, mm, cm
from bs4 import BeautifulSoup
import re
import glob

def md_para_pdf(diretorio=None):
    # Se nenhum diretório for fornecido, usa o diretório atual
    if diretorio is None:
        diretorio = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Buscando arquivos Markdown em: {diretorio}")
    
    # Listar todos os arquivos .md no diretório
    arquivos_md = glob.glob(os.path.join(diretorio, "*.md"))
    
    print(f"Arquivos encontrados: {len(arquivos_md)}")
    for arquivo in arquivos_md:
        print(f"  - {os.path.basename(arquivo)}")
    
    if not arquivos_md:
        print("Nenhum arquivo Markdown (.md) encontrado no diretório.")
        return
    
    # Configurar estilos
    styles = getSampleStyleSheet()
    
    # Estilos personalizados para diferentes elementos
    titulo_style = ParagraphStyle(
        name='TituloStyle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=15,
        alignment=1,  # Centralizado
        textColor=colors.darkblue
    )
    
    heading1_style = ParagraphStyle(
        name='Heading1Style',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        textColor=colors.darkblue
    )
    
    heading2_style = ParagraphStyle(
        name='Heading2Style',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=10,
        textColor=colors.navy
    )
    
    heading3_style = ParagraphStyle(
        name='Heading3Style',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8,
        textColor=colors.blue
    )
    
    code_style = ParagraphStyle(
        name='CodeStyle',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=9,
        leading=12,
        backColor=colors.lightgrey,
        borderPadding=5,
        borderWidth=0.5,
        borderColor=colors.grey
    )
    
    normal_style = ParagraphStyle(
        name='NormalStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        spaceBefore=6,
        spaceAfter=6
    )
    
    # Estilo específico para células de tabela
    tabela_style = ParagraphStyle(
        name='TabelaStyle',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        spaceBefore=0,
        spaceAfter=0
    )
    
    tabela_header_style = ParagraphStyle(
        name='TabelaHeaderStyle',
        parent=tabela_style,
        fontName='Helvetica-Bold',
        alignment=1  # Centralizado
    )
    
    link_style = ParagraphStyle(
        name='LinkStyle',
        parent=normal_style,
        textColor=colors.blue,
        underline=True
    )
    
    # Processar cada arquivo Markdown
    for md_file in arquivos_md:
        try:
            # Determinar nome do arquivo PDF de saída
            nome_base = os.path.splitext(os.path.basename(md_file))[0]
            caminho_pdf = os.path.join(diretorio, f"{nome_base}.pdf")
            
            print(f"Processando: {md_file} -> {caminho_pdf}")
            
            # Ler o conteúdo do arquivo Markdown
            with open(md_file, 'r', encoding='utf-8') as file:
                md_content = file.read()
            
            print(f"  - Arquivo lido: {len(md_content)} caracteres")
            
            # Converter Markdown para HTML usando extensões apropriadas
            html_content = markdown.markdown(
                md_content, 
                extensions=[
                    'tables',
                    'fenced_code',
                    'codehilite',
                    'toc',
                    'nl2br',
                    'attr_list'
                ]
            )
            
            print(f"  - Markdown convertido para HTML: {len(html_content)} caracteres")
            
            # Usar BeautifulSoup para analisar o HTML
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Criar o documento PDF
            doc = SimpleDocTemplate(
                caminho_pdf,
                pagesize=A4,
                rightMargin=15*mm,
                leftMargin=15*mm,
                topMargin=20*mm,
                bottomMargin=20*mm,
                title=nome_base
            )
            
            # Calcular largura disponível para conteúdo
            largura_pagina = A4[0] - 30*mm  # 15mm margem esquerda + 15mm margem direita
            
            story = []
            
            # Adicionar título do documento (nome do arquivo)
            story.append(Paragraph(nome_base.replace('_', ' ').title(), titulo_style))
            story.append(Spacer(1, 10*mm))
            
            print("  - Processando elementos HTML para o PDF")
            elementos_encontrados = []
            
            # Processar elementos HTML e adicionar ao PDF
            for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'pre', 'ul', 'ol', 'table']):
                elementos_encontrados.append(element.name)
                if element.name == 'h1':
                    story.append(Paragraph(element.get_text(), heading1_style))
                elif element.name == 'h2':
                    story.append(Paragraph(element.get_text(), heading2_style))
                elif element.name == 'h3' or element.name == 'h4':
                    story.append(Paragraph(element.get_text(), heading3_style))
                elif element.name == 'p':
                    story.append(Paragraph(element.get_text(), normal_style))
                elif element.name == 'pre':
                    code = element.get_text()
                    story.append(Paragraph(code, code_style))
                elif element.name == 'table':
                    # Processar tabela
                    table_data = []
                    num_colunas = 0
                    
                    # Primeiro, determinar o número de colunas na tabela
                    for tr in element.find_all('tr'):
                        colunas = len(tr.find_all(['td', 'th']))
                        if colunas > num_colunas:
                            num_colunas = colunas
                    
                    if num_colunas == 0:
                        continue  # Tabela vazia, pular
                    
                    # Processar cabeçalho, usando Paragraph para permitir quebra de linha
                    tem_cabecalho = False
                    if element.find('thead'):
                        tem_cabecalho = True
                        header_row = []
                        for th in element.find('thead').find_all('th'):
                            header_row.append(Paragraph(th.get_text(), tabela_header_style))
                        
                        # Garantir que a linha do cabeçalho tem o número correto de colunas
                        while len(header_row) < num_colunas:
                            header_row.append(Paragraph("", tabela_header_style))
                        
                        table_data.append(header_row)
                    
                    # Processar corpo da tabela
                    for tr in element.find_all('tr'):
                        if tr.parent.name != 'thead':  # Pular linhas de cabeçalho já processadas
                            row = []
                            for td in tr.find_all(['td', 'th']):
                                # Usar Paragraph para permitir quebra de texto
                                row.append(Paragraph(td.get_text(), tabela_style))
                            
                            # Garantir que cada linha tem o número correto de colunas
                            while len(row) < num_colunas:
                                row.append(Paragraph("", tabela_style))
                            
                            if row:  # Adicionar apenas se a linha não estiver vazia
                                table_data.append(row)
                    
                    # Criar tabela ReportLab com largura automática
                    if table_data:
                        # Calcular larguras de coluna
                        col_widths = [largura_pagina / num_colunas] * num_colunas
                        
                        # Criar a tabela com larguras de coluna definidas
                        table = Table(table_data, colWidths=col_widths)
                        
                        # Estilizar a tabela
                        table_style_commands = [
                            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                            ('FONTSIZE', (0, 0), (-1, -1), 9),
                            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                            ('TOPPADDING', (0, 0), (-1, -1), 6),
                            ('LEFTPADDING', (0, 0), (-1, -1), 4),
                            ('RIGHTPADDING', (0, 0), (-1, -1), 4),
                        ]
                        
                        # Estilo adicional para o cabeçalho, se existir
                        if tem_cabecalho:
                            table_style_commands.extend([
                                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                            ])
                        
                        # Estilo zebrado para linhas do corpo
                        start_row = 1 if tem_cabecalho else 0
                        if len(table_data) > start_row:
                            table_style_commands.append(
                                ('ROWBACKGROUNDS', (0, start_row), (-1, -1), [colors.whitesmoke, colors.white])
                            )
                        
                        style = TableStyle(table_style_commands)
                        table.setStyle(style)
                        
                        # Permitir que a tabela quebre entre páginas
                        table.hAlign = 'LEFT'
                        table.repeatRows = 1 if tem_cabecalho else 0
                        
                        # Adicionar ao documento
                        story.append(table)
                        story.append(Spacer(1, 5*mm))
                
                # Espaçamento entre elementos
                story.append(Spacer(1, 3*mm))
            
            print(f"  - Elementos encontrados: {', '.join(set(elementos_encontrados))}")
            print(f"  - Total de elementos: {len(elementos_encontrados)}")
            
            if len(story) <= 2:  # Apenas título e espaço
                print("  - AVISO: Nenhum conteúdo foi extraído do arquivo Markdown!")
            
            # Construir o PDF
            print("  - Gerando PDF...")
            doc.build(story)
            print(f"  - PDF gerado com sucesso: {caminho_pdf}")
            
        except Exception as e:
            print(f"Erro ao processar o arquivo {md_file}: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    # Executar o script diretamente
    md_para_pdf() 