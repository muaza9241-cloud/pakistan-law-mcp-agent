import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add root path to system path
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.agent import run_pakistan_law_agent

def main():
    print("=== Pakistan Law AI Assistant (MCP + Agent Demo) ===")
    print("Type your legal query below (or type 'exit' to quit).\n")
    
    while True:
        query = input("Ask about Pakistan Law: ")
        if query.lower() in ["exit", "quit"]:
            print("Exiting assistant. Goodbye!")
            break
            
        if not query.strip():
            continue
            
        print("\nProcessing query...")
        response = run_pakistan_law_agent(query)
        print(f"\nAnswer:\n{response}\n" + "-"*50)

if __name__ == "__main__":
    main()