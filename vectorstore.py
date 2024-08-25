# vectorstore.py

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import MODEL_NAME, PERSIST_DIRECTORY

# Initialize embedding function and vector store
def initialize_vectorstore():
    embedding_function = HuggingFaceEmbeddings(model_name=MODEL_NAME, model_kwargs={'device': 'cpu'})
    vectorstore = Chroma(persist_directory=PERSIST_DIRECTORY, embedding_function=embedding_function)
    return vectorstore
