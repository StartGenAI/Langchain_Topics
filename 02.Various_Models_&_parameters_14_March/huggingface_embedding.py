import os
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

text="Mumbai is the capital of Maharashtra"

vector=embeddings.embed_query(text)

#print(vector)

print(len(vector))

