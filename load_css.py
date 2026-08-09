import streamlit as st

def load_css():
    try:
        with open("assets/style.css", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("File style.css tidak ditemukan.")