import streamlit as st
import tempfile
import os

from parsers.txt_parser import parse_txt
from parsers.csv_parser import parse_csv
from parsers.json_parser import parse_json


st.title("📄 File Parser")

uploaded_file = st.file_uploader("Choose a file", type=["txt", "csv", "json"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension == "txt":
        result = parse_txt(tmp_path)
    elif extension == "csv":
        result = parse_csv(tmp_path)
    elif extension == "json":
        result = parse_json(tmp_path)

    st.success(f"File '{uploaded_file.name}' parsed successfully!")
    
    st.subheader("File Summary")
    for key, value in result.items():
        st.metric(label=key.upper(), value=value)

    os.unlink(tmp_path)
