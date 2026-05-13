# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df

# %%

df.info(memory_usage="deep")

# %%

df.dtypes

# %%
# Criar um dataframe novo com a coluna renomeada

renamed_columns = {
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"
}

df.rename(columns=renamed_columns, inplace=True) # inplace=True para modificar o dataframe original
df

# %%
# Acessar duas colunas e retornar um dataframe

colunas = ["IdCliente", "qtPontos"]
df[colunas]

# %%
# SELECT * FROM df

df

# %%
# SELECT idCliente FROM df

df[["IdCliente"]]

# %%
#SELECT idCliente, qtPontos FROM df LIMIT 5

df[["IdCliente", "qtPontos"]].head(5)

# %%

colunas = list(df.columns) # list() para converter o Index em uma lista
colunas.sort() # ordena a lista em ordem alfabética
colunas

df = df[colunas] # reordena as colunas do dataframe
df