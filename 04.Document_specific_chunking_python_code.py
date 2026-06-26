from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

python_text="""
class DataProcessor:
    def __init__(self, source_file):
        self.source = source_file
        self.records = []
    
    def load_data(self):
        return pd.read_csv(self.source)
    
    def validate_records(self):
        return len(self.records) > 0

"""
text_splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=80,
    chunk_overlap=0
)

docs=text_splitter.split_text(python_text)

print(len(docs))

print("chunk--->",docs[0])

print("chunk--->",docs[1])

print("chunk--->",docs[2])