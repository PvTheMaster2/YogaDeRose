---
created: 2025-04-14T04:02
updated: 2025-04-14T04:37
---
# 🪴 Digital Garden com Obsidian: Guia Completo de Configuração, Personalização, Publicação e Automação

Este guia passo a passo ensina **como configurar, personalizar, publicar e automatizar um _Digital Garden_** utilizando o plugin **Digital Garden (oleeskild)** no Obsidian. Apresentamos o processo desde a configuração inicial até recursos avançados de **indexação automática** e **domínio personalizado**, dividido em fases claras. Siga as instruções e dicas a seguir para criar um jardim digital robusto e elegante, pronto para ser compartilhado na web.

## ⚙️ 1. Primeira Configuração

Nesta fase inicial, vamos preparar todo o ambiente necessário para o seu Digital Garden. Você irá instalar o plugin, criar o site estático integrado ao GitHub e configurar o Obsidian para publicar notas.

### 1.1 Pré-requisitos

- **Obsidian instalado:** Certifique-se de ter o Obsidian (aplicativo de notas Markdown) instalado em seu computador e um vault (cofre) criado para suas notas.
    
- **Conta no GitHub:** Será necessário um repositório Git para armazenar as notas publicadas. Se você não tiver uma conta, crie gratuitamente em GitHub.com.
    
- **Conta no Vercel ou Netlify:** Esses serviços de hospedagem permitem publicar sites estáticos gratuitamente. Crie uma conta em pelo menos um deles (pode usar login via GitHub para facilitar). Ambas as opções oferecem um domínio gratuito (ex: `seudigitalgarden.netlify.app`) e HTTPS automático.
    

### 1.2 Instalação do plugin Digital Garden (oleeskild)

1. **Abra o Obsidian e vá em Configurações → Comunidade → Plugins da comunidade**. Certifique-se de que os _Plugins da comunidade_ estão habilitados.
    
2. **Busque por "Digital Garden"** no repositório de plugins. Identifique o plugin _Digital Garden_ desenvolvido por Ole Eskild (oleeskild).
    
3. **Instale e habilite o plugin**: Clique em **Instalar** e depois em **Ativar**. O plugin agora aparecerá na lista de plugins instalados.
    

### 1.3 Criando o repositório e site (Deploy em Netlify/Vercel)

Agora iremos criar o **repositório no GitHub e configurar o site estático** automaticamente usando um modelo pronto fornecido pelo plugin:

1. **Acesse o template do Digital Garden**: Abra a página do repositório template fornecido pelo autor. Você pode encontrar o link no próprio Obsidian (seção de documentação do plugin) ou usar diretamente: há botões "Deploy to Netlify" e "Deploy to Vercel" disponíveis no repositório do projeto.
    
2. **Deploy via botão:** Clique no botão de deploy referente à sua plataforma de hospedagem escolhida:
    
    - **Netlify:** Botão _"Deploy to Netlify"_.
        
    - **Vercel:** Botão _"Deploy to Vercel"_.
        
3. **Crie o repositório no seu GitHub:** Ao clicar, você será guiado para autorizar a criação de um repositório no seu GitHub com os arquivos do Digital Garden. Dê um nome apropriado (ex: `meu-digital-garden`).
    
4. **Configure a publicação no provedor:** Siga os passos no Netlify/Vercel para criar o site: escolha o repositório recém-criado e confirme as configurações padrão de build. O template já vem configurado com um gerador estático (Eleventy/11ty) para transformar suas notas em HTML.
    
5. **Conclua o deploy:** Ao finalizar, o Netlify/Vercel vai construir o site e disponibilizar uma URL pública temporária (por exemplo, `meu-digital-garden.netlify.app`). Guarde essa URL – é onde seu garden aparecerá online. _(Você poderá configurar um domínio personalizado depois, caso deseje.)_
    

> **Dica:** Após esse passo, você já terá um repositório GitHub conectado ao seu site. É recomendável tornar esse repositório **privado** (nas configurações do GitHub, em _Settings → Danger Zone → Change visibility_), para que suas notas não fiquem públicas no GitHub. O site continuará funcionando normalmente com repositório privado.

### 1.4 Gerando um GitHub Access Token (fine-grained)

Para que o Obsidian envie suas notas para o GitHub automaticamente, precisamos de um **token de acesso do GitHub**:

1. **Crie um token no GitHub:** Logado em sua conta, acesse **Settings (Configurações) → Developer Settings → Personal Access Tokens**. Escolha a opção de criar um token. Prefira criar um **Fine-grained Token** (token de acesso _granular_) para maior segurança.
    
2. **Defina permissões mínimas necessárias:** Selecione apenas o repositório do seu Digital Garden e conceda a ele permissões de **leitura e escrita em Contents** (conteúdo) e **leitura e escrita em Pull Requests**. Essas permissões são suficientes para o plugin conseguir criar/atualizar arquivos e, se necessário, abrir _pull requests_ no repositório.
    
