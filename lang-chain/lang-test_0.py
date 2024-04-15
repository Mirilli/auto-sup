from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key)

messages = [
    HumanMessage(content="oi como você está?"),
    AIMessage(content="Estou bem e você?"),
    HumanMessage(content="o que eu acabei de te falar?")
]

result = chat_model.invoke(messages)
print(result)