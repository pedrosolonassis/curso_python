# %%

import pandas as pd

# %%
# Em python puro, para filtrar os valores maiores ou iguais a 50

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]

valores_50_mais = []
for i in pontos:
    if i >= 50:
        valores_50_mais.append(i)
valores_50_mais

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
filtro = []

valores_50_mais = []
for i in pontos:
        filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
resultado

# %%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     }
)

filtro = brinquedo["idade"] >= 18
brinquedo[filtro]

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# %%

filtro = df["QtdePontos"] >= 50
df[filtro]

# %%
# O & é o operador lógico "E" e o | é o operador lógico "OU" no Pandas

filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] >= 100)
df[filtro]

# %%

filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

# %%
# Pontos entre 0 e 50 ou do ano de 2025 em diante

filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"] <= 50) | (df["DtCriacao"] >= "2025-01-01")
df[filtro]

# %%