3. **Sem data de expiração (opcional):** Você pode definir o token sem expirar (_No expiration_) para não precisar gerar novamente no futuro. (Lembre-se: tokens _fine-grained_ podem ter validade limitada, então anote se precisar regenerar depois de expirar).
    
4. **Gerar token:** Clique em **Generate Token** e **copie o token** exibido **uma única vez** na tela. Salve-o em local seguro (caso você perca, será preciso gerar um novo).
    

### 1.5 Configuração do plugin no Obsidian

Com o token em mãos, vamos configurar o plugin Digital Garden dentro do Obsidian para que ele se conecte ao GitHub:

1. **Abra as configurações do Obsidian** e vá até **Plugins da comunidade → Digital Garden**. Você verá os campos de configuração do plugin.
    
2. **Preencha as credenciais:** Informe seu **nome de usuário do GitHub** e o **nome do repositório** que você criou (exatamente como está no GitHub). Em seguida, cole o **token de acesso** no campo apropriado.
    
3. **Teste a conexão:** Ao inserir os dados, o plugin tentará se conectar. Verifique se aparece um indicador de sucesso (por exemplo, um ícone de check ✅ indicando que o token e repositório foram aceitos).
    
4. **Ajustes adicionais:** Certifique-se de que a **URL base** do seu site está correta nas configurações (deve ser preenchida automaticamente com a URL do deploy, mas você pode editar se necessário). Ex: `https://meu-digital-garden.netlify.app`. Isso garante que os links gerados pelo plugin apontem para o seu site.
    

Agora o Obsidian está pronto para publicar suas notas diretamente no site do Digital Garden!

### 1.6 Criando e publicando a primeira nota (`dg-publish` e `dg-home`)

Vamos criar sua **primeira nota publicada** no garden, que também será usada como página inicial:

1. **Crie uma nova nota no Obsidian** (por exemplo, chamada "Home" ou "Bem-vindo"). Escreva algum conteúdo de teste nessa nota – pode ser uma breve apresentação do seu jardim digital.
    
2. **Adicione propriedades de publicação na nota:** No topo do arquivo, precisamos incluir propriedades em formato YAML (entre `---` no início) ou usar a interface de propriedades do Obsidian. As duas propriedades essenciais são:
    
    - `dg-publish: true` – indica que a nota deve ser **publicada** no site.
        
    - `dg-home: true` – indica que esta nota será a **página inicial (Home)** do garden. _(Apenas **uma** nota do vault deve ter `dg-home: true`.)_
        
    
    Você pode adicionar essas propriedades de duas formas:  
    a) **Via editor YAML:** Digite manualmente o bloco no início da nota:
    
    yaml
    
    CopiarEditar
    
    `--- dg-publish: true dg-home: true ---`
    
    b) **Via Propriedades do Obsidian:** Clique no ícone de propriedades do arquivo (ou use `Ctrl+;`) e adicione novas propriedades com os nomes acima e marque os valores como verdadeiro (checkbox ativado).
    
3. **Publique a nota:** Abra a **Paleta de Comandos** do Obsidian (`Ctrl+P` no Windows/Linux, ou `Cmd+P` no macOS) e procure pelo comando **"Digital Garden: Publish Single Note"**. Selecione-o enquanto a sua nova nota está aberta. O plugin então enviará esta nota para o repositório GitHub e disparará o processo de build do site.
    
4. **Verifique o site:** Acesse a URL do seu garden (aquela fornecida pelo Netlify/Vercel). Pode levar alguns instantes (geralmente menos de um minuto) para a mudança aparecer. Atualize a página e você deverá ver o conteúdo da sua nota publicado. 🎉
    

Parabéns! Você configurou com sucesso o ambiente e publicou sua primeira nota no Digital Garden. A seguir, veremos como gerenciar publicações de outras notas e organizar seu conteúdo.

## 🚀 2. Publicação e Gerenciamento de Notas

Após a configuração inicial, é importante entender **como publicar novas notas, gerenciar atualizações e controlar o que está ou não no site**. Esta seção explica o fluxo de publicação e as ferramentas disponíveis para gerenciar seu jardim digital.

_Fluxo de publicação do Digital Garden:_ o diagrama acima ilustra como suas notas saem do Obsidian e chegam ao site. Quando você publica uma nota, o plugin envia o arquivo Markdown para seu repositório no **GitHub**, geralmente através de um commit automático. O provedor de hospedagem (**Netlify** ou **Vercel**) detecta a mudança no repositório e inicia a reconstrução do site estático (usando o gerador Eleventy). Em poucos instantes, a versão atualizada do site é disponibilizada na URL pública do seu garden. Esse processo automatizado permite que você publique novas notas ou edite existentes com rapidez, simplesmente marcando-as com a propriedade adequada e acionando o comando de publicação.

### 2.1 Publicando uma nota manualmente

Para publicar qualquer nota adicional no seu garden, siga passos similares ao da primeira nota:

1. **Marque a nota para publicação:** Abra a nota desejada no Obsidian e adicione (via YAML ou propriedades) `dg-publish: true` no início. Você também pode usar o comando **"Digital Garden: Add Publish Flag"**, que insere essa propriedade automaticamente na nota ativa.
    
