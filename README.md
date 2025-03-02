<div align="left" style="position: relative;">
<img src="E-Commerce-Support-Agent-RAG.png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>E-COMMERCE-SUPPORT-AGENT-RAG</h1>
<p align="left">
	<em>Empowering Commerce with Conversational AI Precision</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/HopMaster03/E-Commerce-Support-Agent-RAG?style=default&logo=opensourceinitiative&logoColor=white&color=a2aaad" alt="license">
	<img src="https://img.shields.io/github/last-commit/HopMaster03/E-Commerce-Support-Agent-RAG?style=default&logo=git&logoColor=white&color=a2aaad" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/HopMaster03/E-Commerce-Support-Agent-RAG?style=default&color=a2aaad" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/HopMaster03/E-Commerce-Support-Agent-RAG?style=default&color=a2aaad" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The E-Commerce-Support-Agent-RAG project provides a comprehensive understanding of the working behind a Customer Service Agent for online retailers by utilizing advanced AI to provide dynamic, personalized support by implementing **Adaptive RAG**.<br>
**Adaptive RAG** is a method that chooses the best strategy for answering questions, from a direct LLM response to single or multiple retrieval steps. This selection is based on the query’s complexity, as determined by a classifier. The 2 strategies for answering are:<br>

- **Single-Step Retrieval**: For moderately complex questions, it retrieves information from a single external source, ensuring the answer is both swift and well-informed.<br>
- **Multi-Step Retrieval**: For highly complex questions, it consults multiple sources, piecing together a detailed and comprehensive answer.<br>
<br>
This system efficiently processes and responds to customer inquiries, ensuring a seamless QA experience. Ideal for e-commerce platforms seeking to enhance customer interaction and satisfaction, it leverages machine learning to handle queries with precision and speed.<br>

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes a modular approach with separate components for handling different functionalities such as user interaction, data management, and response generation.</li><li>Employs `ChromaDB` for efficient management and indexing of embedding data.</li><li>Integrates AI-driven response generation using `LiteLLM`.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Code is organized into logical modules such as `app.py`, `rag/`, and `agent/` for clarity and maintainability.</li><li>Uses `Pydantic` for data validation and schema management, enhancing code reliability.</li><li>Adheres to Pythonic standards for readability and maintainability.</li></ul> |
| 📄 | **Documentation** | <ul><li>Documentation includes detailed comments within code files explaining the purpose and functionality of each component.</li><li>Provides comprehensive setup instructions using `pip` and `requirements.txt`.</li><li>Usage and test commands are clearly documented for easy setup and testing.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with `ChromaDB` for data storage and retrieval.</li><li>Uses `LiteLLM` for AI and machine learning capabilities.</li><li>Environment variables managed through `python-dotenv` for secure configuration.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Highly modular design with clear separation of concerns among components like `EmbeddingService`, `SupportAgent`, and utility modules.</li><li>Allows easy extension or modification of individual components without affecting others.</li><li>Modular structure supports scalable development and maintenance.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes testing setup with `pytest` for ensuring code quality and functionality.</li><li>Test commands provided in the documentation to facilitate continuous integration and deployment processes.</li><li>Modular design aids in isolating and testing specific components effectively.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized data handling and response generation for real-time user interaction.</li><li>Efficient embedding storage and retrieval with `ChromaDB`.</li><li>Batch processing capabilities in `EmbeddingService` enhance performance for multiple texts.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Uses environment variables for secure API key management.</li><li>Secure data handling and processing practices are implied through the use of `Pydantic` models.</li><li>No explicit security vulnerabilities mentioned, but standard security practices are assumed.</li></ul> |

---

## 📁 Project Structure

```sh
└── E-Commerce-Support-Agent-RAG/
    ├── LICENSE
    ├── README.md
    ├── agent
    │   ├── support_agent.py
    │   └── utils.py
    ├── app.py
    ├── chainlit.md
    ├── config
    │   └── settings.py
    ├── data
    │   ├── knowledge_base
    │   ├── loaders
    │   └── processors
    ├── llm
    │   ├── litellm_service.py
    │   └── prompt_templates.py
    ├── models
    │   └── schema.py
    ├── rag
    │   ├── embedding_service.py
    │   └── vector_store.py
    └── requirements.txt
```


