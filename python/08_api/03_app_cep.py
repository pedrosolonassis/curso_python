# %%
import streamlit as st
import pandas as pd
import requests

url = "https://viacep.com.br/ws/{cep}/json/"

st.title("Consulta de CEP")

cep_input = st.text_input("Digite o CEP (apenas números):")

if cep_input != "":
    resp = requests.get(url.format(cep=cep_input))
    if resp.status_code == 200:
        dados = resp.json()
        data = pd.DataFrame([resp.json()])
        st.dataframe(data)
        st.write("Informações do CEP:")
        st.write(f"CEP: {dados.get('cep', 'N/A')}")
        st.write(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        st.write(f"Bairro: {dados.get('bairro', 'N/A')}")
        st.write(f"Cidade: {dados.get('localidade', 'N/A')}")
        st.write(f"Estado: {dados.get('uf', 'N/A')}")
    else:
        st.error("Erro na consulta. Verifique o CEP e tente novamente.")