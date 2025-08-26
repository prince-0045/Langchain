# console.anthropic.com par api key we find
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv() # load env file
#we have to purchase anthropic api key😒😒😒

#create instance of ChatAnthropic
#we can select temperature ,max_completion_tokens etc
model=ChatAnthropic(model="claude-2")
result=model.invoke("what is the captal of India?") 
print(result)