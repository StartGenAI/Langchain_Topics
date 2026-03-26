from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv
load_dotenv()

promp1=PromptTemplate(
    template="Create a short note on {topic}"
)

prompt2=PromptTemplate(
    template="create a 3 quiz questions on {topic}"
)

llm= ChatOpenAI(
    model="gpt-4o"
)

parser=StrOutputParser()

parallel_chain=RunnableParallel(
    {
        "notes":RunnableSequence(promp1,llm,parser),
        "quiz":RunnableSequence(prompt2,llm,parser)
    }
)

# result=parallel_chain.invoke(
#     {
#         "topic":"Filter function in python"
#     }
# )

# print("----->",result)

# print("----->",result["notes"])

# print("----->",result["quiz"])

prompt3=PromptTemplate(
    template="combine the below study material into 1 document: \n Notes: {notes} \n Quiz: {quiz}"
)

full_pipeline=RunnableSequence(parallel_chain,prompt3,llm,parser)

result=full_pipeline.invoke({
    "topic":"reduce function in python"
})

print(result)