import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain



# ✅ Use your Gemini API key here
GOOGLE_API_KEY = "AIzaSyCV4wYTTtBkKaUkR-fnHH4-K0PDiIailcw"

# Streamlit UI
st.header("My Internal Chatbot")

with st.sidebar:
    st.title("Upload PDF")
    file = st.file_uploader("Upload a PDF file", type="pdf")

if file is not None:
    # Extract text
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    # Split text
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separators=["\n"],
        length_function=len
    )
    chunks = splitter.split_text(text)

    # Gemini embeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    # FAISS vector store
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)

    # User question
    user_question = st.text_input("Ask a question about the document:")

    if user_question:
        matched_docs = vector_store.similarity_search(user_question)

        # Gemini LLM
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            temperature=0.3,
            google_api_key=GOOGLE_API_KEY
        )

        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=matched_docs, question=user_question)

        st.subheader("Answer:")
        st.write(response)
