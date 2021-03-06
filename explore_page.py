import streamlit as st

from pandas import read_csv
import plotly.express as px
from utility import from_disk


desc_names = list(from_disk('metad.pickle')['desc_names'])
d = read_csv('data.csv')
def show_explore_page():
    st.markdown("# :mag_right: BBB Dataset Exploration")

    st.write("Select two molecular descriptors. We will plot the molecules in our training set based on the descriptors (x-position, y-position) and whether they are known to pass the BBB (color).")

    xd = st.selectbox("x", desc_names, index=0)
    yd = st.selectbox("y", desc_names, index=1)

    fig = px.scatter(d,
        x=xd,
        y=yd,
        color='passes BBB',
        hover_data=['SMILES']
    )
    fig.update_layout(
        xaxis_title=xd,
        yaxis_title=yd,
    )

    st.write(fig)
    '''
    fig1, ax1 = plt.subplots()
    ax1.axis('equal')
    ax1.scatter(d[xd], d[yd])
    st.pyplot(fig1)
    '''
