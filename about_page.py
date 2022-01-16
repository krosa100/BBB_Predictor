import streamlit as st
from PIL import Image

image = Image.open('img.png')

def show_about_page():
    st.markdown("# :blue_book: About this Project")
    st.write('This is a BBB app.')
    st.image(image,use_column_width=True)