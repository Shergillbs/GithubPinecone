from setuptools import setup, find_packages

setup(
    name='github_openai_pinecone',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'jupyter',
        'github3.py',
        'openai',
        'pinecone-io',
    ],
    entry_points={
        'console_scripts': [
            'extract_github_repo=src.github_repo_extractor:extract_github_repo',
            'create_openai_embedding=src.openai_embedding_creator:create_openai_embedding',
            'upsert_to_pinecone=src.pinecone_upserter:upsert_to_pinecone',
        ],
    },
    python_requires='>=3.6',
)