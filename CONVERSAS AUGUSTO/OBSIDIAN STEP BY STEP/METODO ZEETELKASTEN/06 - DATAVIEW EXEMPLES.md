---
created: 2025-04-14T03:23
updated: 2025-04-14T04:37
---
The sources highlight Dataview as a powerful plugin for Obsidian that significantly enhances the Zettelkasten method by allowing users to query their notes as if they were a database1 .... It enables the creation of dynamic lists and tables based on the metadata (YAML frontmatter and tags) and folder structure of your Obsidian vault1 ....

Here's a breakdown of what the sources say about Dataview in the context of Zettelkasten in Obsidian:

•

Core Functionality: Dataview allows you to visualize structured data within Obsidian7 . It enables you to query your notes like a database and display the results in dynamic lists or tables1 .... You can write queries in code blocks or using JavaScript for more complex cases8 . The syntax resembles SQL combined with Markdown8 .

•

Integration with Zettelkasten Principles: Dataview leverages the core principles of Zettelkasten, especially the emphasis on metadata (tags and YAML) and interconnectedness2 .... By consistently applying tags and structuring information in the frontmatter, you can use Dataview to gain dynamic overviews and manage your knowledge more effectively2 ....

•

Importance of Metadata: To effectively use Dataview, it's crucial to plan your tags and fields of frontmatter in a way that aligns with the queries you want to perform8 . Consistent use of tags and frontmatter ensures your notes are discoverable and manageable as your vault grows2 .... Hierarchical tags further enhance Dataview's capabilities, allowing you to filter notes based on broader categories and sub-tags9 .

•

Use Cases with Different Note Types: The sources provide several practical examples of how Dataview can be integrated with different Zettelkasten note types:

◦

Structure Notes (Maps of Content - MOCs): Instead of manually maintaining lists of links, you can use Dataview to automatically pull all notes with a certain theme tag into a structure note, creating an automatic Map of Content6 .... For example, in a note called "📑 Philosophy - Mapa", you could use LIST FROM #theme/filosofia AND #type/note SORT file.name to list all permanent philosophy notes6 .

◦

Permanent Notes: You can create lists of pending notes by querying for permanent notes with specific status tags like #status/draft or those containing a specific task marker6 .... An example query is TABLE file.link AS Nota, status FROM "3_Permanent" WHERE status = "draft" SORT file.mtime DESC to show draft permanent notes ordered by modification date6 .

◦

Literature Notes: Dataview can be used to create reviews of literature by listing all literature notes within a specific timeframe or those that haven't yet been transformed into permanent notes6 .... For instance, TABLE Author, link FROM #type/paper WHERE date >= 2025-01-01 could list all "paper" type notes (literature notes for papers) read in 20256 .

◦

Project Notes: You can create project dashboards by using Dataview to list subtasaks or related notes within a specific project folder6 .... For example, LIST FROM "4_Project/Meu Projeto" would list all notes within the "Meu Projeto" folder6 .

◦

Glossary: Dataview can automatically generate glossaries and indexes by pulling terms and their definitions based on properties filled in the notes8 .... The Glossary template in the Starter Kit uses Dataview to show defined terms and the number of backlinks to each term8 .

•

Role in Organization and Navigation: Dataview snippets located below Structure Notes help to navigate and organize the knowledge base with automatic queries for things like bibliographies, glossaries, and indexes7 . Structure notes and Dataview queries work together to organize and navigate through all other notes14 . Dataview allows for dynamic visualizations of your knowledge, going beyond manual lists and aiding in discovering relationships between notes1 .

•

Automation: Dataview enables automation by creating automatic maps of content and lists of pending tasks, reducing the need for manual updates1 ....

•

Templates and Starter Kit: The Zettelkasten Starter Kit by Edmund Gröpl includes some pre-written Dataview snippets in templates, such as the glossary example8 . This makes it easier for users to start leveraging Dataview in their Zettelkasten workflow8 .

•

Questions Dataview Can Answer: With a well-planned taxonomy of tags and frontmatter fields, Dataview allows you to answer questions like:

◦

"How many permanent notes have I created this month?"8

◦

"Which books (literature notes) have I not yet summarized in a permanent note?"8

◦

"Which concepts have the most connections (backlinks)?"8

