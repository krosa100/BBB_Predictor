import streamlit as st

import numpy as np
from sklearn.decomposition import KernelPCA
from rdkit import Chem
from mordred import Calculator, descriptors
from tensorflow.keras.models import load_model
from utility import *

px = from_disk(r'out\model\px')
m = load_model(r'out\model\m')

calc = Calculator(descriptors, ignore_3D=True)
def pred(s):
    '''
    f = select(lambda i : px['smiles'][i] == s, rlen(px['smiles']))
    if False:#f != []:
        return {'type': 'lookup', 'pred': ys[f[0]]}
    '''

    mol = Chem.MolFromSmiles(s)
    xs = np.array([calc(mol)], dtype=float)

    xs1 = xs[:, px['g_inputs']]

    vs = (1 * np.isnan(xs1))[:, px['a']]
    xs2 = np.concatenate([xs1, vs], axis=1)

    xs3 = np.where(np.isnan(xs2), px['cm'], xs2) 

    xs4 = (xs3 - px['m']) / px['s']

    xs5 = px['pca'].transform(xs4)
    prob = m.predict(xs5)[:,0][0]
    return {'type': 'pred', 'prob': prob, 'pred': prob > 0.5}
    r'''
        try:
        pass
    except:
        return {'type': 'error'}
    '''


def show_predict_page():
    st.markdown("# :brain: BBB Permeability Prediction")
    st.write("Enter the SMILES of the molecule of interest. We will predict the probability it passes the BBB.")

    s = st.text_input('SMILES')

    ok = st.button("Predict")
    if ok:
        if s == '':
            st.subheader('Error. Please try again.') 
        else:
            pred_ = pred(s)
            if pred_['type'] == 'error':
                st.subheader('Error. Please try again.') 
            else:
                st.subheader(sf('Probability Permeable: {}', pred_['prob']))
            