from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv() # load env file
#we have to purchase openai api key😒😒😒

# model we can see in platform.openai.com which openai supports
# we can improve our model performance by changing temperature
# temp value -> 0 to 2 ma lie kare
# temp=0 -> more deterministic output
# temp=2 -> more creative output
#one other parameter->
#max_completion_tokens -> max token ni limit set kare

#ChatOpenAI(model,temperature,max_completion_tokens)
model=ChatOpenAI(model="gpt-4")
result=model.invoke("what is the captal of India?")
print(result)
#now result is not same as LLMS 
#format of output in langchain
#content=actual answer contain
#additional_kwargs=token ni all info store thayeli che


#so only result jovu hoy then then we only fetch content from result
print(result.content)