# app.py

import streamlit as st
from rag_system import generate_rag_prompt, get_relevant_context_from_db, generate_answer
from pdf_processing import process_pdf

def main():
    st.title("RAG System with PDF Upload")
    st.write("Ask me anything and I will provide answers based on the context from my database.")

    query = st.text_input("Your Question:")
    if st.button("Get Answer"):
        if query:
            context = get_relevant_context_from_db(query)
            prompt = generate_rag_prompt(query=query, context=context)
            answer = generate_answer(prompt=prompt)
            st.write(answer)
        else:
            st.write("Please enter a question.")

    st.write("Upload a PDF to add new information to the database:")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        process_pdf(uploaded_file)
        st.success("PDF processed and database updated successfully.")

if __name__ == "__main__":
    main()
