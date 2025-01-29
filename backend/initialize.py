from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def initialize_resources():
    # Initialize all ressources
    embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory="database", embedding_function=embedding_function)
    model = ChatOpenAI(model_name="gpt-3.5-turbo")
    prompt_template = ChatPromptTemplate.from_template("""
    Vous êtes un assistant environnemental. Répondez de manière précise en vous basant uniquement sur les informations suivantes :

    {context}

    Répondez à la question suivante en utilisant le contexte : {question}. Veuillez répondre dans la langue de la question.
    """)
    return db, model, prompt_template