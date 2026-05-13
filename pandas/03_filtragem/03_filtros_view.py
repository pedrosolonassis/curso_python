# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes.head()

# %%
# Determinar a variavel
filtro = clientes["qtdePontos"] == 0
clientes_0 = clientes[filtro]
clientes_0.head()

# %%
# Criação de uma View para os clientes com 0 pontos

filtro = clientes["qtdePontos"] == 0
cliente_0 = clientes[filtro]
clientes_0["flag_1"] = 1
clientes_0

# %%
# Para criar uma copia, basta colocar .copy() no final da linha

filtro = clientes["qtdePontos"] == 0
cliente_0 = clientes[filtro].copy()
clientes_0["flag_1"] = 1
clientes_0