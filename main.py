import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = init_chat_model(model="llama-3.1-8b-instant", model_provider="groq")
embeddings = GoogleGenerativeAIEmbeddings(model = "models/gemini-embedding-001")

file_path = "faiss_index"


# -------------------------------- Streamlit Code ------------------------------------

st.header("News Research Tool 📈")
st.sidebar.title("News Article URLs")

main_placeholder = st.empty()

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    urls.append(url)

process_url_button = st.sidebar.button("Process URLs")

if process_url_button:

    # Load the data
    loader = UnstructuredURLLoader(urls = urls)
    main_placeholder.text("Data Loading... Started...")
    data = loader.load()

    # Split the data
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    main_placeholder.text("Text Splitter... started...")
    docs = text_splitter.split_documents(data)

    # Create embeddings and save it to FAISS index
    faiss_index = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Documents Started Building...")

    time.sleep(2)

    # Save the FAISS index
    file_path = "faiss_index"
    faiss_index.save_local(file_path)

    main_placeholder.text("✅ Processing Complete! You can now ask questions.")


query = main_placeholder.text_input("Question : ")
if query:
    search_button = st.button("Search")
    if search_button:
        if os.path.exists(file_path):
            faiss_index_loaded = FAISS.load_local(
                file_path,
                embeddings,
                allow_dangerous_deserialization=True
            )

            chain = RetrievalQAWithSourcesChain.from_llm(
                llm = model, 
                retriever = faiss_index_loaded.as_retriever(),
                return_source_documents=True
            )
            response = chain.invoke({"question": query}, return_only_outputs = True)

            st.header("Answer")
            st.write(response["answer"])

            # Display sources if avialable
            sources = response.get("sources", "")
            if sources:
                st.subheader("Sources : ")
                sources_list = sources.split("\n")
                for source in sources_list:
                    st.write(f"- {source}")

        else:
            st.warning("Process the URLs in order to answer the query")