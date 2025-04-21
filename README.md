---
created: 2025-04-18T00:06
updated: 2025-04-18T02:57
---
# 🧘 Trato de Yôga - Processamento para Obsidian Zettelkasten

Este projeto contém scripts e recursos para converter o documento "Trato de Yôga do Mestre De Rose" em um sistema Zettelkasten no Obsidian, facilitando o estudo e a referência do material.

## 📋 Visão Gerall

O pipeline de processamento tem as seguintes etapas:

1. **Conversão do documento LaTeX para Markdown limpo**
2. **Divisão do conteúdo em notas Zettelkasten atômicas**
3. **Criação de um Mapa de Conteúdo (MOC) para navegação**
4. **Configuração de templates para criação de novas notas**

## 🚀 Como Executar

### Pré-requisitos

- Python 3.6+
- Obsidian instalado
- Plugins recomendados para Obsidian:
  - Templater
  - Dataview
  - Smart Connections
  - Map of Content

### Execução do Pipeline

1. Clone ou baixe este repositório
2. Certifique-se de que o arquivo original `Yoga_R00.md` está em `00 - INBOX/02 - LITERATURE/`
3. Execute o script principal:

```bash
python Scripts/run_yoga_pipeline.py
```

Para executar apenas partes específicas do pipeline:

```bash
# Pular a conversão LaTeX -> Markdown (se já tiver o arquivo limpo)
python Scripts/run_yoga_pipeline.py --skip-conversion

# Pular a geração de Zettels (se já tiver as notas)
python Scripts/run_yoga_pipeline.py --skip-zettels

# Regenerar os Zettels com a estrutura hierárquica correta
python Scripts/run_yoga_pipeline.py --regenerate

# Atualizar links entre notas
python Scripts/run_yoga_pipeline.py --update-links
```

## 📂 Estrutura do Projeto

```
.
├── 00 - INBOX
│   └── 02 - LITERATURE       # Documentos de entrada
│       ├── Yoga_R00.md       # Documento original em LaTeX/Markdown
│       └── Yoga_R00_cleaned.md  # Documento convertido para Markdown puro
├── 10 - PERMANENT
│   └── Zettels
│       └── Yoga              # Notas Zettelkasten geradas
├── 30 - MPS OF CONTENTS      # Mapas de conteúdo
│   └── Yoga MOC.md           # MOC gerado para o Trato de Yoga
├── 99 - RESOURCES
│   └── Templates             # Templates para Obsidian
│       └── Yoga Template.md  # Template para criação de novas notas sobre Yoga
├── Scripts                   # Scripts de processamento
│   ├── convert_latex_to_md.py    # Converte LaTeX para Markdown
│   ├── generate_zettels.py       # Gera notas Zettelkasten
│   ├── update_connections.py     # Atualiza links entre notas
│   └── run_yoga_pipeline.py      # Executa todo o pipeline
└── README.md                 # Este arquivo
```

## 🔖 Taxonomia de Tags

O sistema usa as seguintes categorias de tags:

- **`#type/`** - Define o tipo da nota:
  - `#type/concept` - Conceito principal
  - `#type/subconcept` - Subconceto
  - `#type/detail` - Detalhe específico
  - `#type/practice` - Prática
  - `#type/reflection` - Reflexão pessoal
  - `#type/reference` - Referência externa

- **`#theme/`** - Define o tema da nota:
  - `#theme/yoga` - Relacionado ao Yoga
  - `#theme/filosofia` - Aspectos filosóficos
  - `#theme/tantra` - Relacionado ao Tantra
  - `#theme/energia` - Energia, chakras, respiração
  - `#theme/pranayama` - Técnicas de respiração
  - `#theme/asana` - Posturas físicas
  - `#theme/meditacao` - Meditação e concentração
  - `#theme/mantra` - Mantras e sons

- **`#source/`** - Define a fonte da nota:
  - `#source/trato-yoga` - Vindo do Trato de Yoga

## 🔄 Fluxo de Trabalho no Obsidian

