from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

def make_query(query_text, db, model, prompt_template):
    # Search the database for the query
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if not results or results[0][1] < 0.3:
        return {"error": "Unable to find matching results."}

    # Format the prompt and generate a response
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
    prompt = prompt_template.format(context=context_text, question=query_text)
    response = model.invoke([prompt])
    response_text = response.content

    # Collect and process the sources
    sources = {os.path.splitext(os.path.basename(doc.metadata.get("source", "")))[0] for doc, _ in results}

    return f"{response_text}\n\nSources: {sources}"