```python
import os
import requests
from typing import Dict

GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")

def extract_github_repo(repo_name: str) -> Dict:
    """
    Function to extract GitHub repository data using GitHub API.
    """
    headers = {"Authorization": f"token {GITHUB_API_KEY}"}
    response = requests.get(f"https://api.github.com/repos/{repo_name}", headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Error with status code: {response.status_code}")
    
    repo_data = response.json()
    
    # Define the Repo Data Schema
    repo_data_schema = {
        "id": repo_data.get("id"),
        "name": repo_data.get("name"),
        "full_name": repo_data.get("full_name"),
        "description": repo_data.get("description"),
        "created_at": repo_data.get("created_at"),
        "updated_at": repo_data.get("updated_at"),
        "pushed_at": repo_data.get("pushed_at"),
        "size": repo_data.get("size"),
        "stargazers_count": repo_data.get("stargazers_count"),
        "watchers_count": repo_data.get("watchers_count"),
        "language": repo_data.get("language"),
        "forks_count": repo_data.get("forks_count"),
        "open_issues_count": repo_data.get("open_issues_count"),
        "license": repo_data.get("license"),
        "score": repo_data.get("score"),
    }
    
    return repo_data_schema
```