2. **Execute o comando de publicação:** Com a nota aberta, use **"Digital Garden: Publish Single Note"** na paleta de comandos. Alternativamente, o plugin oferece o comando **"Publish Multiple Notes"**, que publica _todas_ as notas do vault marcadas com `dg-publish: true` de uma vez – útil se você marcou várias notas e quer enviá-las em lote.
    
3. **Acompanhe o progresso:** Ao publicar, o status aparece normalmente na barra inferior direita do Obsidian (por exemplo, mostrando upload de arquivos ou completado). Assim que terminar, o plugin terá enviado as mudanças para o GitHub.
    
4. **Confira no site:** Acesse seu site no navegador e atualize. As novas notas publicadas já devem aparecer. Se houver um atraso, aguarde meio minuto e tente novamente, pois o build no Netlify/Vercel pode ainda estar em andamento.
    

_Observação:_ O comando **"Quick Publish and Share"** do plugin pode agilizar o processo – ele marca a nota com `dg-publish`, publica e já copia a URL da nota publicada para sua área de transferência, tudo em um passo.

### 2.2 Publicando notas interligadas (backlinks)

Uma das vantagens de um Digital Garden é a **conexão entre notas através de links internos**. Veja como proceder quando suas notas têm links umas para as outras:

- **Links internos no Obsidian:** Você pode criar links normalmente usando `[[Nome da Nota]]`. Se a nota de destino ainda não existe, crie-a e escreva seu conteúdo.
    
- **Publicar notas linkadas:** Certifique-se de **publicar também todas as notas referenciadas** via links, adicionando `dg-publish: true` nelas. Por exemplo, se a Nota A possui um link para Nota B, marque a Nota B para publicação também.
    
- **Backlinks automáticos:** O template do Digital Garden exibirá, em cada página do site, os _backlinks_ (referências de outras notas). Assim, se A linka B e ambos estão publicados, na página da Nota B o usuário verá um link de volta para A na seção de referências. Isso incentiva navegação fluida entre suas ideias.
    
- **Publicação incremental:** Você não precisa publicar tudo de uma vez. Pode ir marcando e publicando conforme escreve novas notas. Apenas lembre que, para evitar links quebrados no site, toda nota linkada deve estar publicada ou o link aparecerá sem destino. (Dica: use o **Publication Center** do plugin para ver quais notas estão publicadas ou pendentes, conforme explicado adiante.)
    

### 2.3 Despublicando uma nota

Pode acontecer de você querer **remover** uma nota do site (por exemplo, um rascunho que não faz mais sentido ficar público). Para despublicar uma nota:

1. **Remova a flag de publicação:** Abra a nota no Obsidian e remova ou desative `dg-publish` (se estiver via YAML, apague ou coloque `false`; se via propriedades, desmarque a checkbox).
    
2. **Atualize o site:** Há duas formas de efetivar a remoção:
    
    - Abra o **Publication Center** (pelo comando **"Open Publication Center"**). Nele, você verá uma lista de arquivos publicados, alterados e não publicados. Encontre a nota que você desmarcou e clique em **"Delete from garden"** (ou equivalente) para removê-la do site.
        
    - _Ou_, use novamente o comando **"Publish Multiple Notes"**: ele irá sincronizar o estado de todas as notas. Como aquela nota não tem mais `dg-publish`, o sistema irá deletá-la do site no próximo deploy.
        
3. **Verifique no site:** Após o processo, acesse o site e confirme que a nota não aparece mais (ela deve retornar um erro 404 ou desaparecer de listas de conteúdos). Os links que apontavam para ela em outras páginas podem permanecer, mas agora serão links quebrados – então remova ou ajuste quaisquer referências se necessário.
    

> **Nota:** Remover uma nota publicada do site não apaga o arquivo do seu vault ou do GitHub; apenas deixa de incluí-lo na geração do site. Você sempre pode voltar a publicá-lo marcando `dg-publish: true` de novo.

### 2.4 Acessando o site e acompanhando o deploy

- **URL do site:** Sempre que quiser visitar seu Digital Garden, use a URL fornecida pelo Netlify/Vercel. Você pode encontrá-la no dashboard do serviço (geralmente é algo como `https://seu-garden.vercel.app` ou `https://seu-garden.netlify.app`). Recomenda-se fixar essa URL em seus favoritos.
    
- **Comportamento do deploy:** Toda vez que você publica ou modifica notas, o Netlify/Vercel faz automaticamente um _deploy_ (implantação) do site. Nos painéis desses serviços, é possível acompanhar logs de build em tempo real caso precise depurar problemas. Porém, para a maioria das atualizações, basta esperar alguns segundos e recarregar a página.
    
- **Atualização de conteúdo:** O site é estático, então não atualiza conteúdo em tempo real sem novo deploy. Sempre que editar uma nota publicada, rode o comando de **Publicar** novamente para enviar as alterações. O fluxo (Obsidian → GitHub → build → site) se repetirá.
    
