import streamlit as st
import hashlib

st.title("LinkSphere")

url = st.text_input("Enter URL")

if st.button("Shorten"):
    short = hashlib.md5(url.encode()).hexdigest()[:6]
    st.write("Short URL:", short)
