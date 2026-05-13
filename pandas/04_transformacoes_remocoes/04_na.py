# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
# Removendo as linhas com valores faltantes

clientes.dropna() # Uma view

# %%
 # Considerando apenas as linhas que possuem valores faltantes em todas as colunas

clientes.dropna(how="any")

# %%
# Exemplo:

df = pd.DataFrame(
    {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]
    }
)

df

# %%
# ALL: Todos tem que NA / ANY: Apenas uma

df.dropna(how="all", subset=["idade", "nome"]) # Subset: Lista de colunas a considerar

# %%
# Fill NA: Preencher os valores faltantes, substitui a célula

df["idade"].fillna(0)

# %%
# Preenchendo os valores faltantes de acordo com a coluna

df.fillna({"nome": "alguem", "idade": 0})

# %%
# Preenchendo os valores faltantes com a média da coluna

medias = df[["idade", "salario"]].mean()
df.fillna(medias)