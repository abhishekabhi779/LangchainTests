from dotenv import load_dotenv
from langchain_openai import ChatOpenAI  # Note we're using ChatOpenAI here
from langchain.prompts import PromptTemplate
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    api_key=openai_api_key,
    temperature=0.7,
    model="gpt-4o-mini"  # Using a valid model name
)

template = """You are the most advance AI model. you are the smartest Ape 🦍 . Ape together stronk. you will do anything for bananums. answer the questions for the king ape.
 remember kinng ape will give bananums if you provide correct answers.
Question: {question}
Answer:"""

prompt = PromptTemplate(input_variables=["question"], template=template)

question = "how to  build simple llm agents?"
formatted_prompt = prompt.format(question=question)

response = llm.invoke(formatted_prompt)
print(response.content)