```python
import os
import openai
from typing import Dict

# Shared dependencies
GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
REPO_DATA_SCHEMA = Dict[str, str]  # Define the schema as per your requirements
EMBEDDING_DATA_SCHEMA = Dict[str, str]  # Define the schema as per your requirements

openai.api_key = OPENAI_API_KEY

def extract_github_repo(repo_name: str, api_key: str = GITHUB_API_KEY) -> REPO_DATA_SCHEMA:
    # Implement the function to extract GitHub repo data
    pass

def create_openai_embedding(repo_data: REPO_DATA_SCHEMA, api_key: str = OPENAI_API_KEY) -> EMBEDDING_DATA_SCHEMA:
    # Implement the function to create embeddings using OpenAI model
    pass

if __name__ == "__main__":
    repo_name = "your-repo-name"  # Replace with your repo name
    repo_data = extract_github_repo(repo_name)
    embedding = create_openai_embedding(repo_data)
```
