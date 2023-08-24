import streamlit as st
from io import StringIO
from langchain.schema import Document
from langchain.document_transformers import DoctranTextTranslator

def main():
    st.set_page_config(page_title="Analyze / Translate Document",
                       page_icon="💻")
    st.header("Analyze / Translate Document 💻")

    
    with st.sidebar:
        st.subheader("Your documents")
        docs = st.file_uploader(
            "Upload your documents here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                print("done!")
                # st.text(docs)
                # To convert to a string based IO:
                # for doc in docs:
                #     st.text()
                #     stringio = StringIO(doc.getvalue().decode("utf-8"))
                #     st.write(stringio)
    i = 1
    for doc in docs:
        st.write("File " + str(i) + ": *" + doc.name + "*")
        stringio = StringIO(doc.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)
        st.write("------\n")
        i += 1
    
    # st.write('**What language would you like to translate these documents into?**')
    # language = st.text_input('Choose a language')
    # if language is not None:
    #     if st.button("Translate!"):

main()