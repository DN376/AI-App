import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from googletrans import Translator, constants
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def main():

    st.set_page_config(page_title="Analyze / Translate Document",
                       page_icon="💻")
    st.header("Analyze / Translate Document 💻")

    
    with st.sidebar:
        st.subheader("Your documents")
        docs = st.file_uploader(
            "Upload your documents here!", accept_multiple_files=True)
    # i = 1
    # for doc in docs:
    #     st.write("File " + str(i) + ": *" + doc.name + "*")
    #     stringio = StringIO(doc.getvalue().decode("utf-8"))
    #     string_data = stringio.read()
    #     st.write(string_data)
    #     st.write("------\n")
    #     i += 1
    
    st.write('**What language would you like to translate these documents into?**')
    language = st.text_input('Choose a language').lower()
    if not validLang(language):
        st.write("Invalid language!")
    else:
        if docs is not None:
            if st.button("Translate Into "+ language.title() +"!"):
                # init the Google API translator
                files = []
                translator = Translator()
                for doc in docs:
                    st.write("Translation of File: **" + doc.name + "**")
                    text = doc.getvalue().decode("utf-8")
                    translation = translator.translate(text, dest=language)
                    newName = language + "_" + doc.name
                    st.write(translation.text)
                    st.download_button(label="Download Translation of " + doc.name, data=translation.text, file_name=newName)
                    st.write("------\n")
                

def validLang(lang):
    if lang is None:
        return False
    langNames = constants.LANGUAGES.values()
    for langName in langNames:
        if lang == langName:
            return True
    return False


main()