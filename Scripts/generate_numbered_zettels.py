#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import yaml
from pathlib import Path
from datetime import datetime

# Configuração do diretório de saída
OUTPUT_DIR = "10 - PERMANENT/Zettels/Yoga"

# Função para gerar o frontmatter 
def generate_frontmatter(title, section_number, tags=None):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%dT%H%M%S")
    date_str = now.strftime("%Y-%m-%d")
    
    if tags is None:
        tags = ["source/trato-yoga", "type/concept", "theme/yoga"]
    
    tags_str = ", ".join([f'"{tag}"' for tag in tags])
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

# Função para criar arquivo
def create_zettel(section_number, title, content, tags=None):
    # Criar nome de arquivo
    clean_number = section_number.replace('.', '-')
    filename = f"{clean_number}-{title.lower().replace(' ', '-')}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Gerar frontmatter
    frontmatter = generate_frontmatter(title, section_number, tags)
    
    # Escrever arquivo
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write(content)
        f.write("\n\n## 🔗 Links e Referências")
    
    print(f"Criado zettel: {filename}")

# Assegurar que o diretório existe
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

# Lista de zettels a serem criados, baseada na imagem
zettels = [
    # Principais seções
    ("1", "Definições", "Yôga é qualquer metodologia estritamente prática que conduza ao samádhi.\n\nSamádhi é o estado de hiperconsciência e autoconhecimento que só o Yôga proporciona.\n\nnovÆ sed antiquÆ\n\nSwáSthya Yôga é o nome da sistematização do Yôga Antigo."),
    
    ("2", "Sem reeducação comportamental", "Para funcionar, o Yôga, precisa que você adote os conceitos de reeducação comportamental. Sem um bom relacionamento humano e sem um bom relacionamento afetivo, sem mudar sua atitude, sua alimentação, sem eliminar o uso do fumo, do álcool e das drogas, ele não funciona."),
    
    ("3", "O que é o DeRose Method", "O DeRose Method é uma proposta de boas coisas: boa qualidade de vida, boas maneiras, boas relações humanas, boa cultura, boa alimentação, boa forma, bom ambiente e bons ideais."),
    
    ("4", "Cronologia Histórica", "O Yôga Antigo e o Yôga Moderno. O primeiro ocupa um espaço de 4000 anos. O segundo ocupa apenas os últimos mil anos. Portanto, a primeira divisão deveria ser quatro vezes maior do que a segunda."),
    
    ("5", "COMO SE PROCESSOU A TRANSFORMAÇÃO", "No período mais antigo, Pré-Clássico, o Yôga tinha raízes Tantra e Sámkhya (TS). No período Clássico, preservou a raiz Sámkhya, mas, com a ocupação ariana, passou a ser Brahmácharya (BS)."),
    
    ("6", "ARVORE DO YÔGA", "Os primeiros oito ramos de Yôga a surgir foram: Ásana Yôga, Rája Yôga, Bhakti Yôga, Karma Yôga, Jñána Yôga, Laya Yôga, Mantra Yôga e Tantra Yôga."),
    
    ("7", "TIPOS DE YÔGA", "Para sua ilustração, vamos descrever alguns tipos de Yôga."),
    
    # Subseções
    ("5.1", "Tipos de Yôgin", "### a) Um yôgin do tronco Pré-Clássico\n\n- **T**: Por ser tântrico, seu comportamento é pautado pelo matriarcalismo, pela sensorialidade e pela desrepressão.\n- **S**: Por ser Sámkhya, é naturalista (não-espiritualista) e interpreta os fenômenos desencadeados pelo Yôga como ocorrências que obedecem às leis da Natureza."),
    
    ("5.1.1", "a) Um yôgin do tronco Pré-Clássico", "- **T**: Por ser tântrico, seu comportamento é pautado pelo matriarcalismo, pela sensorialidade e pela desrepressão.\n- **S**: Por ser Sámkhya, é naturalista (não-espiritualista) e interpreta os fenômenos desencadeados pelo Yôga como ocorrências que obedecem às leis da Natureza."),
    
    ("5.1.2", "b) Um yôgin do tronco Clássico", "- **B**: Por já ser brahmácharya, é marcado pelo patriarcalismo, pela antissensorialidade e pela repressão.\n- **S**: Por ser Sámkhya, também é naturalista (não-espiritualista) e interpreta os fenômenos desencadeados pelo Yôga como ocorrências que obedecem às leis da Natureza."),
    
    ("5.1.3", "c) Um yôgin do tronco Medieval", "- **B**: Por ser brahmácharya, é vincado pelo patriarcalismo, pela antissensorialidade e pela repressão.\n- **V**: Por ser Vêdánta, é espiritualista, não raro, místico, e atribui os fenômenos produzidos pela prática do Yôga à graça divina e ao mérito espiritual do praticante."),
    
    ("5.1.4", "d) Um yôgin do tronco Contemporâneo", "- **T**: Por ser tântrico, seu comportamento é pautado pelo matriarcalismo, pela sensorialidade e pela desrepressão.\n- **V**: Por ser Vêdánta, é espiritualista, não raro, místico, e atribui os fenômenos produzidos pela prática do Yôga à graça divina e ao mérito espiritual do praticante."),
    
    # Tipos de Yoga
    ("7.1", "Descrição de várias modalidades de Yôga", "Para sua ilustração, vamos descrever alguns tipos de Yôga."),
    
    ("7.1.1", "Rája Yôga, o Yôga mental", "Rája significa real (dos reis). Consiste em quatro partes ou angas: pratyáhára (abstração dos sentidos), dháraná (concentração mental), dhyána (meditação) e samádhi (hiperconsciência)."),
    
    ("7.1.2", "Bhakti Yôga, o Yôga devocional", "Bhakti significa devoção. O Yôga devocional não é forçosamente espiritualista. Em suas origens pré-clássicas, sua fundamentação era naturalista."),
    
    ("7.1.3", "Karma Yôga, o Yôga da ação", "Karma significa ação. É um Yôga que induz à ação. Sua vertente medieval passou a ter enfatizadas conotações da filosofia Vêdánta."),
    
    ("7.1.4", "Jñána Yôga, o Yôga do autoconhecimento", "Jñána significa conhecimento. O método dessa modalidade consiste em meditar na resposta que o seu psiquismo elaborar para a pergunta \"quem sou eu?\"."),
    
    ("7.1.5", "Laya Yôga, o Yôga das paranormalidades", "Laya significa dissolução. A intenção neste tipo de Yôga é dissolver a personalidade, ou seja, eliminar a barreira que existe entre o ego e o self."),
    
    ("7.1.6", "Mantra Yôga, o Yôga do domínio do som e do ultrassom", "Mantra significa vocalização. Trata-se de um ramo de Yôga que pretende alcançar a meta através da ressonância transmitida aos centros de energia do próprio corpo."),
    
    ("7.1.7", "Tantra Yôga, o Yôga da sensorialidade", "Tantra significa a maneira correta de fazer qualquer coisa, autoridade, prosperidade, riqueza; encordoamento (de um instrumento musical) etc."),
    
    ("7.1.8", "SwáSthya Yôga, o Yôga Antigo, de raízes pré-clássicas", "SwáSthya significa auto-suficiência, saúde, bem-estar, conforto, satisfação. SwáSthya Yôga é o nome da sistematização do Yôga Antigo."),
]

# Criar os zettels
for section_number, title, content in zettels:
    create_zettel(section_number, title, content)

print(f"Processo concluído! Criados {len(zettels)} zettels com numeração estruturada.") 