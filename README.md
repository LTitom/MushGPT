# MushGPT

MushGPT is an AI-powered chatbot designed to answer environmental and ecological questions using Retrieval-Augmented Generation (RAG) technology and the OpenAI API (currently utilizing GPT-3.5-turbo). The primary objective is to provide accurate and cost-effective responses based on verified data.

---

## Features
- **RAG-Based Response System**: Ensures answers are grounded in reliable, domain-specific knowledge.
- **FastAPI Backend**: Provides a lightweight and efficient API for query handling.
- **Vite + React Frontend**: Offers a responsive and user-friendly interface.
- **Docker Deployment**: Easily deployable using Docker and Docker Compose.

---

## How It Works
1. **User Query Submission**: Users input environmental or ecological questions via the frontend.
2. **Processing in FastAPI**:
   - The query is received and formatted.
   - The system interacts with a structured database using `langchain` to retrieve relevant information.
   - The OpenAI API (GPT-3.5-turbo) processes the query using predefined prompt templates.
3. **Response Generation**: The chatbot returns a concise and informative response based on the retrieved knowledge.

---

## Project Structure
- **Backend**: FastAPI application handling API requests and responses.
- **Frontend**: Vite + React-based UI for user interaction.
- **Database**: Stores verified environmental data used for augmenting chatbot responses.
- **Docker Integration**: Simplifies setup and deployment.

---

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- **Docker**

### Steps to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/MushGPT.git
   cd MushGPT
   ```
2. Create a `.env` file in the root directory and add your OpenAI API key:
   ```sh
   OPENAI_API_KEY=your_api_key_here
   ```
   If you don’t have an OpenAI API key, follow the official guide here: [How to get an OpenAI API Key](https://platform.openai.com/docs/quickstart).
3. Build and launch the project using Docker:
   ```sh
   docker compose up --build
   ```

The application will be available at `http://localhost:8000` (API) and the frontend at `http://localhost:5173`.

---

## API Endpoints
- `POST /query/`
  - **Description**: Accepts a JSON payload with a user query and returns an AI-generated response.
  - **Request Format**:
    ```json
    {
      "query_text": "How is human activity affecting the marine ecosystems?"
    }
    ```
  - **Response Format**:
    ```json
    {
      "response": "Human activity is affecting marine ecosystems by causing pollution, overfishing, and ocean acidification. [...]"
    }
    ```

---

## Contact
For any inquiries, please reach out via GitHub Issues or email at [thomas.gillet@efrei.net].

