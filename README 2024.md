# install
right click extract px.7z.001 to px (then put just the file in the dir)
pyenv install 3.9.13
pyenv shell 3.9.13

python -m venv venv
venv\Scripts\activate.bat
comment out "m = load_model(r'model\m', custom_objects=px['co'])" in pred_m.py
pip install tensorflow==2.10.0 streamlit rdkit matplotlib plotly mordred autokeras==1.0.20

# run
pyenv shell 3.9.13
venv\Scripts\activate.bat
streamlit run app.py
