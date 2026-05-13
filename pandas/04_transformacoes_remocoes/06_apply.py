# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()

# %%

idCliente = "000dc0f6-e4f2-4a42-b8cd-b586ed1c709a"

def get_last_id(x):
    return idCliente.split("-")[-1]

# %%

get_last_id("001749bd-37b5-4b1e-8111-f9fbba90f530")

# %%
# Python puro

id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()

# %%
# Com apply: Rodar a função para cada linha da coluna
df["idCliente"].apply(get_last_id)