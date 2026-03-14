import os
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=800
)

text="Mumbai is the capital of Maharashtra"

vector=embeddings.embed_query(text)

#print(vector)

print(len(vector))

