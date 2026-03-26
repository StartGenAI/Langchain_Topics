from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnablePassthrough,RunnableParallel
from dotenv import load_dotenv
load_dotenv()

def word_count(text):
    return len(text.split())

prompt=PromptTemplate(
    template="write a report on {topic}"
)

llm=ChatOpenAI(
    model="gpt-4o"
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        "report":RunnablePassthrough(),
        "word_count":RunnableLambda(word_count)
    }
)

final_chain=prompt|llm|parser|parallel_chain

result=final_chain.invoke({
    "topic":"cliamte change"
})

print(result)