1. **Navegação pelo MOC**: Use o arquivo `30 - MPS OF CONTENTS/Yoga MOC.md` como ponto de partida
2. **Criação de novas notas**: Use o template em `99 - RESOURCES/Templates/Yoga Template Auto Link.md`
3. **Manutenção de conexões**: Execute periodicamente o script `Scripts/update_connections.py` para atualizar links sugeridos
4. **Consultas com Dataview**: Use consultas como:

```
TABLE tags as "Tags"
FROM #source/trato-yoga
WHERE contains(tags, "#theme/filosofia")
SORT file.name ASC
```

## 🔢 Estrutura Hierárquica Numérica

Um aspecto fundamental deste projeto é a preservação da estrutura hierárquica numérica do documento original para organizar melhor as notas e facilitar a navegação:

1. **Formato do número**:
   - Seções principais: `1`, `2`, `3`, etc.
   - Subseções: `5.1`, `7.1`, `24.3`, etc.
   - Sub-subseções: `5.1.1`, `7.1.3`, `24.3.25`, etc.

2. **Nomes de arquivos**:
   - Os números estão incorporados nos nomes de arquivos, substituindo pontos por hífens:
   - Exemplo: `5-1-2-b-um-yogin-do-tronco-classico.md` para a seção `5.1.2 b) Um yôgin do tronco Clássico`

3. **Títulos das notas**:
   - Os títulos preservam os números originais para facilitar a referência cruzada:
   - Exemplo: `24.3.25 – 25 - Súrya pránáyáma - respiração pela narina positiva ou solar`

4. **MOC estruturado**:
   - O MOC agrupa as notas de acordo com sua hierarquia numérica, facilitando a navegação pelo conteúdo

5. **Benefícios**:
   - Preserva a estrutura original do documento
   - Facilita a localização de tópicos específicos
   - Mantém as relações hierárquicas entre conceitos
   - Torna o sistema mais utilizável para quem já está familiarizado com o material original

## 🔧 Personalização

Você pode personalizar:

- **Taxonomia de tags**: Edite a função `generate_frontmatter()` em `generate_zettels.py`
- **Estrutura do MOC**: Edite a função `create_moc()` em `generate_zettels.py`
- **Template para novas notas**: Edite o arquivo `Yoga Template Auto Link.md`

## 📚 Funcionalidades Adicionais

- **Smart Connections**: Ative o plugin para obter sugestões automáticas de links entre notas
- **Integração com flashcards**: Use plugins como Spaced Repetition ou AnkiConnect para gerar flashcards 

## 🔄 Últimas Atualizações e Melhorias

### Aprimoramentos no Sistema de Links (2025-04-18)

As seguintes melhorias foram implementadas para resolver problemas com links e enriquecer o MOC:

