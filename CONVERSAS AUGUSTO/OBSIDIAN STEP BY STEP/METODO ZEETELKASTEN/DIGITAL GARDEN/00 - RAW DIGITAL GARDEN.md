---
created: 2025-04-14T03:33
updated: 2025-04-14T04:37
---
Here is a step-by-step guide to setting up your digital garden, drawing from the provided sources:

**Phase 1: Prerequisites**

1. **Download and install Obsidian** if you haven't already.
2. You will need a **GitHub account**. If you don't have one, create one.
3. You'll also need an account with a hosting service. The sources mention **Vercel** and **Netlify**. The video tutorial and the written tutorial primarily use Netlify and highlight its free tier and free encryption. You can sign up for Netlify using your GitHub account.

**Phase 2: Building the Publishing Flow**

1. **Install the Digital Garden plugin in Obsidian.** Go to **Settings**, then **Community plugins**, and search for "Digital Garden". Install and enable it.
2. **Open the Digital Garden repository** linked in the "01 Getting started" guide. Click the blue **"Deploy to Vercel" button**. Alternatively, for Netlify, follow the "Hosting Alternatives" guide within the Digital Garden plugin documentation and click the **"deploy to nly" button**. This will create a copy of the repository in your GitHub account. Give it a suitable name, like 'my-digital-garden'.
3. **Follow the steps on Vercel or Netlify** to publish your site to the internet. Netlify will automatically create a repository on your GitHub. Your site's URL will be provided by Vercel or Netlify.
4. **Create an access token for your GitHub account.** This allows the Digital Garden plugin to add new notes to your GitHub repository. Go to the specified GitHub page while logged in.
    - For more security, consider using a **fine-grained access token** that only has access to your digital garden repository. The recommended permissions for a fine-grained token are **read & write** access to **contents** and **pull requests**.
    - You can choose "No expiration" for a classic token if you don't want to regenerate it frequently. Remember to regenerate fine-grained tokens after their expiration date.
    - Click "Generate token" and **copy the token** presented on the next page. This token will only be shown once, so save it securely.
5. **Open Obsidian settings** and go to the settings for **"Digital Garden"**.
6. Fill in your **GitHub username**, the **name of the repository** you created (e.g., 'my-digital-garden'), and **paste the GitHub token**. If the authentication is successful, you should see a green checkmark.
7. **(Optional but Recommended)** For security, you can **make your GitHub repository private** after the initial deployment. Go to your GitHub repository, click on **Settings**, scroll to the **"Danger Zone"**, and change the visibility to private.

**Phase 3: Publishing Your First Note**

1. **Create a new note in Obsidian**.
2. **Add two new properties** to the note:
    - **dg-publish**: Toggle this checkbox to indicate that the note should be published.
    - **dg-home**: Toggle this checkbox to designate this note as your home page or entry point to your digital garden. **Only one note** should have this setting enabled.
    - You can add properties using the **Add file property** command, the **Cmd/Ctrl+;** hotkey, the **More actions** menu, by right-clicking the tab, or by typing `---` at the beginning of the file.
3. Open your **command palette** by pressing **CTRL+P** (Windows/Linux) or **CMD+P** (Mac).
4. Find the command **"Digital Garden: Publish Single Note"** and press Enter.
5. Go to your **site's URL** which you can find on Vercel or Netlify. It might take a minute for the changes to appear, so refresh the page. Your note should now be live.

**Next Steps and Customization**

- You can now start adding internal links to other notes using double square brackets `[[your note title]]`. Remember to also publish the notes you are linking to by adding the `dg-publish` property to them.
- To **unpublish a note**, simply uncheck or remove the `dg-publish` property and then use the "Delete notes from garden" button in the publication center.
- Explore the **available commands** and **note settings** in the Digital Garden plugin settings.
- You can **change the theme** of your digital garden in the plugin's appearance settings.
- Consider creating a **Digital Garden template** with the `dg-publish` and potentially `tags` and `aliases` properties to streamline the publishing process for future notes.
- You can set a **custom domain name** for your digital garden through your hosting provider (like Netlify) after purchasing one from a domain registrar (like NameCheap). You will need to configure the DNS settings of your domain to point to your hosting provider.
- **Enable HTTPS** for your custom domain. Netlify offers free encryption via Let's Encrypt. You may need to add CAA DNS records as shown in the video tutorial and the "How to Publish" guide.

Congratulations, you now have your own digital garden! You can continue to add and link notes, building your personal corner of the internet.


# 🪴 **Workflow Completo: Digital Garden com Obsidian**

Este fluxo descreve **como criar, configurar, publicar e gerenciar** um Digital Garden (jardim digital) utilizando **Obsidian + GitHub + Vercel/Netlify**, com foco em automação e controle granular de publicação.

---

## 🧭 1. Getting Started (Primeiros Passos)

### Objetivo:

Iniciar o projeto do Digital Garden com o mínimo necessário, criando uma base funcional e segura.

### Etapas:

#### 🔹 **Initial Setup (Minutes)**

- Instale o plugin [Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) no Obsidian.
    
- Crie uma conta no GitHub.
    
- Crie uma conta no Vercel ou Netlify.
    
- Faça o deploy do repositório para o Vercel/Netlify.
    

#### 🔹 **Control and Customization**

- Gere um GitHub Access Token (preferencialmente do tipo "Fine-grained").
    
- Configure o plugin no Obsidian com suas credenciais.
    
- Crie sua primeira nota.
    

#### 🔹 **Steps**

1. Adicione propriedades no YAML da nota:
    
    - `dg-publish: true`
        
    - `dg-home: true` (se quiser que seja a página inicial)
        
