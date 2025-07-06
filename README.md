✅ Step 1: Open Your Project in PyCharm
Make sure your project folder is open in PyCharm.

✅ Step 2: Create the README.md File
In the Project panel (usually on the left), right-click on your root project folder (e.g., Pdfchatbot).

Select New → File

Type README.md as the file name and click OK.

✅ Step 3: Write the Project Description
Once the file opens, paste this sample content below, or edit as per your needs:

# 📄 Gemini PDF Chatbot using LangChain & Streamlit

This project is a chatbot app that lets users upload a PDF file and ask natural language questions about its content. It uses **Google Gemini API**, **LangChain**, and **Streamlit** to deliver intelligent responses directly from the PDF.


## 🚀 Features
- Upload and read PDF documents
- Chunk PDF text for better processing
- Use FAISS vector search to find contextually relevant chunks
- Ask questions and get answers powered by Gemini LLM
- Built using LangChain, Streamlit, and Google Generative AI


## 🛠️ Tech Stack
- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Google Gemini API](https://ai.google.dev/)
- PyPDF2 for PDF parsing


## ✅ How to Run This Project

1. Make sure your API key is set inside the `chatboat.py` file.
2. Install required libraries using pip.
3. Run the app using:

streamlit run chatboat.py

Upload a PDF and start asking questions!

📦 Sample requirements.txt
nginx
Copy
Edit
streamlit
PyPDF2
langchain
faiss-cpu
google-generativeai
sentence-transformers

📌 Note

This app currently uses Gemini-1.5 model, which may require billing enabled if you're beyond the free tier.

Make sure your PDF is text-based, not scanned images.


🌐 License
This project is open source and available under the MIT License.


