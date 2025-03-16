# importing required libraries
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

# loading the ollama model
ollama_model = Ollama(model="tinyllama")

# creating the fastapi app
app = FastAPI(
    title="Poem Generator App",
    description="A simple chat app using LangChain and FastAPI",
    version="1.0.0",
)

# writing the prompt
prompt = ChatPromptTemplate.from_template("Write a poem about the {topic} in 1 stanza.")

# Pydantic model for input validation
class PoemInput(BaseModel):
    topic: str

# Pydantic model for output
class PoemOutput(BaseModel):
    output: str

@app.post("/poem/invoke", response_model=PoemOutput)
async def invoke(input_data: PoemInput):
    chain = prompt | ollama_model
    result = chain.invoke({"topic": input_data.topic})  # Ensure correct dict format
    print("Generated result:", result)  # Debugging
    return PoemOutput(output=result)

# driver code
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)