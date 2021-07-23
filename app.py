import streamlit as st

st.set_page_config('BBB Predictor',':brain:')


from predict_page import show_predict_page
from explore_page import show_explore_page
from about_page import show_about_page

page = st.sidebar.selectbox("Page", ("Predict", "Explore", "About"))

if page == "Predict":
    show_predict_page()
elif page == 'About':
    show_about_page()
else:
    show_explore_page()