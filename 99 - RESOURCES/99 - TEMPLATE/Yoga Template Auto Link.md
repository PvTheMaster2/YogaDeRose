---
created: 2025-04-18T00:39
updated: 2025-04-18T00:51
---
<%*
// Template avançado com auto-linking para notas sobre Yoga
const title = await tp.system.prompt("Título da nota");
const now = new Date();
const timestamp = now.toISOString().replace(/[-:]/g, "").split(".")[0];
const dateStr = now.toISOString().split("T")[0];

// Obter tags
const tagOptions = ["theme/yoga", "theme/filosofia", "theme/tantra", "theme/energia", "theme/pratica"];
const selectedTags = await tp.system.suggester(
  ["Yoga", "Filosofia", "Tantra", "Energia", "Prática"], 
  tagOptions,
  true, 
  "Selecione tags (múltipla escolha)"
);

// Obter tipo de nota
const typeOptions = ["type/concept", "type/practice", "type/reflection", "type/reference"];
const selectedType = await tp.system.suggester(
  ["Conceito", "Prática", "Reflexão", "Referência"], 
  typeOptions, 
  false, 
  "Selecione o tipo de nota"
);

// Construir array de tags
let tags = ["source/trato-yoga"];
if (selectedTags && selectedTags.length > 0) {
  tags = tags.concat(selectedTags);
}
if (selectedType) {
  tags.push(selectedType);
}

// Obter a fonte
const source = await tp.system.prompt("Fonte (deixe em branco para 'Trato de Yôga do Mestre De Rose')") || "Trato de Yôga do Mestre De Rose";

// Formatando as tags corretamente para YAML
const tagsStr = tags.map(t => `"${t}"`).join(", ");

// Buscar arquivos relacionados baseados no título
const dv = app.plugins.plugins.dataview?.api;
let relatedLinks = "";

if (dv) {
  // Dividir o título em palavras para buscar
  const titleWords = title.toLowerCase().split(/\s+/).filter(word => word.length > 3);
  const searchTerms = titleWords.join(" OR ");
  
  try {
    // Buscar notas que contêm palavras do título
    const pages = dv.pages('"10 - PERMANENT/Zettels/Yoga"')
      .where(p => {
        // Verificar se o conteúdo da página contém alguma das palavras-chave
        const content = p.file.content?.toLowerCase() || "";
        return titleWords.some(word => content.includes(word));
      })
      .sort(p => p.file.name)
      .limit(5);
    
    if (pages.length > 0) {
      relatedLinks = "\n### Notas Possivelmente Relacionadas\n\n";
      
      for (const page of pages.values) {
        const pageTitle = page.file.name;
        // Só incluir se não for a própria nota
        if (pageTitle.toLowerCase() !== title.toLowerCase()) {
          relatedLinks += `- [[10 - PERMANENT/Zettels/Yoga/${pageTitle}|${page.title || pageTitle}]]\n`;
        }
      }
    }
  } catch (error) {
    relatedLinks = "\n<!-- Erro ao buscar notas relacionadas: " + error.message + " -->\n";
  }
}

// Buscar tags relacionadas e sugerir conexões
let tagConnections = "";
if (dv && tags.length > 0) {
  try {
    const relatedByTags = dv.pages('"10 - PERMANENT/Zettels/Yoga"')
      .where(p => {
        // Verificar se a página tem pelo menos uma tag em comum
        if (!p.tags) return false;
        const pageTags = Array.isArray(p.tags) ? p.tags : [p.tags];
        return tags.some(tag => pageTags.some(pageTag => 
          pageTag.includes(tag.replace(/^"(.*)"$/, '$1'))
        ));
      })
      .sort(p => p.file.name)
      .limit(5);
    
    if (relatedByTags.length > 0) {
      tagConnections = "\n### Conexões por Tags\n\n";
      
      for (const page of relatedByTags.values) {
        const pageTitle = page.file.name;
        // Só incluir se não for a própria nota
        if (pageTitle.toLowerCase() !== title.toLowerCase()) {
          tagConnections += `- [[10 - PERMANENT/Zettels/Yoga/${pageTitle}|${page.title || pageTitle}]]\n`;
        }
      }
    }
  } catch (error) {
    tagConnections = "\n<!-- Erro ao buscar conexões por tags: " + error.message + " -->\n";
  }
}

// Conteúdo principal
const conteudo = await tp.system.prompt("Conteúdo principal da nota");

// Gerar frontmatter e conteúdo
tR = `---
id: ${timestamp}
title: "${title}"
tags: [${tagsStr}]
zettel-type: literature
source: "${source}"
created: ${dateStr}
---

# ${title}

## 🌱 Resumo

${await tp.system.prompt("Resumo da nota (opcional)")}

## 📝 Detalhes

${conteudo}

## 🔗 Links e Referências

${relatedLinks}${tagConnections}

### Adicionar Links Manualmente

<!-- Adicione links relacionados abaixo -->

`;
_%> 