In summary, Dataview is a crucial tool for implementing a modern digital Zettelkasten in Obsidian. It moves beyond static organization by allowing you to create dynamic and interconnected views of your knowledge based on the metadata you define. By leveraging Dataview, you can enhance navigation, automate organizational tasks, and gain deeper insights into the relationships within your personal knowledge base1 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Examples:, in the larger context of Dataview.

The sources provide several examples of how the Dataview plugin in Obsidian can be used within a Zettelkasten system to create dynamic visualizations and manage information1 .... Dataview allows you to query your notes as if they were a database, leveraging metadata (YAML frontmatter, tags) and folder structure1 ....

Here are some specific examples from the sources:

•

Listing pending notes: You can create a Dataview query to display all permanent notes that have a specific status tag, such as #status/draft8 .... An example query provided is: TABLE file.link AS Nota, status FROM "3_Permanent" WHERE status = "draft" SORT file.mtime DESC8 . This generates a table of draft permanent notes, ordered by modification date8 .

•

Creating automatic Maps of Content (MOCs) or Structure Notes: Instead of manually maintaining lists of links, you can use Dataview to pull all notes with a certain theme tag, such as #theme/filosofia8 .... A query example is: LIST FROM #theme/filosofia AND #type/note SORT file.name8 . This would automatically list all permanent notes tagged with #theme/filosofia8 .

•

Reviewing literature notes: Dataview can help manage literature notes by listing those created within a specific timeframe or those that haven't yet been processed into permanent notes8 .... An example query is: TABLE Author, link FROM #type/paper WHERE date >= 2025-01-01 to have a table of articles (literature notes) read in 2025, with author and link8 .

•

Building project dashboards: Within project notes or control notes, Dataview can display subtasks or related notes within a specific project folder8 .... For example: LIST FROM "4_Project/Meu Projeto" would list all notes within the "Meu Projeto" folder8 .

•

Generating glossaries and indexes: Dataview can automatically create lists of terms and their definitions based on designated metadata. The Glossário template in the Starter Kit includes a Dataview query that generates a table of defined terms, showing the definition (from the lead field) and the number of backlinks to each term9 ....

•

Listing flashcards: If you convert Anki flashcards to Obsidian, you can use Dataview to manage them. A basic query example is:

•

This generates a table of flashcards in the "2_Flashcards" folder containing the tag #cardio14 . An advanced query example is:

•

This lists flashcards from the "AnKing" deck created after 2025-01-01, ordered by creation date15 .

These examples highlight how Dataview uses tags, YAML frontmatter fields (like status, theme, date, author, lead, deck, created), and folder structure to dynamically retrieve and display information from your Zettelkasten2 .... The ability to create these dynamic overviews helps you manage your knowledge, track progress, and discover connections between notes in ways that manual linking alone cannot achieve16 .... Effectively planning your metadata and tag structure is crucial for creating meaningful Dataview queries13 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Listing pending notes, in the larger context of Examples:.

The sources discuss listing pending notes primarily in the context of using the Dataview plugin within Obsidian for a Zettelkasten system1 .... This functionality is highlighted as a practical example of how Dataview can enhance organization and workflow by allowing users to dynamically query and display notes based on their metadata, such as tags or frontmatter properties1 ....

Here's a breakdown of what the sources say about listing pending notes, along with examples:

•

Dataview as a Tool for Dynamic Queries: The sources emphasize that Dataview allows you to treat your Obsidian notes as a database1 .... This means you can write queries to filter and display notes that meet specific criteria, such as having a particular tag or a certain value in their frontmatter1 ....

•

Identifying Pending Notes: The concept of "pending notes" typically refers to notes that are in a specific stage of processing or completion. In the context of a Zettelkasten, this often means Permanent Notes that are still in draft form or Literature Notes that haven't yet been transformed into Permanent Notes2 ....

•

Examples of Listing Pending Notes using Dataview: Several sources provide concrete examples of how to list pending notes using Dataview queries:

◦

Listing draft Permanent Notes by tag: One common example is to list all Permanent Notes that have a #status/draft tag2 .... The query provided in one source is: TABLE file.link AS Nota, status FROM "3_Permanent" WHERE status = "draft" SORT file.mtime DESC10 . This query creates a table showing the link to the note (as "Nota") and its status, filtering notes from the "3_Permanent" folder where the status property is "draft," and sorting them by the last modification time10 .

