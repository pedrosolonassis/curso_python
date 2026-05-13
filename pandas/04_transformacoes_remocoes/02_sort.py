# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")

# Cliente com mais pontos

max_pontos = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_pontos
clientes[filtro]

# %%
# Clientes com mais pontos (top 5)

clientes.sort_values(by="qtdePontos", ascending=False).head(5)

# %%
# Outra maneira

(clientes.sort_values(by="qtdePontos", ascending=False)
            .head(5))

# %%
# Ordenar duas colunas

clientes.sort_values(by=["qtdePontos", "DtCriacao"], ascending=[False, True]).head(5)