- **Publication Center:** Utilize a interface do Publication Center do plugin (disponível nas configurações do plugin ou via comando) para uma visão geral do estado do garden. Ele lista: notas publicadas, notas com alterações não publicadas (precisando republish), notas recém removidas, e notas que nunca foram publicadas. É uma forma prática de gerenciar em larga escala, permitindo, por exemplo, publicar todas de uma vez, ou remover várias de uma vez, etc.
    

## 🗒️ 3. Propriedades Especiais das Notas

As **propriedades YAML (metadados)** no topo de cada nota são a chave para controlar o comportamento do seu Digital Garden. Já usamos `dg-publish` e `dg-home`, mas o plugin oferece outras propriedades úteis para customizar cada página. Abaixo estão as principais propriedades especiais e suas funções:

- **`dg-publish`**: Marca a nota para publicação. Deve ser `true` em todas as notas que você deseja **expor no site**. Sem essa propriedade (ou se `false`), a nota permanece privada (não é exportada no garden).
    
- **`dg-home`**: Indica a nota que será a **página inicial (Home)** do garden. Apenas **uma** nota publicada deve ter `dg-home: true`. Normalmente usada na sua nota de introdução ou índice principal.
    
- **`aliases`**: Lista de nomes alternativos para a nota. Útil se a nota tiver outros títulos pelos quais possa ser referenciada. No site, os aliases permitem que links internos funcionem mesmo com nomes diferentes e também podem aparecer como títulos secundários. Formato: `aliases: ["Nome Alternativo 1", "Nome 2"]`.
    
- **`tags`**: Palavras-chave ou categorias associadas à nota (no Obsidian, definidas com `#exemplo`). No YAML, você pode listar tags em `tags: [tag1, tag2]`. As tags ajudam a agrupar conteúdos relacionados; no site, as tags de uma nota são exibidas e podem ser usadas para navegar por tópicos (clicar em uma tag mostra todas as notas com aquela tag, em uma página de índice automática).
    
- **`dg-pinned`**: Quando `true`, fixa a nota no topo da lista de notas dentro da pasta (no menu de navegação do site). Use isso para destacar notas importantes em meio às outras. Por exemplo, você pode "pinmar" um arquivo README dentro de uma categoria para que ele apareça primeiro.
    
- **`dg-note-icon`**: Define um ícone para representar a nota. O plugin suporta ícones personalizados para notas – por padrão há 4 opções internas (icones padrão numerados de 1 a 3, além de "default"). Você pode definir `dg-note-icon: 1` (ou 2, 3) para usar esses ícones predefinidos, ou configurar ícones próprios (embora isso exija passos avançados de adicionar SVGs ao template e ajustar CSS). Os ícones de nota aparecem ao lado do título da nota no site, no índice e em links internos, dando um toque visual ao seu garden (por exemplo, usar um ícone de 📌 para notas fixas, etc.).
    

Além dessas, existem outras propriedades avançadas para personalizações específicas, como `dg-hide` (para ocultar a nota do índice do site), `dg-hide-in-graph` (ocultar a nota do grafo de conexões), `dg-enable-backlink`/`dg-enable-search` (habilitar ou desabilitar backlinks e busca para aquela nota individualmente), `dg-metatags` (definir meta tags de SEO/Graph para compartilhamento em redes sociais), entre outras. Essas configurações adicionais podem ser consultadas na documentação oficial, mas as citadas acima são as mais utilizadas no dia a dia.

**Exemplo de bloco YAML completo em uma nota publicada:** suponha que queremos publicar uma nota chamada "Projetos 2025" que não é home, mas que tenha um alias, tags, ícone e esteja fixada no topo de sua pasta:

yaml

CopiarEditar

`--- dg-publish: true dg-home: false            # (por padrão, pode ser omitido se false) dg-pinned: true dg-note-icon: "2" aliases: ["Projetos Futuros", "Projects 2025"] tags: [planning, projetos, 2025] ---`

No exemplo acima, a nota será publicada (`dg-publish`), não é a home, ficará fixada (`dg-pinned`) no topo do menu daquela pasta, usará o ícone "2" fornecido pelo tema do plugin, poderá ser encontrada também pelos nomes "Projetos Futuros" ou "Projects 2025" (aliases), e estará categorizada sob as tags "planning", "projetos" e "2025". Ajuste as propriedades conforme suas necessidades. Lembre-se de **aplicar essas propriedades antes de publicar** a nota para que tenham efeito no site.

## 🎨 4. Personalização Visual e Temática

Uma vez que seu garden está funcionando, você vai querer deixá-lo com a sua cara. O plugin Digital Garden permite várias **personalizações visuais e de tema** sem precisar mexer diretamente no código do site (embora isso também seja possível para usuários avançados). Nesta seção, veremos como alterar o tema, adicionar CSS personalizado, criar templates de notas e ajustar a identidade visual geral do seu jardim digital.

### 4.1 Escolha de tema e aparência

