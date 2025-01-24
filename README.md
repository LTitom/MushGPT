Mush GPT

1️⃣ Prerequisites
Ensure you have the following installed on your system:
- Docker
- Docker Compose

2️⃣ Setup
1. Create a .env file
Before running the application, create a .env file in the project's root directory and add your OpenAI API key:
OPENAI_API_KEY=your_openai_api_key_here

2. Start the Application
Use Docker Compose to build and run the application:
docker-compose up --build

3️⃣ Usage
Once the application is running, you can:
- Access the API at: http://localhost:8000
- Query the API using tools like Postman or curl.