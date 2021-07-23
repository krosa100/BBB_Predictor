import streamlit as st

from tensorflow.keras.models import load_model
import numpy as np
from rdkit.ML.Descriptors.MoleculeDescriptors import MolecularDescriptorCalculator
from rdkit.Chem import MolFromSmiles
from utility import mp, sf, from_disk

metad = from_disk('metad.pickle')
desc_names, us, ss = metad['desc_names'], metad['us'], metad['ss']
calculator = MolecularDescriptorCalculator(desc_names)

# repeat code start
def desc_from_s(s):
    mol = MolFromSmiles(s)
    if mol == None: return None
    ds = calculator.CalcDescriptors(mol)
    if np.any(mp(np.isnan, ds)): return None
    return np.array(ds)
# end
m = load_model('model')
def pred_from_desc(desc):
    desc_n = (desc - us) / ss
    return m.predict(np.array([desc_n]))

def pred_from_s(s):
    desc = desc_from_s(s)
    if desc == None: return None
    return pred_from_desc()[0, 1]

def show_predict_page():
    st.markdown("# :brain: BBB Permeability Prediction")
    st.write("Enter the SMILES of the molecule of interest. We will predict the probability it passes the BBB.")

    s = st.text_input('SMILES')

    ok = st.button("Predict")
    if ok:
        if s == '':
            st.subheader('Error. Please try again.') 
        else:
            pred = pred_from_s(s)
            if pred == None:
                st.subheader('Error. Please try again.') 
            else:
                st.subheader(sf('Probability Permeable: {}', pred))
            