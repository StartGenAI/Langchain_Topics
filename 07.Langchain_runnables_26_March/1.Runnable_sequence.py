from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()


prompt1=PromptTemplate(
    template="write a detailed report on {topic}"
)

prompt2=PromptTemplate(
    template="Provide a five liner summary on the following {text}"
)

llm=ChatOpenAI(
    model="gpt-4o"
)

parser=StrOutputParser()

runnable=RunnableSequence(prompt1,llm,parser,prompt2,llm,parser)

result=runnable.invoke(
    {
        "topic":"solar Energy"
    }
)

print(result)