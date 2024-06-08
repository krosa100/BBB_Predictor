import streamlit as st

import pandas as pd
import plotly.express as px

from pred_m import px as px2

desc_names = list(px2['descs'])
d = pd.DataFrame(px2['xs'], columns=px2['descs'])
d['passes BBB'] = px2['ys']
d['SMILES'] = px2['smiles']

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
