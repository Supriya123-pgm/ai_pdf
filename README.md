📄 AI PDF Assistant
About the Project

This project is a simple AI assistant that works with PDF files. You can upload a document, ask questions about it, generate notes, and even see how the system improves its answers step by step.

I built this as part of my internship to understand how real-world AI systems work, especially concepts like retrieval-based answering and iterative improvement.

What It Can Do
Upload any PDF file
Extract and process the content
Answer questions based on the document
Generate short notes from the PDF
Improve answers using feedback (iteration with scoring)

How It Works (Simple Explanation)
You upload a PDF
The system reads and splits it into smaller parts
When you ask a question, it finds the most relevant part
It generates an answer from that content
The answer is evaluated and improved until it reaches a good quality

Tech Used
Python
Streamlit (for UI)
PyPDF2 (for reading PDFs)
Basic RAG logic
Simulated AI model (no API used)

How to Run

Install dependencies:

pip install streamlit PyPDF2

Run the app:

streamlit run app.py
Project Files
app.py        → Main app (UI)
utils.py      → PDF processing
rag.py        → Retrieval logic
fake_llm.py   → Answer generation & improvement

What I Learned
How RAG (Retrieval-Augmented Generation) works
How to structure an AI workflow
How to build interactive apps using Streamlit
Importance of iterative improvement in AI responses

Future Improvements
Use real AI APIs (like OpenAI)
Add better search using embeddings
Improve UI design
Deploy the app online
