import streamlit as st
from PIL import Image

image = Image.open('img.png')

def show_about_page():
    st.markdown("# :blue_book: About this Project")
    st.write('This app was built to predict molecular passage across the blood-brain barrier.')
    #old code for image: st.image(image,use_column_width=True)
        #   figure out how to put in images to site 
