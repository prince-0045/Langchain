from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # load env file

# create instance of LLM
llm=OpenAI(model="gpt-3.5-turbo-instruct")

# invoke method ni help we can compunicate with LLM
result=llm.invoke("what is the captal of India?")
print(result)

