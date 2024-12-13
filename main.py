import streamlit as st
from delete_codes import process_excel_column_a

st.title("Обробка Excel-файлу зі стовпчиком A")

uploaded_file = st.file_uploader("Завантажте файл Excel", type=["xlsx", "xls"])

if uploaded_file is not None:
    st.write("**Значення зі стовпчика A:**")
    values = process_excel_column_a(uploaded_file)
    for value in values:
        st.write(value)