2. Publique uma nota individual usando a paleta de comandos (`Command Palette`).
    
3. Acesse o site gerado pela URL do Vercel/Netlify.
    
4. Adicione links entre notas (dentro do Obsidian).
    
5. Publique notas interligadas.
    
6. Para despublicar, remova `dg-publish`.
    

---

## 🚀 2. Publishing Flow (Fluxo de Publicação)

### Objetivo:

Entender a estrutura por trás da publicação automática.

### Componentes:

- **Obsidian Vault:** seu repositório local de notas.
    
- **Digital Garden Plugin:** integra Obsidian com seu site estático.
    
- **GitHub Repository:** armazena os arquivos e serve como backend.
    
- **Hosting Provider:** onde seu site é servido (Netlify, Vercel, GitHub Pages).
    
- **Static Site Generator (Eleventy/11ty):** transforma Markdown em HTML.
    
- **Markdown → HTML:** o conteúdo da nota é convertido e exibido no navegador.
    

---

## 🎨 3. Customization (Personalização)

### (Este bloco está apenas representado no diagrama, mas não expandido.)

Você pode customizar:

- Estilo visual (CSS)
    
- Tema do garden
    
- Componentes HTML renderizados
    
- Filtros e exibições baseadas em metadados
    

---

## 🌐 4. Hosting

### (Também um nó do fluxo principal não expandido.)

Normalmente hospedado com:

- **Netlify**: simples e gratuito
    
- **Vercel**: integração com GitHub automática
    
- **GitHub Pages**: alternativa mais técnica
    

---

## 🔗 5. GitHub Connection

### Objetivo:

Controlar a visibilidade e função de cada nota por meio de propriedades.

#### Propriedades:

- `dg-publish`: marca a nota para ser publicada.
    
- `dg-home`: define a nota como **página inicial**.
    
- `aliases`: nomes alternativos da nota.
    
- `tags`: usadas para filtrar e categorizar conteúdo.
    
- `dg-pinned`: fixa a nota no topo.
    
- `dg-note-icon`: define um ícone para a nota.
    

---

## 📄 6. Note Properties

- As propriedades YAML são a **chave de controle do sistema**.
    
- São lidas automaticamente pelo plugin para decidir:
    
    - O que publicar
        
    - Onde publicar
        
    - Como exibir a nota
        

---

## 🌍 7. Custom Domain

Você pode conectar um domínio próprio (via DNS) ao seu site no Netlify ou Vercel para ter um endereço como:

> `meujardimdigital.com`

---

## 🔄 8. Related Concepts

Este item remete a tópicos interligados no seu Zettelkasten:

- **Aliases**, **Tags**, **Links Internos**, etc.
    
- São essenciais para a **navegação semântica** dentro do garden.
    

---

## ✅ Conclusão: Visão Geral do Workflow

css

CopiarEditar

`[1] Configuração Inicial ➜ [2] Integração com GitHub/Vercel ➜ [3] Criação de Notas no Obsidian ➜ [4] Controle via Propriedades YAML ➜ [5] Publicação Manual ou em Lote ➜ [6] Visualização e Navegação Online ➜ [7] Atualizações automáticas ➜ [8] Customização contínua`

Esse sistema é ideal para:

- Criadores de conteúdo
    
- Pesquisadores
    
- Usuários de Zettelkasten
    
- Quem deseja um blog minimalista e conectado
    

---

Se quiser, posso gerar:

- ✅ Templates YAML prontos para usar
    
- ✅ Scripts de deploy automático
    
- ✅ Instruções para configurar domínio próprio
    

Quer que eu monte um pacote para isso também?


Claro, Pedro! Aqui está a **transcrição exata das palavras e frases da imagem** do **mapa mental do Digital Garden**:

---

### 🟪 **Digital Garden**

#### 🟦 Getting Started

- 🟩 Initial Setup (Minutes)
    
- 🟩 Control and Customization
    
- 🟩 Steps
    
    - Install Digital Garden Plugin (Obsidian)
        
    - GitHub Account
        
    - Vercel Account (or Netlify)
        
    - Deploy Repo to Vercel/Netlify
        
    - Create GitHub Access Token
        
    - Configure Plugin Settings
        
    - Create First Note
        
    - Add Properties (dg-publish, dg-home)
        
    - Publish Single Note (Command Palette)
        
    - View Site URL (Vercel/Netlify)
        
    - Add Links (Obsidian)
        
    - Publish Linked Notes
        
    - Unpublish Note (Remove dg-publish)
        
- 🟩 More Secure Token (Fine-grained)
    

#### 🟦 Publishing Flow

- 🟩 Obsidian Vault
    
- 🟩 Digital Garden Plugin
    
- 🟩 GitHub Repository
    
- 🟩 Hosting Provider (Netlify, Vercel, GitHub Pages)
    
- 🟩 Static Site Generation (11ty)
    
- 🟩 Markdown to HTML
    

#### 🟦 Customization

#### 🟦 Hosting

#### 🟦 GitHub Connection

- 🟩 dg-publish (Publish to Garden)
    
- 🟩 dg-home (Homepage)
    
- 🟩 Aliases
    
- 🟩 Tags
    
- 🟩 dg-pinned
    
- 🟩 dg-note-icon
    

#### 🟦 Note Properties

#### 🟦 Custom Domain

#### 🟦 Related Concepts

---

Se quiser, posso transformar isso em um documento formatado ou template de instruções para facilitar o uso com outros LLMs ou gerar em outros formatos como JSON, YAML, Markdown etc. Deseja isso?

