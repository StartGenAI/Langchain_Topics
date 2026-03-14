import os
from langchain_openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv

load_dotenv()

embeddings=OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=800
)

docs = [
    "Mumbai is the capital of Maharashtra",
    "virat kohli is good cricketer",
    "Narendra modi is PM of our country"
]

docs_vector=embeddings.embed_documents(docs)

#print(vector)
#print(vector[2])
# [[1],[2],[3]]

query="what is the capital of maharashtra? "

query_vector=embeddings.embed_query(query)

scores=cosine_similarity([query_vector],docs_vector)[0]

print(scores)