- **Temas do Obsidian no site:** O plugin suporta o uso de **temas da comunidade do Obsidian** em seu site. Ou seja, você pode aplicar no garden o mesmo tema que usa no Obsidian, ou qualquer outro de sua preferência. Para isso, vá em **Configurações → Digital Garden → Appearance (Aparência)**. Lá você encontrará uma lista suspensa **"Theme"**. Selecione um dos temas disponíveis (a maioria dos temas populares do Obsidian está suportada).
    
- **Modo claro/escuro:** Após escolher um tema, você pode definir se o site deve usar a versão **Dark** (escura) ou **Light** (clara) desse tema. Muitos temas têm suporte a ambos; se o tema escolhido não suportar o modo selecionado, o plugin avisará.
    
- **Aplicar o tema:** Clique no botão **"Apply settings to site"** (Aplicar configurações ao site) para enviar essas alterações. Isso irá gerar um novo deploy apenas com a mudança de estilo. Ao recarregar seu site, o visual deverá estar atualizado conforme o tema escolhido.
    
- **Nome do site:** Ainda nas configurações de aparência, defina o **"Site name (Nome do site)"**. Por padrão pode estar algo como "Digital Garden". Mude para o título que deseja ver no topo da página (por exemplo, o seu nome ou o nome do seu garden). Esse nome aparecerá na barra de navegação superior do site. Lembre de clicar **Apply** após alterá-lo.
    
- **Favicon:** Você pode personalizar o favicon (ícone que aparece na aba do navegador). Prepare um arquivo de imagem em formato **SVG** para o ícone (o template só aceita SVGs). Coloque esse arquivo em alguma pasta do seu vault e, na configuração **"Favicon"**, insira o caminho para o arquivo (ex: `Pasta/Icones/meufavicon.svg`). Aplique as configurações e, quando o site atualizar, seu ícone personalizado será exibido na aba do browser. _(Dica: se o favicon não mudar de imediato, limpe o cache do navegador.)_
    

### 4.2 Estilos CSS personalizados

Para ajustes finos de design ou caso queira alterar algo específico do tema:

- **CSS Snippets:** Você pode utilizar **CSS customizado** para estilizar elementos. Crie um arquivo `.css` no seu vault com as regras desejadas (por exemplo, alterar cores de fundo, fontes, tamanhos, etc). Em seguida, integre esse CSS ao site. Há algumas formas:
    
    - **Via plugin Style Settings:** Se você usa o plugin "Style Settings" no Obsidian para customizar temas, o Digital Garden consegue aplicar essas configurações. Nas configurações de aparência do Digital Garden, haverá uma seção **"Style Settings"** com um botão _Apply_. Isso incorporará as preferências de estilo que você configurou (por exemplo, fonte personalizada, espaçamento) ao site.
        
    - **Via arquivo CSS no template:** Para total liberdade, edite o repositório do seu site no GitHub: há uma pasta (por exemplo `src/styles/`) onde você pode colocar seu CSS. Alternativamente, o plugin oferece uma chave frontmatter `dg-content-classes` para adicionar classes CSS por nota, e então no seu arquivo CSS você estiliza essas classes específicas. Esse nível de customização exige conhecer CSS/HTML, mas permite modificar praticamente qualquer aspecto visual.
        
- **Mudando componentes HTML:** Usuários com conhecimento web podem alterar layout adicionando componentes customizados. O template do garden possui _slots_ onde você pode injetar HTML/JS – por exemplo, inserir um bloco no rodapé da página, ou um widget. Essas modificações avançadas estão além do escopo deste guia, mas vale saber que são possíveis editando arquivos do template (como `userSetup.js` ou criando partials do Eleventy). Sempre faça backup antes de experimentar customizações profundas.
    

Para a maioria dos casos, escolher um bom tema e eventualmente adicionar pequenos trechos de CSS já é suficiente para deixar o garden com personalidade única.

### 4.3 Modelo de nota publicável (template)

Conforme você for criando muitas notas, é útil ter um **template padrão** com a estrutura básica já pronta, facilitando marcar notas para publicação sem esquecer campos importantes:

- **Crie um template de garden:** No seu vault, habilite o plugin interno **Templates (Modelos)** do Obsidian. Crie uma nova nota em sua pasta de templates chamada, por exemplo, "_Template Digital Garden". Nessa nota, coloque um frontmatter YAML com os campos que normalmente você usará. Por exemplo:
    
    yaml
    
    CopiarEditar
    
    `--- dg-publish: true dg-home: false tags: [] aliases: [] ---`
    
    E talvez um esqueleto de conteúdo, como um título (`# Título da Nota`) para lembrar de inserir um título visível (especialmente útil para notas home, cujo título de arquivo não aparece por padrão no site).
    
- **Use o template nas novas notas:** Sempre que for criar uma nova nota que será publicada, aplique esse modelo (usando o comando de inserir template). Assim, ela já virá com `dg-publish: true` e você só preenche tags, aliases, etc. Isso padroniza suas publicações e economiza tempo.
    
- **Variações de template:** Você pode ter mais de um template – por exemplo, um para notas normais e outro para a página home (com `dg-home: true` e talvez layout diferente). Outra ideia: um template para "coleções" ou "projetos" que inclua uma seção de índice. Personalize conforme seu fluxo de trabalho.
    

