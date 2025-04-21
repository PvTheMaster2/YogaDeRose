---
created: 2025-04-14T03:19
updated: 2025-04-14T04:37
---
The sources extensively discuss YAML frontmatter as a crucial component of metadata within an Obsidian Zettelkasten system1 .... Metadata, in general, refers to data about data14 .... In the context of Obsidian, this includes information added to your notes that provides context and facilitates organization and retrieval4 ....

YAML frontmatter is a specific way to add structured metadata to your Markdown notes in Obsidian1 .... It is a block of text at the beginning of a note, enclosed by triple hyphens (---)1 .... This block uses the YAML data serialization format to define key-value pairs, where each line specifies a property (key) and its corresponding value16 .

The sources highlight several key aspects of using YAML frontmatter for metadata:

•

Standardizing Information: YAML frontmatter allows you to padronizar informações about your notes1 . This is crucial for maintaining consistency and making your notes easily searchable and queryable1 . By using a consistent structure, you ensure that important attributes are always recorded in a predictable way16 .

•

Common Metadata Fields: The sources provide numerous examples of metadata fields commonly included in YAML frontmatter1 ...:

◦

tags: A list of tags that classify the note (e.g., type/note, theme/psychology, status/draft)5 .... Tags can be hierarchical (e.g., #type/note)4 ....

◦

aliases: Alternative names or secondary titles for the note, useful for search5 ....

◦

created and modified: Dates of creation and last modification5 ....

◦

lead: A short summary or key phrase defining the note5 ....

◦

based_on or source: Reference to the source or note from which the information came, maintaining traceability5 ....

◦

template_type and version: Indicate the template used for the note17 ....

◦

Project-specific metadata (e.g., status for Project Notes)17 ....

◦

Bibliographic information for Literature Notes (e.g., title, author, publish_date, isbn)23 .

◦

Operational metadata (e.g., rating, read date for books)21 .

•

Templates for Consistency: Creating templates for each note type with pre-formatted YAML is highly recommended24 .... This ensures that essential metadata fields are always present, promoting consistency across your vault5 ....

•

Powering Dataview: Metadata in YAML frontmatter is crucial for the Dataview plugin1 .... Dataview allows you to query your notes as a database based on this structured metadata18 .... You can create dynamic lists, tables, and overviews based on specific criteria defined in the YAML frontmatter (e.g., listing all notes with #status/draft, or all books read in a certain year)12 ....

•

Relationship with Tags: Both YAML frontmatter and tags serve as forms of metadata for organizing and filtering notes4 .... Tags are more free-form and can be added anywhere in the note content, while YAML frontmatter provides a structured and consistent way to record specific attributes5 .... Hierarchical tags (e.g., #type/note) can also be included in the tags field of the YAML frontmatter18 .... As noted in "CHAT_GPT_INVESTIGAR_1.md", "tags categorizam, links conectam diretamente o contexto do conteúdo"12 ....

•

Automation and Efficiency: Consistent metadata in YAML frontmatter, combined with Dataview, enables automation of various tasks like creating automatic maps of content, managing literature reviews, and building project dashboards12 .... AI prompts can also be used to automatically fill metadata in the YAML frontmatter12 ....

•

Enhanced Search and Navigation: Metadata in YAML, including aliases, makes your notes more easily discoverable through Obsidian's search functionality5 .... Combined with tags and links, well-defined metadata contributes to a more navigable and interconnected knowledge base32 ....

In essence, YAML frontmatter provides a structured and powerful way to manage metadata in your Obsidian Zettelkasten. By consistently using it, you lay the foundation for effective organization, dynamic querying with Dataview, and ultimately, a more insightful and manageable knowledge system38 .

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Tags (#), in the larger context of Metadata.

The sources highlight that tags (#) are a crucial component of metadata within an Obsidian Zettelkasten system, providing a flexible way to classify and filter notes beyond direct linking1 .... They work alongside other metadata, often stored in the YAML frontmatter, to enhance organization and information retrieval3 ....

Definition and Basic Function: Tags in Obsidian are keywords prefixed with a # symbol1 .... Their primary function is to categorize notes by topic, type, source, or status, making it easier to find notes that share common attributes, even if they are not directly linked3 .... Edmund Gröpl considers tags as "specially designated search terms"10 .

Hierarchical Tagging: Obsidian supports hierarchical tagging through naming conventions1 .... By using prefixes, you can create broader categories and sub-tags for more granular classification. For example, #type/note and #type/literature share the #type prefix, indicating different types of notes1 .... This allows for more organized filtering and searching3 ....

Common Tag Families: Several common tag families are suggested in the sources11 ...:

•

#type/...: This mandatory tag defines the role of the note within the system11 .... Examples include #type/fleeting, #type/note (permanent), #type/term, #type/book, #type/project, #type/structure, #type/sketchnote, #type/prompt, #type/question, and #type/visual11 ....

•

#source/...: This tag indicates the origin of the information11 .... Examples include #source/book, #source/paper, #source/web, or even more specific sources like #source/YourBlogName11 .

•

#theme/...: This represents the topic or subject of the note11 .... Examples include #theme/psychology, #theme/philosophy, #theme/IA, #theme/learning, #theme/writing, #theme/thinking, and #theme/sketchnoting11 .... A permanent note can have multiple theme tags11 .

•

#status/...: This optional tag denotes the state of a note or project11 .... Examples include #status/draft, #status/idea, #status/complete, and #status/cancelled11 . This is particularly useful for Project Notes or tracking the progress of Permanent Notes11 .

•

#target/...: This tag indicates the intended outcome or application of the note or project11 .... Examples include #target/ebook, #target/blog, and #target/presentation11 ....

•

Other special tags like #🌟 for favorite notes or #toMerge for duplicates can also be used17 .

Relationship with YAML Frontmatter: Tags are often included as a field within the YAML frontmatter of a note1 .... The YAML frontmatter is a section at the beginning of a Markdown file, enclosed by ---, that stores structured metadata about the note22 .... Besides tags, other common YAML fields include1 ...:

•

aliases: Alternative names for the note, aiding search.

•

created and modified: Timestamps of note creation and last edit.

•

lead: A brief summary or key phrase defining the note.

•

based_on or source: Explicit reference to the origin of the information.

•

template_type and version: Indicating the template used.

•

Custom fields relevant to specific note types (e.g., title, author, publish_date for books; birth, death, bio_short for people; quote, year for quotes)19 ....

Tags for Searching, Filtering, and Dataview: Tags significantly enhance searching and filtering of notes3 .... You can easily find all notes with a specific tag or a combination of tags using Obsidian's search functionality27 ....

Furthermore, tags, along with other YAML metadata and folder structure, are crucial for leveraging the power of the Dataview plugin12 .... Dataview allows you to query your notes as if they were a database and display the results in dynamic lists or tables12 .... You can create queries based on specific tags (e.g., list all notes with #type/note and #theme/sci-fi) or combinations of tags and other metadata33 .... Examples of Dataview use with tags include39 ...:

•

Listing pending notes with a #status/draft tag.

•

Creating automatic Maps of Content by listing all notes with a specific #theme/ tag.

•

Managing literature reviews by listing notes with #type/paper within a specific date range.

Cognitive Benefits: Daniel Levitin and Sönke Ahrens suggest that the human brain is pre-configured to classify and categorize information, making tags a natural cognitive interface that not only organizes but also helps in better thinking29 ....

Tags in the Zettelkasten Workflow: Consistent and well-planned tagging is essential for a functioning Zettelkasten system3 .... Along with links, tags help to build clusters of ideas and provide alternative pathways for navigating your knowledge base9 .... While links connect the context of the content directly, tags categorize notes across different contexts31 .... Therefore, a combination of robust linking and a consistent tagging strategy is recommended for an effective Obsidian Zettelkasten31 .

In summary, tags are a vital form of metadata in Obsidian Zettelkasten, working in tandem with YAML frontmatter and internal links to create a well-organized and interconnected knowledge network. Their consistent and hierarchical use enables effective searching, filtering, and powerful dynamic visualizations through the Dataview plugin, ultimately enhancing the process of knowledge creation and retrieval35 .

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Hierarchical Tags, in the larger context of Metadata.

The sources emphasize that hierarchical tags are an important aspect of metadata within an Obsidian Zettelkasten system, contributing significantly to organization, search, and the ability to perform dynamic queries1 ....

Metadata in Obsidian:

Metadata in Obsidian refers to structured information about your notes, which enhances their organization and allows for more powerful retrieval and manipulation4 .... This metadata is often stored in the YAML frontmatter at the beginning of a Markdown file and includes elements like tags, aliases, creation and modification dates, a brief summary (lead), source information (based_on or source), and template details (template_type, version)2 .... The Dataview plugin heavily relies on this metadata to query and display information dynamically4 ....

What are Hierarchical Tags?

Hierarchical tags in Obsidian are created by naming convention, using a prefix to indicate a broader category followed by a sub-tag for more specific classification, separated by a forward slash (e.g., #type/note, #theme/psychology, #source/book)1 .... This allows for a structured system of categorization where tags share a common prefix, indicating they belong to the same family of categories1 ....

Purpose and Benefits of Hierarchical Tags:

•

Classification and Filtering: Hierarchical tags help to classify and filter notes by transversal aspects1 .... By using prefixes like #type/, you can easily distinguish between different kinds of notes such as #type/fleeting, #type/note (permanent), or #type/literature10 ....

•

Granular Categorization: They allow for more granular categorization than simple tags13 .... For example, under the #theme/ prefix, you can have specific subjects like #theme/psychology, #theme/philosophy, or #theme/IA10 ....

•

Semantic Layer of Organization: Hierarchical tags provide an additional semantic layer to your knowledge base16 . Seeing a tag like #theme/learning and #type/note on a note immediately contextualizes it as a permanent note about learning16 .

•

Improved Search: They can facilitate more effective searching and filtering of notes based on broader categories or specific sub-categories1 ....

•

Integration with Dataview: Hierarchical tags are crucial for leveraging the power of the Dataview plugin, which can query your notes based on these tags to create dynamic lists and tables9 .... For instance, you can create queries like "list all notes with #type/note and #theme/sci-fi" or "show all #type/project with #status/ongoing"17 .

•

Consistent Tagging: Using hierarchical tags can promote standardization in your tagging practices, especially when predefined in templates for different note types17 .... This ensures consistency and avoids the ambiguity of using flat tags.

Common Hierarchical Tag Families:

The sources suggest several common families of hierarchical tags10 ...:

•

#type/...: Defines the type of note and is often considered a mandatory tag indicating the note's role in the system (e.g., #type/fleeting, #type/note, #type/book)10 ....

•

#source/...: Indicates the origin of the information (e.g., #source/book, #source/paper, #source/web, #source/YourBlogName)10 ....

•

#theme/...: Represents the topic or subject of the note (e.g., #theme/psychology, #theme/filosofia, #theme/IA)10 .... A permanent note can have multiple #theme tags12 .

•

#status/...: An optional tag for the state of a note or project (e.g., #status/draft, #status/idea, #status/complete)10 .... This is particularly useful for Project Notes or tracking the progress of Permanent Notes.

•

#target/...: Indicates the intended outcome or application of a note or project (e.g., #target/ebook, #target/blog, #target/presentation)10 ....

Relationship with Other Metadata:

Hierarchical tags work alongside other metadata in the YAML frontmatter to provide a comprehensive system for organizing and retrieving information13 .... While tags offer flexible categorization, other fields like lead provide a concise summary, and based_on establishes the source of the note2 .... Aliases provide alternative search terms2 .... All this metadata, including hierarchical tags, can be queried by Dataview9 ....

Hierarchical Tags vs. Folders and Links:

The sources emphasize that in a Zettelkasten, links are more important than folder hierarchy for representing associations between ideas19 . While folders might be used to group processes for managing different types of notes, they are not for structuring ideas20 . Hierarchical tags offer an orthogonal layer of organization to both links and folders16 . Links connect content directly based on context, while tags categorize notes by various relevant facets, allowing you to find related notes even if they are not directly linked9 .

Cognitive Benefits:

Daniel Levitin and Sönke Ahrens are quoted as saying that the brain is pre-configured to classify and categorize automatically, and we use categories to facilitate recognition and grouping. They suggest that tags help to identify the type of information, facilitating future processing, acting as a cognitive interface to not just organize, but also to think better21 .

In summary, hierarchical tags are a valuable component of metadata in an Obsidian Zettelkasten. By providing a structured and semantic way to categorize notes, they enhance organization, improve search capabilities, and enable powerful dynamic queries through plugins like Dataview, ultimately contributing to a more robust and interconnected knowledge system. Consistent use of well-defined hierarchical tags, often facilitated by templates, is crucial for maximizing the benefits of this system.

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about #type/..., in the larger context of Hierarchical Tags.

The sources emphasize that #type/... is a crucial component of hierarchical tagging in Obsidian, particularly within a Zettelkasten system1 .... Hierarchical tags in Obsidian are created by convention using prefixes to indicate broader categories followed by sub-tags for more specific classifications1 .... For example, #type/note and #type/literature both fall under the #type category1 ....

Here's what the sources say about #type/...:

•

Definition and Purpose: The #type/... tag family is used to define the type or role of a note within the Zettelkasten system2 .... It is considered a mandatory tag, indicating the specific function of that note2 . This helps in understanding the nature of the information contained within a note7 .

•

Examples of #type/... Tags: Several examples of #type/... tags are provided across the sources:

◦

#type/fleeting2 (Fleeting Note)

◦

#type/note2 ... (Permanent Note)

◦

#type/term2 (Reference Note for a term)

◦

#type/book2 (Literature Note for a book)

◦

#type/prompt2 (Note containing a prompt or idea)

◦

#type/literature1 ... (Literature Note)

◦

#type/structure8 (Structure Note)

◦

#type/sketchnote9

◦

#type/question9

◦

#type/visual9

◦

#type/paper10 (Literature Note for a paper)

•

Mandatory Nature: The #type/... tag is often described as mandatory, highlighting its importance in categorizing the fundamental nature of each note in your vault2 . This ensures that the role of each piece of information is clearly defined within the system2 ....

•

Integration with Templates: It is suggested to include #type/... in note templates, particularly in the frontmatter. For example, a template for a Permanent Note might include tags: [type/note, theme/...]11 . Edmund Gröpl's templates also pre-fill mandatory tags like #type/... to ensure consistency12 .

•

Benefits for Searching and Filtering: Using #type/... as part of a hierarchical tagging system allows for efficient searching and filtering of notes based on their type1 .... For instance, you can easily find all your Permanent Notes by searching for #type/note10 ....

•

Synergy with Dataview: The #type/... tag is particularly useful with the Dataview plugin, which allows you to query your notes as a database4 .... You can create dynamic lists or tables of notes of a specific type. For example, you could list all #type/book notes or all #type/note that have a certain #theme/... tag10 ....

•

Relationship to Note Workflow: The #type/... tag helps to visualize and manage the flow of knowledge within the Zettelkasten system14 .... By clearly identifying note types, you can ensure that Fleeting Notes are processed into Literature or Permanent Notes, and so on15 ....

In summary, #type/... is a foundational element of hierarchical tagging in an Obsidian Zettelkasten. It serves to clearly define the function of each note, making the system more organized, searchable, and allowing for dynamic visualizations and queries using tools like Dataview. Its mandatory nature, as highlighted in the sources, underscores its importance in maintaining a well-structured and effective personal knowledge management system2 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about #source/..., in the larger context of Hierarchical Tags.

The sources emphasize the role of hierarchical tags as a crucial element for organizing and filtering notes within an Obsidian Zettelkasten system1 .... Hierarchical tags are created by using prefixes to denote broader categories followed by more specific sub-categories, separated by a forward slash (e.g., #category/subcategory)1 ....

In this context, #source/... is identified as one of the common and useful families of hierarchical tags4 .... The primary purpose of the #source/... tag family is to indicate the origin of a particular note4 .... This allows users to easily track where the information in their notes originated from4 .

Here's a breakdown of what the sources say specifically about #source/... within the larger context of hierarchical tags:

•

Categorization of Sources: The #source/... tag allows for the categorization of notes based on the type of source they draw information from4 . Examples provided include #source/book, #source/paper, #source/web, and even more granular designations like #source/YourBlogName4 . This enables you to quickly identify and filter notes based on whether they originated from a book, a research paper, a website, or another specific source4 .

•

Hierarchical Structure: As part of the hierarchical tagging system, #source/... can be further refined with more specific sub-tags. For instance, you could have #source/book/psychology to indicate a book on psychology or #source/web/blogpost for a blog post2 .... This allows for a more detailed and nuanced classification of your sources.

•

Traceability and Integrity: The consistent use of #source/... tags supports the Zettelkasten principle of always referencing the source of your notes7 .... By tagging notes with their origin, you maintain traceability and the intellectual integrity of your knowledge base11 ....

•

Filtering and Searching: The #source/... tag family facilitates efficient filtering and searching of your notes1 .... You can easily find all notes derived from a specific type of source (e.g., all notes based on academic papers) by searching for the corresponding #source/... tag4 ....

•

Integration with Dataview: When used in conjunction with the Dataview plugin, #source/... tags become even more powerful5 .... You can create dynamic lists and tables of notes based on their source. For example, you could generate a list of all #type/literature notes tagged with #source/book that you have read in a particular year16 ....

•

Templates for Consistency: The sources recommend creating templates for different note types, and these templates can include predefined #source/ tags8 .... This encourages the consistent recording of source information when creating new notes8 .

•

Relationship to Note Types: The "Explicação imagens.md" source (Diagram 2) specifically identifies #source/ as a preferred tag for Permanent Notes18 and a mandatory tag component for Reference Notes such as #type/term, #type/book, #type/person, #type/quote, and #type/tool19 . This highlights the importance of tracking the origin of both your synthesized knowledge and your direct extractions from sources.

In summary, the #source/... family of hierarchical tags is a fundamental component of a well-organized Obsidian Zettelkasten. It provides a structured and consistent way to categorize notes based on their origin, supporting traceability, efficient searching, and powerful querying with tools like Dataview4 .... By adopting a clear convention for your #source/... tags, you can significantly enhance the organization and utility of your personal knowledge management system20 .

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about #theme/..., in the larger context of Hierarchical Tags.

The sources highlight that #theme/... is a key component of a hierarchical tagging system within Obsidian, used for classifying notes by their subject matter or topic1 .... Hierarchical tags, in general, are created by naming conventions using prefixes to indicate broader categories and sub-tags for more specific classifications1 .... For example, #type/note and #type/literature both share the #type prefix, indicating they are different types of notes1 ....

In this context, #theme/... serves to represent the main subject or topic that a note addresses2 .... It acts as a way to categorize your knowledge by intellectual domain or area of interest2 .... The sources provide several examples of #theme/... tags:

•

#theme/psychology3 ...

•

#theme/philosophy2

•

#theme/IA (Artificial Intelligence)2

•

#theme/learning13 ...

•

#theme/writing13 ...

•

#theme/thinking13

•

#theme/sketchnoting13

•

#theme/zettelkasten13 ...

•

#theme/sci-fi16

•

#theme/engenharia17

The #theme/... tag family is designed to be orthogonal to links and folders, offering another layer of organization18 . While links connect the context of content directly, tags categorize11 .... A single permanent note can have multiple #theme tags to indicate the various subjects it encompasses2 .

Within the larger context of hierarchical tags, #theme/... plays a crucial role in several ways:

•

Semantic Layer: It adds a semantic layer to your notes, allowing you to quickly understand the subject matter of a note just by looking at its tags18 . For instance, seeing #theme/learning and #type/note together contextualizes the note as a permanent note about learning18 .

•

Enhanced Filtering and Searching: The hierarchical structure of #theme/... allows for more granular filtering and searching1 .... You can search for all notes broadly tagged with #theme/ or narrow it down to specific sub-themes like #theme/psychology/cognitive. This is explicitly mentioned as a benefit of tags in general20 .

•

Dataview Queries: #theme/... tags are invaluable for creating dynamic visualizations and queries using the Dataview plugin4 .... You can create automatic Maps of Content (MOCs) by listing all notes with a specific theme tag (e.g., LIST FROM #theme/filosofia AND #type/note)21 . You can also combine #theme/... with other tag families in Dataview queries, such as listing all project notes (#type/project) with a specific theme and a status of ongoing (#status/ongoing)16 . You could also list all notes with the #theme/zettelkasten tag created in the last week15 .

•

Organization and Navigation: By consistently applying #theme/... tags, you create clear pathways for navigating your knowledge base23 .... Structure notes can then aggregate and organize notes based on these theme tags23 .... As Edmund Gröpl suggests, tags can be used to build up an index and define clusters of related notes20 .

•

Integration with AI: AI prompts can leverage #theme/... tags to suggest related notes or identify knowledge gaps within specific thematic areas25 .... For example, you could ask an LLM to analyze notes with a particular #theme/ tag and suggest related readings or missing aspects25 ....

In summary, the #theme/... tag family within a hierarchical tagging system provides a structured and semantic way to categorize the content of your notes by subject. This facilitates organization, efficient searching and filtering, powerful querying with Dataview, and potential integration with AI tools, ultimately enhancing the management and utilization of knowledge within your Obsidian Zettelkasten4 .... The consistency in applying these tags, as emphasized in the sources regarding standardized practices29 , is key to unlocking these benefits.

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about #status/..., in the larger context of Hierarchical Tags.

The sources indicate that #status/... is a family of optional hierarchical tags used within an Obsidian Zettelkasten system1 .... As part of the larger context of hierarchical tags, where prefixes denote broader categories and sub-tags specify further4 ..., #status serves as the main category to denote the state of a particular note or project1 ....

Here's a breakdown of what the sources say about #status/...:

•

Purpose: The primary function of #status/... tags is to indicate the current condition or stage of a note or project1 .... This allows for tracking the progress and distinguishing between notes that are, for example, still being drafted, are just ideas, have been completed, or have been cancelled1 .

•

Optional Nature: Unlike #type/..., which is often considered mandatory1 ..., #status/... is described as an optional tag family1 .... This suggests that its use is dependent on the individual's workflow and the level of detail they wish to track regarding the state of their notes and projects.

•

Examples of #status/... Tags: The sources provide several examples to illustrate the usage of #status/...:

◦

#status/draft1 ...: To mark notes that are still in the process of being written or refined.

◦

#status/idea1 : To categorize notes that represent initial thoughts or concepts.

◦

#status/complete1 : To indicate that a note or project has reached its final stage.

◦

#status/cancelled1 : To mark projects or ideas that are no longer being pursued.

•

Usefulness for Specific Note Types: The #status/... tag family is highlighted as potentially particularly useful for Project Notes1 . Given that Project Notes are focused on specific, temporary projects with defined objectives11 ..., tracking their status (e.g., #status/ongoing, #status/on-hold, #status/done) can be beneficial for project management. It can also be useful for monitoring the progress of elaborating Permanent Notes1 .

•

Integration with Dataview: Similar to other hierarchical tags, #status/... tags can be leveraged with the Dataview plugin2 .... You can create dynamic lists or tables of notes based on their status. For example, you could generate a list of all #type/project notes with the tag #status/ongoing16 .

In the larger context of hierarchical tags, #status/... provides an additional layer of organization that is orthogonal to tags like #type/... and #theme/...18 . While #type defines the role of the note and #theme its subject matter, #status describes its current state of development or completion. This allows for more nuanced filtering and management of notes within your Zettelkasten based on where they are in your workflow5 .... Consistent use of #status/..., when relevant to your needs, can enhance your ability to manage your notes and projects within Obsidian19 .

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about #target/..., in the larger context of Hierarchical Tags.

The sources indicate that #target/... is a family of hierarchical tags used in an Obsidian Zettelkasten system to indicate the intended outcome or application of a particular note or project1 .... Hierarchical tags, in general, are created by convention using prefixes to denote broader categories followed by sub-tags for more specific classifications4 ....

Here's a more detailed breakdown of what the sources say about #target/...:

•

Definition and Purpose: The #target/... tag family serves to specify where a note or the knowledge contained within it is intended to be used or applied1 .... This helps to differentiate notes that have a specific output or purpose in mind1 .

•

Optional Nature: Unlike #type/... which is often described as mandatory, #target/... is presented as an optional tag family1 .... This suggests that it's used when a specific destination or application is relevant to the note or project.

•

Examples of #target/... Tags: The sources provide several examples of how #target/... tags can be used1 ...:

◦

#target/ebook1 ... (indicating the note's content will be used in an ebook)

◦

#target/blog1 or #target/post7 ... (suggesting the content is for a blog post)

◦

#target/presentation1 ... (meaning the note will contribute to a presentation)

◦

#target/discussion7 ...

◦

#target/github7 ...

•

Context of Note Types: The #target/... tag is mentioned in relation to specific note types:

◦

Permanent Notes: It is listed among the possible tags for Permanent Notes, indicating the intended application of the consolidated knowledge within these core Zettelkasten notes7 ....

◦

Structure Notes: A destination tag #target/ is also associated with Structure Notes8 ....

◦

Project Notes: The initial description of #target/... in one source suggests it can indicate a destination or application for a note or project1 .

•

Integration with Workflow: By using #target/... tags, you can track which parts of your knowledge base are intended for specific outputs, aligning your note-taking with your goals for applying that knowledge1 . This can help in organizing your thinking around concrete deliverables.

•

Potential for Filtering and Dataview: Although not explicitly detailed, like other hierarchical tags, #target/... can be used for filtering notes based on their intended use. Furthermore, it could be leveraged with the Dataview plugin to create dynamic lists of notes that are targeted for specific outputs (e.g., a list of all notes tagged #target/blog that are ready for review)2 ....

In the larger context of hierarchical tags, #target/... adds another dimension to the organization of your Zettelkasten. While #type/... defines the role of a note within the knowledge flow1 , #source/... tracks its origin1 , and #theme/... categorizes its subject1 , #target/... looks towards the future application of that knowledge. This tag family, though optional, provides valuable metadata for managing and utilizing the information within your Obsidian vault, helping to bridge the gap between knowledge acquisition and its practical implementation in projects and outputs.

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Aliases, in the larger context of Metadata.

The sources consistently identify aliases as a component of metadata within Obsidian, which plays a significant role in organizing and retrieving information in a Zettelkasten system1 ....

Here's what the sources say about aliases in the larger context of metadata:

•

Definition and Purpose: Aliases are defined as alternative names or secondary titles for a note1 .... Their primary function is to aid the search mechanism in recognizing synonyms1 . This means that even if you don't remember the exact title of a note, you can still find it by searching for one of its aliases2 ....

•

Location: Aliases are typically included in the YAML frontmatter of an Obsidian note, which is a standard location for storing metadata1 .... The YAML frontmatter is enclosed in triple hyphens at the beginning of a Markdown file8 .

•

Benefit for Searching: By providing alternative names, aliases enhance the discoverability of notes4 .... This is particularly useful when different terms can refer to the same concept. For example, a note titled "Artificial Intelligence" could have an alias "AI," allowing users to find the note using either term9 ....

•

Relationship to Other Metadata: Aliases exist alongside other metadata such as tags (#theme/psychology, #type/note), creation and modification dates, a brief lead summary, and references to the source of the information1 .... All these metadata elements contribute to a richer and more searchable knowledge base11 ....

•

Use with Plugins: The metadata, including aliases, becomes particularly powerful when used with plugins like Dataview11 .... Dataview can query your notes based on this structured information, allowing you to create dynamic lists and tables11 .... Aliases can help ensure that all relevant notes are included in these Dataview queries, even if they have different primary titles.

•

Consistent Naming: While aliases provide flexibility in searching, the "Explicação imagens.md" source (Diagram 3) highlights the importance of consistent naming conventions as a key element for effective file searching10 . Aliases complement consistent naming by accounting for variations and synonyms that users might employ during searches.

In essence, aliases are a valuable form of metadata in Obsidian that increase the flexibility and effectiveness of searching within a Zettelkasten system. By providing alternative labels for notes, they ensure that information can be retrieved using various related terms, contributing to a more robust and user-friendly personal knowledge management system2 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Lead (Summary), in the larger context of Metadata.

The sources describe lead as a key piece of metadata within the context of an Obsidian Zettelkasten system, typically implemented in the YAML frontmatter of a note1 .... In the larger context of metadata, which is structured information about a note, the lead field serves a specific purpose related to describing and accessing the note's content1 ....

Here's what the sources say about the lead field:

•

Definition: The lead is a small summary or key phrase that defines the note1 .... It acts as a concise identifier of the note's central idea1 .

•

Purpose: Its primary function is to describe the content of the note briefly6 .... This makes it easier to quickly understand what a note is about without having to open and read the entire content1 .

•

Usefulness for Searching and Organization: The lead field is considered a principal field of descriptive metadata7 . Descriptive metadata, in general, serves "to query structured content elements" and is very useful for detailed searches, lists, and sorting via Dataview6 .... The concise summary in the lead can be particularly helpful when scanning through lists of notes generated by Dataview1 ....

•

Display in Dataview and Tooltips: The lead is specifically mentioned as a field that can be displayed automatically in Dataviews or tooltips1 . This allows for a quick preview of a note's content when hovering over a link or when it appears in a Dataview list1 .

•

Template Integration: It is suggested that templates for Permanent Notes can include a pre-formatted lead: field that is initially empty, prompting the user to fill it in when creating a new note12 . This encourages the consistent use of the lead metadata across all notes of a certain type12 .

•

Enhanced Discoverability: By providing a clear and concise summary, the lead contributes to making notes more discoverable and manageable as a Zettelkasten vault grows8 ....

In essence, the lead field in the YAML frontmatter acts as a brief, human-readable summary or key takeaway of a note. As a form of descriptive metadata, it enhances the organization and retrieval of information within an Obsidian Zettelkasten by facilitating quick understanding, improved search results in Dataview, and informative tooltips1 .... Consistent use of the lead field, possibly through note templates, is encouraged to maximize its benefits for navigating and working with a large network of interconnected ideas8 ....

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Based_on/Source, in the larger context of Metadata.

The sources emphasize that the metadata fields based_on or source serve a crucial role in maintaining the traceability and integrity of knowledge within an Obsidian Zettelkasten system1 .... In the larger context of metadata, which enhances note organization and querying2 ..., these fields specifically address the origin of the information contained within a note1 ....

Here's a breakdown of what the sources say:

•

Purpose: The primary function of based_on or source is to provide a reference to the original source from which the information in a note was derived1 .... This is a fundamental rule in a well-defined Zettelkasten workflow2 ..., ensuring that you can always trace an idea back to where you encountered it10 .... This is explicitly stated as "todo nota deve referenciar sua fonte de origem – isso mantém a rastreabilidade e a integridade do conhecimento"10 ... and "Always keep a link to the source."16 .

•

Location: Like other metadata, based_on or source is typically located in the YAML frontmatter of an Obsidian note1 .... This structured format allows for easy querying and retrieval of this information2 ....

•

Application to Different Note Types: The necessity of referencing the source is highlighted across various note types:

◦

Literature Notes: These notes, which extract information from sources like books and articles, must always contain a reference to the original source (link, book title, DOI, etc.) to maintain traceability10 .... The sources repeatedly emphasize "Referência obrigatória via link para a fonte." for Literature Notes19 ....

◦

Permanent Notes: While Permanent Notes synthesize information in your own words, they often originate from Literature or Fleeting Notes2 .... The based_on or source field can link back to the Literature Note(s) that inspired the Permanent Note, further strengthening the connection to the original material1 ....

◦

Project Notes: These can include links to sources, similar to Literature Notes17 .

•

Relationship with Other Metadata: based_on or source works in conjunction with other metadata fields to provide a comprehensive picture of a note's context1 .... For example, it complements:

◦

Tags (#source/...): While #source/... categorizes the type of source (e.g., #source/book, #source/web)26 ..., based_on or source specifies the exact source1 ....

◦

created and modified: These timestamps track the note's evolution, while based_on/source anchors its intellectual origin1 ....

◦

lead: The brief summary helps understand the note's content, and based_on/source provides the context of where that content came from1 ....

•

Benefits for Workflow and Tooling: Having consistent based_on or source metadata enables several benefits:

◦

Rigor and Credibility: It allows you to easily verify information and understand its context16 ....

◦

Future Review: When revisiting notes, you can quickly refer back to the original source for clarification or deeper understanding30 .

◦

Dataview Queries: You can use Dataview to query notes based on their source, for example, listing all notes derived from a specific book10 .... This allows for dynamic literature reviews or tracking the influence of particular sources on your thinking10 ....

◦

AI Integration: As mentioned in our conversation history and the sources, LLMs can potentially analyze your notes and their sources, suggesting connections or identifying gaps10 .... Knowing the source is crucial for the LLM to provide relevant context.

In summary, the based_on or source metadata field is a cornerstone of the Zettelkasten method as implemented in Obsidian1 .... It is integral to the principle of always linking back to the origin of an idea, ensuring the long-term value, reliability, and interconnectedness of your personal knowledge base. By consistently using this metadata, you create a system where knowledge is not just collected but is also situated within its intellectual lineage, enhancing your ability to understand, synthesize, and utilize it effectively.

keep_pinSave to note

copy_all

thumb_up

thumb_down

Discuss what these sources say about Template_type/Version, in the larger context of Metadata.

The sources indicate that template_type and version are specific fields within the larger context of metadata, typically implemented in the YAML frontmatter of Obsidian notes, and are associated with the use of templates in a Zettelkasten system1 ....

Here's what the sources say about them:

•

Purpose: The primary purpose of template_type and version metadata is to support the general management of information resources within your Obsidian vault5 . They serve to identify which template was used to create a particular note and track the specific version of that template1 .... This is particularly useful when you have multiple templates for different types of notes (e.g., Permanent Notes, Literature Notes, Project Notes) and when those templates might be updated or modified over time1 .

•

Location: These metadata fields are generally found within the YAML frontmatter at the top of an Obsidian Markdown file, enclosed by --- delimiters1 ....

•

Benefits for Organization and Maintenance:

◦

Standardization: Including template_type helps ensure that notes intended to have a consistent structure indeed adhere to a specific format defined by a template1 ....

◦

Tracking Evolution: The version field allows you to see which version of a template was used for a note. This is valuable for maintaining notes over time, especially if you update your templates1 .... If you make changes to a template, knowing the version of a note can help you understand its original structure and decide if or how to update its content or metadata to align with the newer template version1 .

◦

Administrative Control: This metadata assists in the overall management of your knowledge base by providing information about the underlying structure of your notes5 .

◦

Facilitates Queries: Like other metadata in the YAML frontmatter, template_type and version can be leveraged by plugins like Dataview1 .... You could, for example, query all notes created using a specific version of a particular template5 ....

•

Integration with Templates: The use of template_type and version is directly linked to the practice of creating and using templates for different note types6 .... It is recommended to create templates for each type of note, and these templates can come with a pre-formatted YAML frontmatter that already includes fields like template_type6 .... This encourages consistency across notes of the same type6 . Edmund Gröpl's Starter Kit templates are mentioned as having pre-filled tags, which aligns with the idea of including template_type and potentially a default version in templates11 .

In the broader context of metadata, template_type and version contribute to a more structured and manageable Zettelkasten12 .... While tags categorize content and aliases aid search, template_type and version provide information about the structural framework of the notes themselves. This allows for better organization, easier maintenance of a consistent note structure as your system evolves, and more powerful querying capabilities through tools like Dataview1 .... By tracking the template used and its version, you gain a deeper level of control and understanding of your knowledge base's underlying organization5 .