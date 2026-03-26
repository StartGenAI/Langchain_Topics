from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

prompt1=PromptTemplate(
    template="provide 5 liner report on {topic}"
)

prompt2=PromptTemplate(
    template="Summarize the following text /n {text}"
)

llm=ChatOpenAI(
    model="gpt-4o"
)

parser=StrOutputParser()

branch_chain=RunnableBranch(
    (lambda a: len(a.split())>300, prompt2|llm|parser),
    RunnablePassthrough()
)

# final_chain=RunnableSequence(report_chain,branch_chain)

final_chain=prompt1 | llm |parser|branch_chain

result=final_chain.invoke({
    "topic":"climate change"
})

print(result)

