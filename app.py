import streamlit as st
from utils import extract_text, chunk_text
from rag import retrieve
from fake_llm import answer_question, generate_notes, evaluate, improve

# ✅ ALWAYS VISIBLE
st.title("📄 AI PDF Assistant")
st.write("Upload a PDF and ask questions!")

# -------- Upload PDF --------
pdf = st.file_uploader("Upload PDF", type="pdf")

# 👉 Initialize empty variables
chunks = None

# -------- PROCESS PDF --------
if pdf:
    text = extract_text(pdf)
    chunks = chunk_text(text)

    st.success("PDF processed successfully!")

# -------- QUESTION INPUT (OUTSIDE) --------
query = st.text_input("Ask a question:")

# -------- ANSWER BUTTON --------
if st.button("Get Answer"):

    if not pdf:
        st.error("⚠️ Please upload a PDF first!")
    
    elif not query:
        st.error("⚠️ Please enter a question!")
    
    else:
        context = retrieve(query, chunks)
        answer = answer_question(context, query)

        iteration = 1
        
        while True:
            score, feedback = evaluate(answer)
            
            st.write(f"Iteration {iteration} | Score: {score}")
            st.write("Answer:", answer)
            
            if score >= 8 or iteration >= 3:
                break
            
            answer = improve(answer, feedback)
            iteration += 1

        st.success("Final Answer Ready!")

# -------- NOTES BUTTON --------
if st.button("Generate Notes"):

    if not pdf:
        st.error("⚠️ Please upload a PDF first!")
    else:
        notes = generate_notes(chunks)
        st.text_area("Notes", notes, height=200)