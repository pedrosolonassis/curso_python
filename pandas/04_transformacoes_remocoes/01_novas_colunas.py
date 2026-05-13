# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

# %%
# Criação de uma nova coluna. Adiconar 100 pontos para cada cliente

df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%
# Em python puro

nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i + 100)
nova_coluna

# %%
# Criar uma nova coluna com a concatenação de email e twitch

df["emailTwitch"] = df["flEmail"] + df["flTwitch"] # Pode ser com *
df.head()

# %%
# Quantas redes sociais cada cliente tem registrado?

df["qtdeRedesSociais"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()

# %%
# Clientes que tem todas as redes sociais

df["todasRedes"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()

# %%
# Transformação logarítmica da coluna qtdePontos

df["logPontos"] = np.log(df["qtdePontos"] + 1) # Somar 1 para evitar log(0)
df["logPontos"].describe()

# %%
# Histograma da coluna logPontos com matplotlib

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()

# %%
