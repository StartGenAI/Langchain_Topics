import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=800
)

docs = [
    "New Delhi is the capital of India",
    "New York is the capital of America",
    "Bezing is the capital of China"
]

vector=embeddings.embed_documents(docs)

#print(vector)

print(vector[2])

# [[1],[2],[3]]

