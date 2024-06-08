import streamlit as st
from pred_m import pred_from_s

def roundf(f, n=2):
    d = rep('{:.$n$f}', {'$n$': n})
    return d.format(f)

def show_predict_page():
    st.markdown("# :brain: BBB Permeability Prediction")
    st.write("Enter the SMILES of the molecule of interest. This tool will predict the probability it passes the BBB.")

    s = st.text_input('SMILES')

    ok = st.button("Predict")
    if ok:
        if s == '':
            st.subheader('Error. Please try again.') 
        else:
            pred = pred_from_s(s)
            if pred['type'] == 'error':
                st.subheader('Error. Please try again.') 
            if pred['type'] == 'pred':
                st.subheader('Probability Permeable: {:.4f}'.format(pred['prob']))