### 📂 Project Index
<details open>
	<summary><b><code>E-COMMERCE-SUPPORT-AGENT-RAG/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/app.py'>app.py</a></b></td>
				<td>- App.py serves as the entry point for a customer support chat application, initializing the support agent and handling user queries<br>- Upon starting a chat, it loads and indexes necessary data, displays initialization status, and sends a welcome message<br>- It processes incoming messages and generates responses using a support agent, ensuring a dynamic and interactive user experience.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Requirements.txt specifies the necessary Python packages for the project, ensuring consistent environments across different setups<br>- It includes libraries for AI operations, database interactions, environment variable management, numerical computations, and testing<br>- This setup is crucial for maintaining project functionality and compatibility, facilitating development and deployment processes.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- rag Submodule -->
		<summary><b>rag</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/rag/vector_store.py'>vector_store.py</a></b></td>
				<td>- ChromaVectorStore serves as a wrapper for ChromaDB, facilitating the storage of pre-generated embeddings in a specified collection using an ephemeral client<br>- It supports adding embeddings along with optional texts, metadata, and custom IDs, generating UUIDs for documents when IDs are not provided<br>- This component enhances the project's capability to manage and index large volumes of embedding data efficiently.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/rag/embedding_service.py'>embedding_service.py</a></b></td>
				<td>- EmbeddingService in `rag/embedding_service.py` manages the generation of text embeddings using the LiteLLM library, configured with specific API keys and model settings<br>- It supports batch processing for multiple texts and handles individual queries, providing a scalable solution for embedding generation within the project's architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- agent Submodule -->
		<summary><b>agent</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/agent/support_agent.py'>support_agent.py</a></b></td>
				<td>- SupportAgent in `agent/support_agent.py` orchestrates customer interactions for an e-commerce platform by leveraging machine learning models to process and respond to user queries<br>- It initializes services for data loading, text processing, and embedding generation, and handles query classification, context generation, and personalized customer responses based on the nature of the inquiry.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/agent/utils.py'>utils.py</a></b></td>
				<td>- Agent/utils.py serves as a utility module within the broader codebase, primarily handling the parsing of responses from language models and JSON files into structured Pydantic models<br>- It facilitates the extraction and transformation of data into a format that supports further processing and integration within the application's architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- config Submodule -->
		<summary><b>config</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/config/settings.py'>settings.py</a></b></td>
				<td>- Config/settings.py establishes the environment for accessing API keys and configuring models within the software architecture<br>- It initializes settings for embedding and language models, defines parameters for data retrieval, and sets agent behavior controls, ensuring the application interacts effectively with external AI services and manages data processing efficiently.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- llm Submodule -->
		<summary><b>llm</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/llm/prompt_templates.py'>prompt_templates.py</a></b></td>
				<td>- The `prompt_templates.py` in the `llm` directory defines structured templates for handling customer support queries, specifically focusing on extracting and responding to order-related information<br>- It categorizes queries into general knowledge requests and specific customer order data, ensuring responses are tailored and relevant based on the explicit details requested by the customer.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/llm/litellm_service.py'>litellm_service.py</a></b></td>
				<td>- LiteLLMService in llm/litellm_service.py serves as the interface for generating responses using a language model<br>- It initializes with API and model settings, and offers a method to produce text outputs based on user prompts and optional system messages, handling errors gracefully during the process.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- models Submodule -->
		<summary><b>models</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/master/models/schema.py'>schema.py</a></b></td>
				<td>- Defines data models essential for managing product and order information within the system<br>- Models such as Product, OrderDetails, and CustomerDetails facilitate structured data storage and retrieval for order processing and customer management, enhancing the system's ability to handle e-commerce transactions efficiently.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ⚙️ Installation Guide

Install E-Commerce-Support-Agent-RAG using one of the following methods:

**Build from source:**

1. Clone the E-Commerce-Support-Agent-RAG repository:
```sh
❯ git clone https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG
```

2. Navigate to the project directory:
```sh
❯ cd E-Commerce-Support-Agent-RAG
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


### 🤖 Usage
Run E-Commerce-Support-Agent-RAG using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ chainlit run app.py -w
```



---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Adaptive RAG</strike>
- [ ] **`Task 2`**: Enabling conversation history & caching.
- [ ] **`Task 3`**: Metadata Filtering.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/issues)**: Submit bugs found or log feature requests for the `E-Commerce-Support-Agent-RAG` project.
- **💡 [Submit Pull Requests](https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/HopMaster03/E-Commerce-Support-Agent-RAG
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/HopMaster03/E-Commerce-Support-Agent-RAG/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=HopMaster03/E-Commerce-Support-Agent-RAG">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