### 4.4 Identidade visual do garden

Algumas dicas finais para personalizar a identidade do seu Digital Garden:

- **Texto de boas-vindas:** Como a página inicial é a porta de entrada, capriche no conteúdo dela. Você pode incluir uma breve explicação sobre o que as pessoas encontram no seu garden, talvez uma foto ou imagem de capa (basta inserir imagem via Markdown `![](link)` no conteúdo da nota; o plugin publicará imagens referenciadas).
    
- **Navegação e estrutura:** Por padrão, o site exibirá um menu lateral/superior com a estrutura de pastas e notas publicadas. Pense em como quer organizar suas notas publicadas – às vezes faz sentido ter uma pasta específica para "Blog" ou "Diário" e outra para "Notas permanentes", etc., de modo que no site fiquem separadas. Os nomes de pastas também aparecem, então nomeie-as de forma amigável. Você pode esconder certas pastas ou notas do menu usando `dg-hide` se forem meramente técnicas.
    
- **Elementos visuais:** Considere adicionar alguns _toques pessoais_: ícones de notas (como vimos com `dg-note-icon`), emojis nos títulos ou no texto (muitos gardens usam emojis para dar um ar descontraído), e cores que combinem com seu estilo. Se seu tema não destaca links internos, talvez use CSS personalizado para sublinhá-los ou colorir tags.
    
- **Funcionalidades extras:** O Digital Garden plugin tem recursos opcionais como **busca interna** e **grafo local** (visualização dos links entre notas tipo "graph view"). Você pode habilitar ou desabilitar essas funções globalmente ou por nota nas configurações. Por exemplo, habilitar a busca adiciona uma barra de pesquisa no site, permitindo visitantes encontrarem notas por texto. Verifique em **Configurações → Digital Garden → Note Settings** quais features deseja ativar (Backlinks, Graph, Search, Comments, etc.) e aplique ao site. Isso também compõe a "identidade" do seu garden em termos de interatividade.
    

Ao personalizar o visual e a identidade, o objetivo é que seu Digital Garden reflita sua personalidade e seja agradável de navegar. Pequenos ajustes contínuos podem ser feitos – um jardim digital está em constante evolução, tanto em conteúdo quanto em aparência. 🌱

## 🗂️ 5. Indexação Inteligente com Dataview e MOCs

Conforme seu jardim digital cresce, é importante manter a **organização interna** para você e oferecer **navegação intuitiva** para os leitores. Ferramentas como o plugin **Dataview** e as **MOCs (Map of Content ou Notas de Estrutura)** ajudam a criar índices dinâmicos e mapas de conteúdos.

### 5.1 Plugin Dataview: criando índices dinâmicos

O Dataview é um popular plugin do Obsidian que permite **consultas sobre suas notas** (como um banco de dados do seu vault). A boa notícia é que o **Digital Garden suporta publicar os resultados do Dataview** no site:

- **Instale e atualize o Dataview:** Certifique-se de ter o plugin Dataview instalado e atualizado (versão 0.5.39 ou superior) no Obsidian. Mesmo que as consultas rodem na geração do site, elas dependem do Dataview no Obsidian para interpretar.
    
- **Crie uma consulta Dataview:** Em uma nota do seu vault (que será publicada), insira um bloco de código Dataview. Por exemplo, para listar todas as notas publicadas marcadas com a tag `projeto`:
    
    markdown
    
    CopiarEditar
    
    `` ```dataview   LIST FROM #projeto   WHERE dg-publish = true   SORT file.name   \`\`\` ``  
    
    _Explicação:_ Esse snippet irá gerar uma lista (`LIST`) de notas que possuam a tag `#projeto` e que estejam publicadas (`dg-publish = true`), ordenadas pelo nome do arquivo. Você pode ajustar a consulta conforme suas necessidades – Dataview permite filtrar por nome, conteúdo, data, etc.
    
- **Publique a nota de índice:** Marque essa nota (por exemplo "Index de Projetos") com `dg-publish: true` e publique-a. O plugin Digital Garden irá **executar a consulta Dataview no momento do build** e “congelar” o resultado como parte do HTML. Ou seja, a página publicada mostrará a lista atualizada naquele momento. Se você adicionar mais notas que atendam ao critério futuramente, precisará republicar a nota de índice para atualizar a lista.
    
- **Verifique o resultado no site:** Acesse a página publicada e confirme se a listagem aparece como esperado, com links clicáveis para as notas correspondentes. O plugin trata esses links como conteúdo real, então inclusive aparecerão como backlinks nas notas listadas.
    

O Dataview suporta não só listas, mas também **tabelas** e **queries JavaScript (dataviewjs)** para formatações mais avançadas. Por exemplo, você pode criar uma tabela com colunas de título, data de criação, tags, etc., ou até um calendário de publicações. Tudo isso pode ser publicado no garden. Utilize o Dataview para construir páginas especiais como um **arquivo** (lista cronológica de todas as notas publicadas), uma **galeria por tags**, etc.

