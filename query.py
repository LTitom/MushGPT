from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import argparse
import os

# Charge API Key contained in the .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "database"

PROMPT_TEMPLATE = """
Répondez à la question uniquement en vous basant sur le contexte suivant :

{context}

---

Répondez à la question en vous basant sur le contexte ci-dessus : {question}
"""

# Create CLI
def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    return args.query_text

def load_database():
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

def search_database(db, query_text):
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if not results or results[0][1] < 0.5:
        print("Unable to find matching results.")
        return None
    return results

# Formats the prompt using the query and extracted document contents, returning the prompt and document sources.
def create_prompt(query_text, results):
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    sources = [doc.metadata.get("source", None) for doc, _ in results]
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    return prompt_template.format(context=context_text, question=query_text), sources

def generate_response(prompt):
    model = ChatOpenAI(model_name="gpt-3.5-turbo")
    return model.predict(prompt)

def main():
    query_text = argument_parser()
    db = load_database()

    results = search_database(db, query_text)
    if results is None:
        return

    prompt, sources = create_prompt(query_text, results)
    #print(prompt)
    response_text = generate_response(prompt)

    formatted_response = f"{response_text}\nSources: {sources}"
    print(formatted_response)

if __name__ == "__main__":
    main()