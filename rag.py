import os
import sys
import signal
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model=genai.GenerativeModel("gemini-2.0-flash")

embededQuery=HuggingFaceEmbeddings( model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'} ) 


def TextGeneration(query, prompt):
    
    result = model.generate_content(prompt)
     # Extract text correctly
    response_text = result.text if hasattr(result, "text") else str(result)
    
    return f"Your Query:\t{query}\nResponse:\n{response_text}"
    
def handleTerminate(signum, frame):
    print("Thank you for using GEMINI API")
    sys.exit(0)
        
signal.signal(signal.SIGINT, handleTerminate)

def LLM_geenrated_reult(query, result):
    
    prompt= prompt = f"""You are an advanced AI assistant with access to a knowledge base. Use the provided context to answer the query accurately and concisely.

## Context:
{result} 

## Query:
{query} 

## Instructions:
- Use ONLY the provided context to answer the query.
- If the context does not contain enough information, say "I don't have enough information."
- Provide factual and well-structured responses.
- Do not make up information.

## Answer:
"""

    
    print(f" your prompt to passed in >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n {prompt}")
    
      
    print(TextGeneration(query, prompt))

def QueryEmbedding(query):
    content = " "
    vector_store=Chroma(persist_directory="./chroma_db_nccn", embedding_function=embededQuery)
    result= vector_store.similarity_search(query, 5)
    for doc in result:
        content+= doc.page_content
    
    LLM_geenrated_reult(query, content)
    return content    

while True:
    
    print("\n---------------------------------------------------------------------------------------------------------------------------\n")
    query=input("What is yout Query  : \t")
    result= QueryEmbedding(query)
    print("you output ++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(result)