### 5.2 Listas automáticas por tag ou data

Além do Dataview, você pode também criar manualmente ou semi-automaticamente páginas de índice:

- **Index por tags:** Considere criar notas de índice para suas principais tags/tópicos. Ex: uma nota "📂 Projetos" que lista todos os projetos. Você pode preencher manualmente ou usar Dataview conforme descrito. Outra abordagem é usar links diretos: escreva na nota algo como: "Notas relacionadas: [[Projeto Alpha]], [[Projeto Beta]], ..." listando manualmente as notas daquele tema. Isso funciona, mas dá mais trabalho para manter atualizado. O Dataview facilita ao puxar automaticamente todas que têm a tag.
    
- **Index por data:** Se você usa seu garden como um blog ou diário, pode fazer uma página "Arquivo" listando notas por ordem cronológica. Exemplo com Dataview:
    
    dataview
    
    CopiarEditar
    
    `TABLE file.day as Data, file.link as Nota   WHERE dg-publish = true   SORT file.day DESC`  
    
    Isso exibiria uma tabela de notas publicadas com a data (se houver no nome ou metadado) e o link. Ou use `SORT file.mtime` para ordenar por data de modificação.
    
- **Dashboard ou Home dinâmica:** Sua própria homepage do garden pode conter seções dinâmicas. Por exemplo: "Últimas atualizações" (lista das 5 notas mais recentemente modificadas), "Categorias principais" (lista de links para índices de tags). Com combinações de Dataview e alguns links fixos, você transforma a home numa central de navegação.
    
- **Atualização das listas:** Lembre-se sempre de republicar a nota de índice quando houver mudanças relevantes (o plugin não sabe automaticamente quando o resultado do Dataview mudou, a não ser que você modifique algo na nota de índice em si). Uma estratégia é, sempre que publicar uma nova nota, abrir a(s) nota(s) de índice relacionadas, verificar se precisa atualizar (geralmente o próprio republish já atualiza) e rodar o comando Publish de novo nelas também. Isso garante que os índices não fiquem desatualizados.
    

### 5.3 MOCs e transclusões de conteúdo

**MOC (Map of Content)** ou **Notas de Estrutura** são notas cuja função é organizar links de um conjunto de notas relacionadas, servindo como um "mapa" para navegar entre elas. No contexto do Digital Garden:

- **Criação de MOCs:** Escolha um tema ou área do seu conhecimento que tenha várias notas. Crie uma nota "Mapa de [Tema]" (por ex: "🌲 Mapa de Ecologia"). Dentro dela, escreva uma estrutura hierárquica ou uma narrativa breve e insira links para as notas relevantes. Agrupe por subtema se necessário. Essa nota MOC não necessariamente precisa ter muito conteúdo próprio – é mais um índice comentado.
    
- **Uso de transclusões (`![[...]]`):** Você pode enriquecer um MOC com _transclusões_ de conteúdo de outras notas. Ao invés de apenas listar o link, usar `![[Nota X]]` embute o conteúdo completo da "Nota X" dentro do MOC. Isso pode ser útil para, por exemplo, mostrar um parágrafo resumo de cada nota diretamente no mapa. Outra opção é usar transclusão de blocos específicos: se dentro de suas notas você marcar um parágrafo como ^resumo (com um identificador de bloco), pode chamar `![[Nota X^resumo]]` no MOC para trazer apenas aquele resumo. Assim, o leitor vê um overview de cada item sem precisar clicar em todos.
    
- **Navegabilidade do MOC:** Uma vez publicado, o MOC serve como uma página central. Certifique-se de publicar todas as notas linkadas/transcluídas para que apareçam no site. A MOC em si também deve ter `dg-publish: true` (e possivelmente `dg-pinned: true` se quiser destacá-la). O uso de headings e listas no MOC dá estrutura visual – utilize títulos de nível 2/3 para separar seções, e bullet points para listas de notas semelhantes.
    
- **Combinar MOC e Dataview:** Uma abordagem híbrida potente é mesclar conteúdo manual com consultas automáticas. Ex: em um MOC de "Artigos por Ano", você pode escrever manualmente os anos como seções (2023, 2022, 2021...) e abaixo de cada um inserir uma query Dataview que liste notas daquele ano. Assim, a estrutura é fixa, mas o preenchimento é automático.
    

Ao usar essas técnicas, seu Digital Garden se torna mais **descobrível** – tanto para visitantes navegarem por temas e verem relações entre notas, quanto para você mesmo encontrar padrões e conectar ideias. A indexação inteligente mantém o jardim coeso conforme ele expande.

## 🤖 6. Automação e Organização

Manter um fluxo de trabalho organizado é crucial para que seu Digital Garden cresça sem virar um caos. Felizmente, podemos automatizar parte da organização dentro do Obsidian usando plugins auxiliares e boas práticas. Vamos abordar o plugin **Auto Note Mover**, a ideia de **Inbox inteligente** e sugestões de **estrutura de pastas**.

### 6.1 Auto Note Mover: movendo notas por regras

