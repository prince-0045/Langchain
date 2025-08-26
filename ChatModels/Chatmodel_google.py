from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() # load env file

# temp and all things are same 
model=ChatGoogleGenerativeAI(model="gemini-pro")
result=model.invoke("what is the captal of India?")
print(result)
