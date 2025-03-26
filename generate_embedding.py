from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = [PyPDFLoader('./How We Think.pdf')]

doc=[]
for file in loader:
    doc.extend(file.load())
    
Text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs=Text_splitter.split_documents(doc)
embedding_function=HuggingFaceEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'}) 

vectorStore=Chroma.from_documents(documents=docs, embedding=embedding_function, persist_directory='./chroma_db_nccn')

print(vectorStore._collection.count())