O plugin Auto Note Mover permite criar regras que **movem notas automaticamente** para determinadas pastas com base em critérios (por exemplo, tags ou padrões no título). Isso é útil para classificar notas assim que elas são criadas ou marcadas:

- **Instalação:** Instale e habilite o Auto Note Mover pela aba de Plugins da comunidade do Obsidian.
    
- **Definir regras:** Nas configurações do plugin, você poderá adicionar "Rules". Cada regra tipicamente define: uma condição (como "tag contém #inbox" ou "nome começa com 'Projeto - '") e uma ação de mover para uma pasta destino.
    
- **Exemplo de regras:**
    
    - _Regra 1: Mover da Inbox para Publicáveis_ – Se a nota for marcada com a tag `#publicar` (ou tiver `dg-publish: true`), mover a nota para a pasta "Publicadas" do vault. Isso mantém todas as notas que estarão no site reunidas.
        
    - _Regra 2: Organizar por assunto_ – Se uma nota recebe a tag `#tema/filosofia`, mover para `Notas/Filosofia/`. Você pode criar várias regras semelhantes para diferentes temas ou projetos.
        
    - _Regra 3: Manter Inbox limpa_ – Qualquer nota que **não** tenha a tag `#inbox` (ou seja, foi processada) é movida para fora da pasta Inbox para um repositório geral ou arquivo adequado.
        
- **Funcionamento:** O plugin monitora as notas em tempo real. Assim que uma nota atende a uma regra, ele a desloca automaticamente. Por exemplo, você termina de editar uma nova nota e adiciona a tag `#publicar`; instantaneamente o arquivo é movido para "Digital Garden/Publicadas/". Isso elimina a etapa manual de arrastar arquivos.
    
- **Cuidados:** Ordene as regras de forma lógica, pois se duas regras puderem se aplicar à mesma nota, a ordem decidirá. Você pode especificar exceções (pastas a serem ignoradas) para evitar loops – por exemplo, não mover notas já na pasta destino. Felizmente, o plugin permite marcar uma pasta como "excluída" das regras para evitar movimentações indesejadas.
    

Com o Auto Note Mover, sua organização fica **proativa**: à medida que você classifica uma nota com tags ou propriedades, ela vai para o lugar certo sem esforço.

### 6.2 Inbox inteligente (inboxing) e organização automática

Uma prática comum em sistemas de notas (inspirada em GTD e Zettelkasten) é usar uma **Inbox (caixa de entrada)** para notas novas ou não processadas, e depois esvaziá-la regularmente. Podemos potencializar isso no Obsidian:

- **Pasta Inbox:** Crie uma pasta chamada, por exemplo, `📥 Inbox` no seu vault. Configure o Obsidian (Configurações → Arquivos & Links → Local padrão para novas notas) para colocar novas notas nessa pasta. Assim, tudo que você captura rapidamente (via mobile, snippet, etc.) vai para Inbox.
    
- **Processamento:** Reserve momentos para processar a Inbox. Abrir cada nota, decidir o que fazer: se é uma ideia que vira nota permanente, se vira uma tarefa, se deve ser publicada, etc. Durante o processamento, atribua tags ou propriedades adequadas.
    
- **Regras de movimentação:** Com o Auto Note Mover ativo, assim que você adicionar certos marcadores, a nota “sai” da Inbox sozinha. Por exemplo: você abre uma nota na Inbox, vê que é uma nota digna de ir pro garden – você marca `dg-publish: true` e talvez adiciona uma tag de tema; ao fechar, a regra do plugin move para `Publicadas/` ou `📂 Digital Garden`. Pronto, Inbox esvaziada daquela nota. Outra nota talvez receba tag `#to-do` e o Auto Note Mover leva para uma pasta de tarefas.
    
- **Indexação automática:** O wanderloots (criador do blog _Wanderloots.xyz_) sugere um fluxo onde as tags não só movem as notas, mas também alimentam índices. Por exemplo, toda nota com tag `#topic/filosofia` vai para pasta Filosofia e, no site, uma página "Filosofia" usa Dataview para listar tudo daquela pasta ou tag. Assim, a simples ação de **taggear** uma nota coloca ela no lugar certo e garante que ela apareça automaticamente no índice correspondente do site. Essa é uma forma de "indexação viva".
    
- **Benefícios:** Esse sistema de inbox inteligente garante que nada se perca. Notas novas sempre chegam num ponto central (Inbox), e de lá são triadas para onde devem ir. Reduz-se a chance de esquecer de publicar algo (pois se for publicável, a tag cuida disso) ou de ter notas soltas sem contexto. Também ajuda a separar o estágio de **captura** do estágio de **organização** – você não precisa decidir na hora da escrita onde a nota ficará, apenas joga na Inbox e mais tarde, com calma, categoriza.
    

### 6.3 Estrutura de pastas recomendada

Não há uma única forma de organizar um vault, mas para um Digital Garden alguns padrões funcionam bem:

- **Separe o público do privado:** Considere ter uma pasta dedicada às notas que serão publicadas, por exemplo `Digital Garden` ou `