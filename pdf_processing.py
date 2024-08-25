# pdf_processing.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from vectorstore import initialize_vectorstore

def process_pdf(file):
    loaders = [PyPDFLoader(file)]
    docs = []
    for loader in loaders:
        docs.extend(loader.load())
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(docs)
    vectorstore = initialize_vectorstore()
    vectorstore.add_documents(docs)  # Add the new documents to the vector store
    vectorstore.persist()  # Save changes to disk
