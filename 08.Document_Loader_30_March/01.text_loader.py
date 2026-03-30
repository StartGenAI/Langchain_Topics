from langchain_community.document_loaders import TextLoader

file=TextLoader("doc1.txt",encoding="utf-8")

document=file.load()

print(len(document))
print(document[0].page_content)

print(document[0].metadata)
