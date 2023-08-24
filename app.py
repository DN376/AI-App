import streamlit as st
from io import StringIO

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
    for doc in docs:
        stringio = StringIO(doc.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

main()