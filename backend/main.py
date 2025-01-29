from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from loader import setup_database  
from query import make_query
from initialize import initialize_resources
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is loaded correctly
if not openai_api_key:
    raise ValueError("The OPENAI_API_KEY is not defined in the .env file.")

# Define the request format for the JSON payload
class QueryRequest(BaseModel):
    query_text: str

# Initialize FastAPI application
app = FastAPI()

# Initialize resources only once when the application starts
@app.on_event("startup")
async def startup_event():
    setup_database()  # Function that handles database setup, if needed
    global db, model, prompt_template
    db, model, prompt_template = initialize_resources()  # Initialize necessary resources (DB, model, prompt)

# POST endpoint to handle search queries
@app.post("/query/")
async def query(request: QueryRequest):
    query_text = request.query_text
    formatted_response = make_query(query_text, db, model, prompt_template)
    return {"response": formatted_response}
