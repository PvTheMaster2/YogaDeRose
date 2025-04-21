---
created: 2025-04-18T04:24
updated: 2025-04-18T04:56
---
```button
name Publicar Todas as Notas 🌱
type javascript
class garden-button
action
const api = app.plugins.plugins["digital-garden"]?.publishManager;
if (!api) {
  new Notice("🚫 Digital Garden plugin não está carregado!");
} else {
  const files = app.vault.getMarkdownFiles();
  const toPublish = files.filter(file =>
    app.metadataCache.getFileCache(file)?.frontmatter?.["dg-publish"] === true
  );
  
  const result = await api.publishMultipleNotes(toPublish);
  new Notice(`✅ ${result.success.length} notas publicadas! ❌ ${result.failed.length} falharam.`);
}```
