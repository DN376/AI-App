import streamlit as st
from io import StringIO
from langchain.schema import Document
from googletrans import Translator, constants

def main():
    st.set_page_config(page_title="Analyze / Translate Document",
                       page_icon="💻")
    st.header("Analyze / Translate Document 💻")

    
    with st.sidebar:
        st.subheader("Your documents")
        docs = st.file_uploader(
            "Upload your documents here!", accept_multiple_files=True)
    i = 1
    for doc in docs:
        st.write("File " + str(i) + ": *" + doc.name + "*")
        stringio = StringIO(doc.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)
        st.write("------\n")
        i += 1
    
    st.write('**What language would you like to translate these documents into?**')
    language = st.text_input('Choose a language').lower()
    if not validLang(language):
        st.write("Invalid language!")
    else:
        if docs is not None:
            if st.button("Translate into "+ language +"!"):
                i = 1
                # init the Google API translator
                translator = Translator()
                for doc in docs:
                    st.write("Translated File " + str(i) + ": *" + doc.name + "*")
                    text = doc.getvalue().decode("utf-8")
                    translation = translator.translate(text, dest=language)
                    st.write(translation.text)
                    st.write("------\n")
                    i += 1

def validLang(lang):
    if lang is None:
        return False
    langNames = constants.LANGUAGES.values()
    for langName in langNames:
        if lang == langName:
            return True
    return False


main()