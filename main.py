import textwrap
import streamlit as st
import PyPDF2
from pdfParser import parse_pdf
from AI_summariser import summariser
from chatDoc import create_db
from chatDoc import ans_query
from research_summariser import summarise_research_paper

st.title('Chat with Documents')

uploaded_file = st.file_uploader('Choose a PDF file', type='pdf')



if st.button("summarise") and uploaded_file is not None:
    content = parse_pdf(uploaded_file)
    # Display the extracted text
    # st.write('**Research Summary Generated**')
    research_summary = summarise_research_paper(content)
    st.text_area(label = "Summary generated : ",value=research_summary, height=100)

st.subheader("Ask your Document")
ques = st.text_area(label = "Enter your question")

if st.button("Ask Away") and uploaded_file is not None:
    content = parse_pdf(uploaded_file)
    db = create_db(content)
    result, result_reference = ans_query(db,ques)
    st.subheader("Answer: ")
    st.write(result)
    st.subheader("Reference: ")
    st.write(result_reference)





st.title("Summarise with AI")

var = st.text_input(label="Enter your text here")

if st.button("Summarise") and var is not None:
    st.subheader("Summary Generated : ")
    summarisedText = summariser(var)
    st.write(summarisedText)



