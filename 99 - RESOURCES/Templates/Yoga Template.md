---
created: 2025-04-18T00:21
updated: 2025-04-18T00:21
---
<%*
// Template para notas sobre Yoga
const title = await tp.system.prompt("Título da nota");
const now = new Date();
const timestamp = now.toISOString().replace(/[-:]/g, "").split(".")[0];
const dateStr = now.toISOString().split("T")[0];

// Obter tags - note que removemos o # do início
const tagOptions = ["theme/yoga", "theme/filosofia", "theme/tantra", "theme/energia", "theme/pratica"];
const selectedTags = await tp.system.suggester(
  ["Yoga", "Filosofia", "Tantra", "Energia", "Prática"], 
  tagOptions,
  true, 
  "Selecione tags (múltipla escolha)"
);

// Obter tipo de nota - note que removemos o # do início
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

// Formatando corretamente os tags em YAML - colocando cada tag entre aspas
const tagsStr = tags.map(t => `"${t}"`).join(", ");

// Gerar frontmatter
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

${await tp.system.prompt("Conteúdo principal da nota")}

## 🔗 Links e Referências

<!-- Adicionar links relacionados -->

`;
_%> 