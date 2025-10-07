# 📈 News Research Tool

A Streamlit-based application that enables users to analyze and query multiple news articles using AI. It allows users to ask questions about the content in these websites.

## Features
- **URL Processing**: Load and process up to 3 news article URLs simultaneously
- **Vector Embeddings**: Used Google's Gemini embeddings for documents.
- **FAISS Vector Store**: Efficient similarity search using Facebook AI Similarity Search
- **Question Answering**: Ask questions about the articles and get answers
- **Persistent Storage**: Saves embeddings locally for quick subsequent queries

## Getting Started

### Prerequisites
- Groq API key (for any LLM)
- Google API key (for Gemini embeddings)

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/sudharshanreddyt/news_research_assistant.git
    cd news_research_assistant
    ```

2. **Create and activate virtual environment**
    ```bash
    python -m venv .venv
   
    # On Windows
    .venv\Scripts\activate
   
    # On macOS/Linux
    source .venv/bin/activate 
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**
    Create a .env file in the project root:
    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    GOOGLE_API_KEY=your_google_api_key_here
    ```

    Getting API Keys:
    Groq API: Sign up at console.groq.com
    Google API: Get your key from Google AI Studio


### Running the Application
    ```bash
    streamlit run main.py
    ```

    The application will open in your default web browser at http://localhost:8501

### Step-by-Step Guide

1. Enter News URLs
    - Use the sidebar to input up to 3 news article URLs
    - Paste complete URLs (e.g., https://example.com/article)

2. Process URLs
    - Click the "Process URLs" button
    - Wait for the application to:
        - Load article content
        - Split text into chunks
        - Create embeddings
        - Save to FAISS index

3. Ask Questions
- Enter your question in the text input field
- Click "Search" to get answers
- View the answer


### Sample URLS:
- https://www.alphaspread.com/market-news/regulatory-actions/apple-urges-eu-to-rethink-digital-competition-law
- https://9to5mac.com/2025/10/01/apple-will-launch-5-new-products-in-october-heres-whats-coming/
- https://www.macrumors.com/2025/10/03/iphone-18-not-expected-next-year/

### Query
What new Apple products will be launched in October ?

### Example Output
![alt text](/outputs/image.png)