import streamlit as st
import platform, hashlib

st.title("📜 VIDURA - System Integrity Checker")

st.write("System Info", platform.uname())

uploaded_file = st.file_uploader("Upload a file to hash (SHA256)")
if uploaded_file:
    data = uploaded_file.read()
    sha = hashlib.sha256(data).hexdigest()
    st.success(f"SHA256: {sha}")