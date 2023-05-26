import streamlit as st
from annotated_text import annotated_text



def main():

    st.title("Kidz Bopify")
    # Using object notation
    selectbox = st.sidebar.selectbox(
    "Choose An Algorithm to clean-edit your lyrics",
    ("N-grams", "Transformer","Semantic Simlarity"))
    # User input
    corpus = st.text_area("Enter your unclean song lyrics here:", height=200)
    flagged_words = st.text_input("Enter the flagged words (separated by commas):")
    flagged_words = [word.strip() for word in flagged_words.split(",") if word.strip()]


    tuple_set = []
    for word in corpus.split():
        word_attributes = []
        word_attributes.append(word)
        if word in flagged_words:
            word_attributes.append("explicit")
            word_attributes.append("#8b0000")
        else:
            word_attributes.append("")
            word_attributes.append("#5A5A5A")

        tuple_set.append(tuple(word_attributes))
    annotated_text(*tuple(tuple_set))


if __name__ == "__main__":
    main()
