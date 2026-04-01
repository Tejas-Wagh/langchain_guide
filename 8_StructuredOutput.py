from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

class Actor(BaseModel):
    name:str = Field(description="The name of the actor")
    age:int = Field(description="The age of the actor")

class Movie(BaseModel):
    title:str = Field(description="The title of the movie")
    director:str = Field(description="The director of the movie")
    release_year:int = Field(description="The release year of the movie")
    rating:float = Field(description="The rating of the movie out of 10")
    cast:list[Actor] = Field(description="The cast of the movie")


model = ChatOpenAI(model="gpt-4o-mini")
#keep include_raw=True to get the raw response from the model along with the structured output
model_with_structured_output = model.with_structured_output(Movie, include_raw=True)

response = model_with_structured_output.invoke("Tell me about the tv show Breaking Bad")
print(response)