```python
import pinecone
import os

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
pinecone.init(api_key=PINECONE_API_KEY)

def upsert_to_pinecone(data, index_name):
    """
    Function to upsert data to Pinecone
    :param data: data to be upserted
    :param index_name: name of the Pinecone index
    :return: None
    """
    upsert_data = {item['id']: item['vector'] for item in data}
    pinecone.de_index(index_name).upsert(items=upsert_data)

if __name__ == "__main__":
    # Assuming data is in the format of Upsert Data Schema
    data = [{"id": "repo1", "vector": [0.1, 0.2, 0.3]}, {"id": "repo2", "vector": [0.4, 0.5, 0.6]}]
    index_name = "github-repo-embeddings"
    upsert_to_pinecone(data, index_name)
```