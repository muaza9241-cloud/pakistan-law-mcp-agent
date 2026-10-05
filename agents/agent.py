from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

def run_pakistan_law_agent(query: str):
    """Simple agent runner using Local Ollama (Llama 3)."""
    
    llm = ChatOllama(
        model="llama3",
        temperature=0.1
    )
    
    prompt = f"""You are a helpful legal assistant specializing in Pakistan Law. 
    Answer the user's question clearly and accurately.
    
    User Question: {query}
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content