1. **Correção do formato de links** - Substituímos as barras invertidas (`\`) por barras normais (`/`) em todos os links gerados, garantindo compatibilidade com o Obsidian.

2. **Inclusão de caminhos completos** - Adicionamos o caminho completo `10 - PERMANENT/Zettels/Yoga/` nos links para que o Obsidian possa localizá-los corretamente.

3. **Extração de subseções** - Implementamos a detecção e inclusão de subseções (marcadas com ###) no MOC, criando uma nova seção dedicada "🔍 Subseções por Tópico".

4. **Organização hierárquica** - As subseções são agrupadas por nota, permitindo visualizar a estrutura hierárquica do conteúdo.

5. **Tratamento de links antigos** - Adicionamos lógica para detectar e substituir links no formato antigo no MOC.

6. **Manutenção da estrutura existente** - Preservamos outras seções do MOC ao fazer atualizações.

### Scripts Principais

Os arquivos principais que compõem o núcleo do sistema são:

1. `Scripts/improved_converter.py` - Responsável pela conversão inicial de formatos e codificação
2. `Scripts/extract_with_numbering.py` - Cria Zettels numerados sequencialmente
3. `Scripts/update_connections.py` - Gerencia conexões entre notas e mantém o MOC atualizado

## ⚠️ Problemas Comuns e Soluções

### Formatação de Links no Obsidian

O problema mais comum encontrado foi a formatação incorreta de links:

1. **Problema**: Links formatados com barras invertidas (`\`) não funcionam no Obsidian
   - **Solução**: Use sempre barras normais (`/`) nos caminhos, mesmo em sistemas Windows

2. **Problema**: Links sem o caminho completo não são encontrados
   - **Solução**: Use sempre o caminho completo para as notas, ex: `[[10 - PERMANENT/Zettels/Yoga/arquivo|Título]]`

3. **Problema**: MOC com links quebrados
   - **Solução**: Execute o script `update_connections.py` para atualizar todos os links

4. **Problema**: Links de texto simples nas seções do MOC
   - **Solução**: Use a função `update_section_links()` para converter links de texto como `* Título` em links wiki completos

### Correções nos Scripts e Templates

Foram necessárias as seguintes correções:

1. No script `update_connections.py`:
   - Substituir `\\` por `/` nos caminhos
   - Usar o caminho completo para os links
   - Adicionar função para converter links de texto simples nas seções
   - Melhorar a função `update_moc` para evitar duplicação de links
   - Implementar extração e agrupamento de subseções (###) das notas

2. No template `Yoga Template Auto Link.md`:
   - Atualizar a função de geração de links para usar o caminho completo

### Problemas com Estrutura Hierárquica

1. **Problema**: Perda da numeração hierárquica original ao gerar zettels
   - **Solução**: Modificamos o script `generate_zettels.py` para detectar e preservar a numeração original

2. **Problema**: Nomes de arquivos sem a numeração hierárquica
   - **Solução**: Implementamos a função `create_zettel_filename()` que incorpora o número de seção no nome do arquivo

3. **Problema**: MOC sem estrutura hierárquica clara
   - **Solução**: Aprimoramos a função `create_moc()` para organizar as notas por sua numeração hierárquica

## 🧠 Boas Práticas e Lições Aprendidas

### O Que Fazer

1. **Sempre use caminhos completos**: Em todos os links, scripts e templates, use o caminho completo a partir da raiz do vault.

2. **Mantenha consistência nos formatos**: Use sempre barras normais (`/`) em todos os caminhos, independente do sistema operacional.

3. **Automatize a manutenção**: Execute periodicamente o script `update_connections.py` para manter links atualizados.

4. **Teste após mudanças**: Após executar scripts, verifique se os links estão funcionando corretamente.

5. **Use templates avançados**: O template `Yoga Template Auto Link.md` inclui funcionalidades para sugestão automática de links.

6. **Organize por categorias**: Mantenha a estrutura de pastas e o MOC organizado por categorias lógicas.

7. **Estruture o MOC em seções**: Use seções como "Por Categorias", "Todas as Notas" e "Seções Principais" para facilitar a navegação.

8. **Preserve a estrutura numérica original**: Mantenha a numeração hierárquica do documento original nos nomes de arquivos e títulos.

### O Que Não Fazer

1. **Não edite manualmente o MOC**: Evite editar manualmente o MOC, pois isso pode criar inconsistências. Use os scripts.

2. **Não use barras invertidas**: Não use `\` em caminhos, mesmo em sistemas Windows.

3. **Não crie links com caminhos parciais**: Evite links como `[[arquivo]]` ou `[[Yoga/arquivo]]`, sempre use o caminho completo.

4. **Não ignore erros nos scripts**: Se um script falhar, investigue a causa antes de continuar.

5. **Não misture formatos de links**: Mantenha consistência no formato dos links em todo o vault.

6. **Não deixe links de texto simples**: Sempre converta links de texto em formato wiki para que sejam clicáveis.

7. **Não descarte a estrutura numérica original**: A numeração hierárquica é fundamental para a organização e navegação do material.

## 🔄 Processo de Atualização Recomendado

1. Criar novas notas usando o template `Yoga Template Auto Link.md`
2. Periodicamente (semanalmente), executar `python Scripts/update_connections.py`
3. Verificar o MOC e algumas notas para confirmar que os links estão funcionando
4. Corrigir problemas reportados pelos scripts, se houver

## 📌 Comandos Úteis

Aqui estão os comandos mais úteis para manutenção do sistema:

```bash
# Atualizar todas as conexões e links no MOC
python Scripts/update_connections.py

# Regenerar os Zettels preservando a estrutura hierárquica
python Scripts/extract_with_numbering.py

# Extrair os Zettels com numeração sequencial
python Scripts/extract_with_numbering.py

# Corrigir problemas de codificação nos arquivos
python Scripts/improved_converter.py
```

# Yoga MOC Maintenance Workflow

This automated solution helps maintain your Yoga Map of Content (MOC) by performing regular updates, suggesting connections between notes, and generating reports about topics that need additional attention.

## Overview

The workflow consists of three main scripts:

1. **MOC Update Workflow** (`moc_update_workflow.ps1`): Analyzes your notes and generates a report with:
   - New notes to add to the MOC
   - Suggested connections between existing notes
   - Topics without adequate connections

2. **Auto-Link Provider** (`create_auto_link_provider.ps1`): Creates a database of note titles to power auto-completion when creating links between notes.

3. **Scheduled Workflow** (`scheduled_workflow.ps1`): Sets up automatic monthly execution of the maintenance tasks.

## Installation

1. Download all three script files to your YOGA TRATADO directory.
2. Run the `scheduled_workflow.ps1` script with PowerShell:
   ```powershell
   .\scheduled_workflow.ps1
   ```
3. When prompted, choose whether to run the maintenance tasks immediately.

The script will:
- Create necessary directories for scripts, reports, and logs
- Schedule monthly maintenance (on the 1st of each month at 3:00 AM)
- Set up logging and error handling

## Directory Structure

The workflow creates and uses the following directory structure:

```
YOGA TRATADO/
├── 00 - INBOX/
│   ├── 02 - REPORTS/       # Contains monthly MOC update reports
│   ├── 03 - SCRIPTS/       # Contains all maintenance scripts
│   └── 04 - LOGS/          # Contains execution logs
├── 10 - PERMANENT/
│   └── Zettels/
│       └── Yoga/           # Your Yoga notes (analyzed by the scripts)
└── 30 - MPS OF CONTENT/
    └── Yoga MOC.md         # The main MOC file that gets updated
```

## Usage

### Automatic Updates

The scripts will run automatically on the scheduled date. After each run:

1. Check the latest report in `00 - INBOX/02 - REPORTS/` for suggestions
2. Review and implement the recommended actions manually

### Manual Execution

To run the maintenance workflow manually at any time:

```powershell
& "C:\Users\pedro\OneDrive\Área de Trabalho\YOGA TRATADO\00 - INBOX\03 - SCRIPTS\run_monthly_maintenance.ps1"
```

## Features

### MOC Update Workflow

- **New Note Detection**: Identifies notes that aren't yet linked in the MOC
- **Connection Analysis**: Suggests links between notes based on content similarity
- **Gap Detection**: Highlights notes with insufficient connections

### Auto-Link Provider

- **Completion Database**: Creates a database of note titles and aliases
- **Smart Suggestions**: Powers the "Auto Link Title" plugin in Obsidian
- **Title Extraction**: Pulls titles from filenames, frontmatter, and headers

## Requirements

- Windows PowerShell 5.1 or higher
- Obsidian with the "Auto Link Title" plugin installed
- Write permissions to the YOGA TRATADO directory

## Troubleshooting

If you encounter any issues:

1. Check the log file at `00 - INBOX/04 - LOGS/scheduled_workflow_log.txt`
2. Make sure all paths in the scripts match your actual directory structure
3. Verify that PowerShell has sufficient permissions to create scheduled tasks

## Customization

You can modify the scripts to change:

- The schedule frequency
- The threshold for suggesting connections
- The format of the reports
- The paths used for analysis

Look for the configuration section at the top of each script file to make adjustments.

## Maintenance

Periodically check the log files to ensure the scripts are running correctly. If you reorganize your vault or change the structure of your notes, you may need to update the scripts accordingly. 
