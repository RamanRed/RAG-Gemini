# 📚 PDF Question Answering using Gemini + HuggingFace + LangChain

This project is a simple yet powerful Q&A pipeline that allows you to query a PDF file and receive AI-generated answers using:
- 💡 **LangChain** for document splitting, embeddings, and vector storage
- 🧠 **HuggingFace** MiniLM for semantic similarity
- 💃 **ChromaDB** as a persistent vector store
- 🤖 **Google Gemini API** for generating natural language responses

---

## 🧠 What It Does

1. Loads and reads your PDF file (e.g., `How We Think.pdf`)
2. Splits the document into smaller chunks using `RecursiveCharacterTextSplitter`
3. Embeds these chunks using HuggingFace `all-MiniLM-L6-v2`
4. Stores the embeddings in a local Chroma vector database
5. Takes your query, finds the most relevant chunks
6. Passes the results to Google Gemini for answer generation

---

## 📁 Folder Structure

```plaintext
📆pdf-gemini-qa/
 ├ 📄 rag.py
 ├ 📄 requirements.txt (below you can see)
 ├ 📄 .env
 ├ 📄 How We Think.pdf
 ┗ 📁 chroma_db_nccn/
```

---

## 📆 Requirements & Setup

### 🐍 Python Version

- Python 3.8 or higher

### ⚖️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/pdf-gemini-qa.git
cd pdf-gemini-qa

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 📄 Create .env File

You need to add your Gemini API key to a `.env` file in the root folder:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

---

## 📚 Required Packages

Here’s what’s in your `requirements.txt`:

```txt
langchain
langchain-community
chromadb
huggingface-hub
sentence-transformers
python-dotenv
google-generativeai
PyPDF2
```

### 🕽️ Installation (Alternative Manual Way)

If you’re not using `requirements.txt`, you can install packages manually:

```bash
pip install langchain
pip install langchain-community
pip install chromadb
pip install huggingface-hub
pip install sentence-transformers
pip install python-dotenv
pip install google-generativeai
pip install PyPDF2
```

---

## 🛠 Usage

Run the script:

```bash
python main.py
```

You'll be prompted:

```bash
What is your Query:
```

Ask questions based on the content of your PDF!

---

## ✅ Example Query

```bash
What is your Query: What is reflective thinking according to the author?
```

---

## 🔐 Environment Variables

- `GEMINI_API_KEY`: Your API key from Google AI Studio (https://ai.google.dev/)

---

## 🧪 Sample Prompt Sent to Gemini

```txt
## Context:
<relevant document content>

## Query:
Why does the author emphasize reflective thinking?

## Instructions:
- Use ONLY the provided context to answer the query.
- If the context does not contain enough information, say "I don't have enough information."
- Provide factual and well-structured responses.
```

---
## 🙌 Acknowledgments
HuggingFace

LangChain

Google AI / Gemini

## 🙌 Acknowledgments

- [HuggingFace](https://huggingface.co/)
- [LangChain](https://www.langchain.com/)
- [Google AI / Gemini](https://ai.google.dev/)

