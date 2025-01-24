from fastapi import FastAPI
from pydantic import BaseModel
import subprocess
import os

# Define a class for the JSON request format
class QueryRequest(BaseModel):
    query_text: str

# Initialize FastAPI
app = FastAPI()

# Function to execute loader.py when the server starts
def run_loader():
    try:
        subprocess.run(["python", "loader.py"], check=True)
        print("Loader script executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error when executing loader.py: {e}")

# Run loader.py on server startup
@app.on_event("startup")
async def startup_event():
    run_loader()

# POST route to handle search requests
@app.post("/query/")
async def query(request: QueryRequest):
    query_text = request.query_text
    
    # Execute the query.py script with the query text
    try:
        result = subprocess.run(
            ["python", "query.py", query_text],
            capture_output=True,
            text=True,
            check=True
        )
        response = result.stdout.strip()  # Extract the response from the standard output
        return {"response": response}
    except subprocess.CalledProcessError as e:
        return {"error": f"Error when executing query.py: {e}"}
