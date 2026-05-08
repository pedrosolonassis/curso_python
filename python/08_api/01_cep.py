# %%

import requests # para realizar as requisições HTTP
import json # para tratar listas e dicionários para arquivos JSON
from tqdm import tqdm # para mostrar o progresso das requisições
import pandas as pd # para tratar os dados em DataFrames

ceps_estadios = {
    "Maracanã": "20271-110",
    "MorumBIS": "05653-070",
    "Neo Química Arena": "08295-005",
    "Allianz Parque": "05001-200",
    "Mineirão": "31275-000",
    "Beira-Rio": "90810-240",
    "Arena do Grêmio": "90250-557",
    "Arena Fonte Nova": "40050-565",
    "Castelão": "60861-211",
    "Arena da Amazônia": "69050-001",
    "Arena Pantanal": "78048-230",
    "Mané Garrincha": "70070-701",
    "Almeidão": "58088-300"
}

url = "https://viacep.com.br/ws/{cep}/json/"
dados = []

for i in tqdm(ceps_estadios):
    resposta = requests.get(url.format(cep=ceps_estadios[i]))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados


# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps_estadios.csv", sep=";", index=False)

# %%
with open("ceps_estadios.json", "w") as f:
    json.dump(dados, f, indent=4)

# %%
