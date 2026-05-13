# %%

import pandas as pd

# %%
# Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes["twitch_points"] = clientes["qtdePontos"] * clientes["twitch"]

# %%
# Aplique o log na coluna de saldo de pontos, criando uma coluna nova



# %%
# Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.


# %%
# Qual é o id de cliente que tem maior saldo de pontos? E o menor?

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.sort_values(by="qtdePontos", ascending=False).head(1)["IdCliente"]

clientes.sort_values(by="qtdePontos", ascending=True).head(1)["IdCliente"]

# %%
# Selecione a primeira transação diária de cada cliente.

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.sort_values("DtCriacao", inplace=True)

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"], inplace=True)

transacoes