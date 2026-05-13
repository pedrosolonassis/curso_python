# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")

# %%
# Converter o tipo da coluna

df["qtdePontos"].astype(float)

# %%
# Mudar a data de criação (replace)

df["DtCriacao"].replace(("0000-00-00 00:00:00.000", "2024-02-01 09:00:00.000"), inplace=True)

# %%
# Converter a coluna de data para o tipo datetime

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"], format="%Y-%m-%d %H:%M:%S.%f")

# %%
# Extrair o ano da data de criação

df["DtCriacao"].dt.year