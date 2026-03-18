from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import (
    SystemMessage, HumanMessage, AIMessage
)
from langchain_openai import ChatOpenAI

ai_bot = ChatOpenAI()

# Build an initial conversation with context
dialogue = [
    SystemMessage(content="You are a helpful AI tutor"),
    HumanMessage(content="Tell me about LangChain"),
    AIMessage(content="LangChain is a framework for "
              "building LLM-powered applications..."),
    HumanMessage(content="What are its key features?"),
]

# Send full typed history to LLM
response = ai_bot.invoke(dialogue)

# Store response with its label
dialogue.append(AIMessage(content=response.content))

print(dialogue)   # All messages properly labelled!