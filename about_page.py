import streamlit as st
from PIL import Image

image = Image.open('img.png')

def show_about_page():
    st.markdown("# :blue_book: About this Project")
    st.write('This app was built for some purpose and using such and such resources. This app was built for some purpose and using such and such resources.')
    st.image(image,use_column_width=True)