◦

Listing notes with a "todo" status: Another example mentions listing notes "that contain todo: não concluído"10 . This implies using a frontmatter property (like todo) to mark notes as incomplete and then querying for notes where this property has a specific value10 .

◦

Listing Literature Notes not yet processed: While not explicitly termed "pending," the example of generating a table of "all the Literature Notes that were not yet transformed into permanentes"1 demonstrates the ability to track notes that require further processing. A hypothetical query for this might involve checking for the absence of a specific link or tag that signifies a Permanent Note has been created from the Literature Note.

◦

More general examples: Sources also mention using Dataview to create a "Lista de Notas Pendentes"10 and "listing pending notes" as a general use case2 .... These suggest that the specific criteria for what constitutes a "pending" note can be tailored to the user's workflow and defined through tags or metadata properties.

•

Importance of Metadata (Tags and YAML): The ability to effectively list pending notes using Dataview relies heavily on the consistent use of metadata, particularly tags and YAML frontmatter properties1 .... By consistently tagging notes with their status (e.g., #status/fleeting, #status/draft, #status/to-process) or using specific frontmatter fields (e.g., status: draft, processed: false), users can create accurate and useful Dataview queries to manage their workflow2 ....

In summary, the sources highlight that listing pending notes in an Obsidian Zettelkasten is a practical application of the Dataview plugin1 .... By leveraging tags (like #status/draft) or frontmatter properties (like status: draft or todo: not completed), users can create dynamic lists and tables of notes that require further attention or processing within their knowledge management system2 .... This helps maintain a clear overview of ongoing work and ensures that fleeting insights and literature notes are not forgotten but are instead integrated into the permanent knowledge base18 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Automatic Maps of Content, in the larger context of Examples:.

The sources discuss Automatic Maps of Content (MOCs) primarily through the lens of the Dataview plugin and the potential of AI prompts to assist in their creation. In the larger context of examples, these tools enable the generation of dynamic overviews and indices based on the information within your Obsidian vault.

Structure Notes (Manual MOCs): While the sources heavily emphasize Structure Notes as a way to manually organize and connect related notes1 ..., they also introduce methods for more automatic approaches. Structure Notes, also known as Maps of Content (MOCs) or index notes, serve as high-level navigation hubs, linking to collections of notes on a specific topic1 .... They generally do not contain much new information themselves but act as guides to your knowledge1 . Examples include a note titled "📑 Philosophy - Mapa" that lists and organizes links to numerous philosophical permanent notes, subdivided by subtopic, or a note "📚 Leituras Importantes" that organizes links to various Literature Notes of fundamental books, categorized by subject1 .

Dataview for Automatic Generation: The Dataview plugin is a key tool for creating what can be considered automatic or dynamic MOCs9 .... Dataview allows you to query your notes as if they were a database and display the results in dynamic lists or tables9 . By using Dataview, you can create visualisations that automatically update based on the metadata and content of your notes9 ....

Examples of Automatic MOCs with Dataview:

•

The Glossário template in the Starter Kit includes a Dataview query that generates a table of defined terms, showing their definition (from the lead field) and the number of notes that backlink to each term15 . This automatically creates an index of terms.

•

You can use Dataview to list all permanent notes created within the last week, sorted by their modification date9 .... This acts as an automatic "What's New" MOC for your permanent knowledge.

•

Another example is to generate a table of all Literature Notes that have not yet been transformed into Permanent Notes9 . This helps track the processing stage of your notes.

•

Dataview can also be used to answer questions like "Quais conceitos têm mais conexões (backlinks)?"15 , effectively creating an automatic MOC based on the interconnectedness of your ideas.

•

You can create automatic literature reviews by listing all Literature Notes with specific tags or from particular sources8 .

•

Project dashboards can be built with Dataview, automatically listing tasks, related notes, and progress based on metadata within your Project Notes8 .

To effectively use Dataview for automatic MOCs, it's crucial to plan your tags and frontmatter fields in a way that facilitates the queries you want to create11 .... Consistent tagging and metadata ensure that Dataview can accurately identify and list the notes relevant to your desired MOC15 .

AI Prompts for Assisted Generation: While not fully automatic, AI prompts can help in generating the structure or content for MOCs8 .... For example, you can use a prompt to:

•

Generate a textual mind map based on a set of notes by providing their titles or short summaries. The LLM can then organize and group these items logically, giving you an organizational insight that you can then use to create a manual Structure Note8 ....

•

Ask an AI to suggest tags and links for a note18 ..., which can indirectly aid in building the connections that form the basis of MOCs.

•

Use a prompt to summarize backlinks to a particular note, effectively aggregating the context surrounding that topic from various linked notes18 . This summarized information could then be placed within a Structure Note.

The sources also mention mind maps and concept maps as tools to create connections between notes3 .... While these are often created manually or semi-automatically using plugins like Obsidian Canvas24 , the output can function similarly to a MOC by providing a visual overview of interconnected ideas28 . AI could potentially assist in generating the initial layout or identifying key connections for these visual maps26 .

In summary, while traditional MOCs in a Zettelkasten are often created and maintained manually as Structure Notes, Obsidian allows for the creation of dynamic and automatic overviews using the Dataview plugin. These automatic MOCs, driven by metadata and tags, offer up-to-date perspectives on your knowledge. Additionally, AI prompts can assist in suggesting structures and connections that can inform the creation of both manual and potentially more automated Maps of Content. These methods enhance the ability to navigate and understand the relationships within a growing body of knowledge10 .

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Literature review management, in the larger context of Examples:.

The sources discuss literature review management primarily through the lens of Literature Notes and how they feed into the broader Zettelkasten system within Obsidian1 .... They also highlight how Dataview and potentially AI prompts can aid in this process7 ....

Here's a breakdown of how the sources address literature review management with examples:

•

Literature Notes as the Foundation: The sources consistently emphasize Literature Notes as the initial step in engaging with academic sources or any external material for a literature review1 .... These notes serve to extract the important points from a source, summarize arguments, highlight relevant passages, and include your own observations1 .... A crucial aspect of Literature Notes is that each one should always contain a reference to the original source (link, title, DOI, etc.) to maintain traceability1 ....

◦

Example: When reading a book for your literature review, you would create individual Literature Notes for each key idea or argument, including a brief summary and the page number or link where it originated1 .

•

Transition to Permanent Notes: Literature Notes act as the raw material that then informs the creation of Permanent Notes1 .... In this step, you synthesize the information from your Literature Notes (and potentially multiple sources) into your own words, connecting it with your existing knowledge within the Zettelkasten1 .... This process of transforming extracted information into your own understanding is central to building a coherent literature review within your knowledge base.

◦

Example: After creating several Literature Notes on different aspects of a theory from various papers, you would then formulate one or more Permanent Notes that synthesize these ideas, explain the theory in your own terms, and link it to related concepts already in your vault1 .

•

Organizing and Navigating Literature with Structure Notes and Dataview: The sources suggest using Structure Notes (Maps of Content - MOCs) to organize and provide overviews of the literature you've engaged with1 .... These notes act as hubs that link to collections of Literature and Permanent Notes related to specific themes or aspects of your literature review1 ....

◦

Example: You might have a Structure Note titled "Key Theories in Field X" that lists and links to Permanent Notes explaining each theory, which in turn are based on various Literature Notes from relevant publications1 .

•

Furthermore, the Dataview plugin is highlighted as a powerful tool for creating dynamic lists and tables that can aid in managing your literature review process7 ....

◦

Example: You can use Dataview to generate a table of all Literature Notes with a specific tag related to your literature review topic, allowing you to quickly see all the sources you've processed on that subject11 .

◦

Another example mentioned is using Dataview to create a table of "all the Literature Notes that were not yet transformed into permanentes"11 . This helps track the progress of your literature review by showing which sources you've extracted information from but haven't yet synthesized into your own understanding within Permanent Notes11 . A hypothetical Dataview query for this might filter notes tagged as #type/literature that do not have a specific link or tag indicating a corresponding Permanent Note has been created.

•

Leveraging Metadata for Literature Management: Consistent use of metadata, such as tags (e.g., #source/book, #source/article, #theme/your_topic, #status/processed, #status/to-process) and YAML frontmatter properties (e.g., source: [[Link to Source]], processed: true/false), is crucial for effectively managing literature within the Zettelkasten7 .... This metadata allows you to filter, sort, and query your notes using Dataview to gain insights into your literature review progress11 ....

◦

Example: You could tag all Literature Notes related to "climate change" with #theme/climate-change and use the status property to track whether you've processed them into Permanent Notes (status: processed).

•

AI Assistance in Literature Review (Potential): While not explicitly detailed in the context of full literature review creation, the sources suggest that AI prompts could be used to generate permanent notes from literature notes7 ..., summarize information12 ..., and potentially suggest connections between different literature sources or ideas within your vault7 .... This could indirectly aid in the literature review process by accelerating synthesis and identifying relationships between sources.

◦

Example Prompt: "Read the following Literature Note and create a Permanent Note summarizing the main argument and its implications for [your research question]."25 .

In essence, the sources propose a workflow where you actively engage with literature by creating detailed Literature Notes, synthesize this information into your own understanding in Permanent Notes, and use Structure Notes and Dataview to organize and track your engagement with the sources relevant to your literature review. Consistent metadata practices further enhance the ability to manage and retrieve information throughout this process. While the use of AI for direct literature review generation is not a primary focus, the potential for AI to assist in summarizing and synthesizing information from Literature Notes is suggested.

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Project dashboards, in the larger context of Examples:.

The sources discuss project dashboards primarily in the context of using the Dataview plugin within Obsidian to create dynamic overviews of project-related information1 .... These dashboards serve as examples of how to leverage metadata within your Zettelkasten to organize and visualize information related to specific goals9 ....

In the larger context of examples, project dashboards illustrate the practical application of treating your Obsidian vault as a database using Dataview1 .... By strategically using metadata like tags or properties within your Project Notes9 ..., you can create live, updating views that help you stay organized and track progress2 ....

Here are some key points and examples from the sources:

•

Dataview as the Enabling Tool: The sources consistently highlight Dataview as the primary mechanism for building project dashboards1 .... Dataview allows you to query your notes based on their metadata and display the results in various formats, such as lists or tables1 ....

•

Leveraging Metadata: The effectiveness of project dashboards depends on the consistent use of metadata in your Project Notes2 .... This metadata can include:

◦

Tags: You can use tags like #status/todo, #status/inprogress, or #status/complete to track the progress of tasks within a project2 ....

◦

Frontmatter Properties (YAML): You can define specific properties in the YAML frontmatter of your Project Notes, such as status, due-date, priority, or links to related sub-tasks or notes2 ....

•

Examples of Dataview Queries for Project Dashboards: The sources provide concrete examples of how Dataview queries can be used to build project dashboards:

◦

Listing Subtasks: You can use a query like LIST FROM "4_Project/Meu Projeto" to list all notes located within a specific project folder ("Meu Projeto")2 . This allows you to see all the individual notes associated with that project in one place.

◦

Tracking Task Status: You can create a table showing tasks and their status by using a tag or a frontmatter property. For instance, if you have notes tagged #task and use a #status/todo, #status/inprogress, #status/done system, you could create a Dataview table to display all tasks grouped by their status2 .

◦

Monitoring Progress: By using date-related metadata (e.g., due-date) and status tags, you could create a dashboard that shows overdue tasks, upcoming deadlines, or the completion rate of project tasks9 ....

◦

Displaying Related Notes: You can use Dataview to pull in links to relevant Permanent Notes or Literature Notes that are connected to your project, providing easy access to the underlying knowledge base that informs the project2 .

•

Integration with Project Notes: Project Notes themselves are described as temporary or permanent notes linked to real-world tasks, making them ideal candidates for dashboard integration9 .... They serve to organize tasks, research, and content related to a specific deliverable11 ....

•

Benefits of Project Dashboards: Using Dataview to create project dashboards offers several benefits:

◦

Centralized Information: All relevant project information is aggregated in one easily accessible note2 .

◦

Dynamic Updates: The dashboard automatically updates as you add, modify, or link notes, providing a real-time overview of the project1 .

◦

Improved Organization: By structuring your project information with metadata, you gain better control and clarity over the various components of the project20 .

◦

Enhanced Tracking: Visualizing the status of tasks and progress helps you stay on schedule and identify potential bottlenecks2 .

In essence, project dashboards, as discussed in the sources, are powerful examples of how Obsidian, enhanced by the Dataview plugin, can move beyond simple note-taking to become a dynamic project management tool within the framework of a Zettelkasten system1 .... By combining the principles of interconnected knowledge with structured metadata and dynamic queries, users can create personalized overviews that directly support their project workflows2 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Generating glossaries/indexes, in the larger context of Examples:.

The sources discuss generating glossaries and indexes primarily in the context of using the Dataview plugin within Obsidian1 .... These tools allow for the automatic or semi-automatic creation of these organizational structures based on the content and metadata within your notes1 ....

Here's a breakdown of what the sources say, with examples:

•

Dataview for Automatic Generation: The sources highlight that Dataview can query your Obsidian vault and generate dynamic lists or tables that function as glossaries and indexes1 .... This is achieved by leveraging the metadata in your notes, such as tags and frontmatter properties1 .

◦

Example: Glossary Generation: One specific example is provided by the Glossário template in the Starter Kit, which uses a Dataview query to generate a table of defined terms1 . This table displays the definition of each term (taken from the lead frontmatter field) and the number of notes that backlink to that term1 . This demonstrates how a glossary can be automatically built based on the content of your notes and their connections1 .... The "Explicação imagens.md" source also lists "Glossary" as one of the "Dataview Snippets" that helps navigate and organize knowledge with automatic queries2 ....

◦

Example: Index Generation: Similarly, Dataview can be used to create indexes2 .... While a specific query for a general index isn't explicitly provided in the same detail as the glossary example, the principle is the same: you can query for notes based on specific criteria (e.g., notes tagged with a particular theme or belonging to a certain folder) and list their links in a table format. A Structure Note can then incorporate this Dataview query to function as a dynamic index for a specific topic1 .... The "Explicação imagens.md" source explicitly lists "Index" as a Dataview snippet type2 ....

◦

The "CHAT_GPT_INVESTIGAR_1.md" source mentions that with a well-planned taxonomy of tags and frontmatter fields, Dataview allows you to answer questions like "Quais conceitos têm mais conexões (backlinks)?"1 . The result of such a query could effectively serve as an index of highly connected concepts1 .

•

Structure Notes (MOCs) as Manual or Semi-Automatic Indexes: Structure Notes, also known as Maps of Content (MOCs) or index notes, serve as high-level notes that organize and connect other related notes3 .... While they are often created and maintained manually by linking to relevant notes13 ..., they can also incorporate Dataview queries to dynamically list notes based on certain criteria, making them semi-automatic indexes1 ....

◦

Example: A Structure Note on "#theme/philosophy" could contain a Dataview query that lists all Permanent Notes tagged with #theme/philosophy, effectively acting as an index for that subject16 .

•

AI Prompts for Assisting in Glossary/Index Creation: While not directly generating dynamic glossaries or indexes like Dataview, AI prompts can assist in identifying terms for a glossary or structuring topics for an index3 ....

◦

Example (Glossary): You could use an AI prompt to "create a note in the style of a Glossary for the term X. The note should define the term clearly, list synonyms, and mention the source"3 .... While this creates individual glossary entries, you would likely use Dataview to then compile these into a comprehensive glossary1 ....

◦

Example (Index): An AI prompt could "generate a textual mind map based on a set of notes"3 .... This output could provide a hierarchical structure of topics and subtopics, which you could then use as a basis for creating a manual or semi-automatic index (using links or Dataview)19 .

•

Importance of Metadata for Effective Generation: The ability to create useful glossaries and indexes with Dataview relies heavily on consistently applying metadata such as tags (e.g., #type/term for glossary entries) and frontmatter fields (e.g., lead for definitions)1 .... A well-thought-out system of tags and metadata allows for precise and effective Dataview queries1 .

In summary, the sources emphasize Dataview as the primary tool for automatically generating glossaries and indexes in Obsidian by querying notes based on their metadata and content1 .... Structure Notes can serve as both manual and semi-automatic indexes, potentially incorporating Dataview queries for dynamic content1 .... AI prompts can assist in the process by helping to identify terms and structures, but the dynamic compilation is largely facilitated by Dataview3 .... The effectiveness of these methods is directly tied to the consistent and thoughtful use of metadata within your Zettelkasten1 ....