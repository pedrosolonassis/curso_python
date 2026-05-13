# %%
# Leia o arquivo transacoes.csv com a formatação correta;
# Adicione uma coluna com valores 1;
# Salve o dataframe com nome: transacoes_1.csv

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes['nova_coluna'] = 1

transacoes.to_csv("../data/transacoes_1.csv", index=False)

# %%
# Quantas linhas há no arquivo clientes.csv ?

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
linhas = df_clientes.shape[0]

print(f"O arquivo de clientes.csv tem {linhas} linhas")

# %%
# Quantas colunas do tipo int há no arquivo transacoes.csv?

df_transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
df_transacoes.dtypes

print("O arquivo transacoes.csv tem uma coluna do tipo int (qtdePontos)")

# %%
# Quantas colunas do tipo object há no arquivo produtos.csv?

df_produtos = pd.read_csv("../data/produtos.csv", sep=";")
df_produtos.dtypes

print("O arquivo produtos.csv tem 1 coluna do tipo object (descProduto)")

# %%
# Qual o id do cliente no índice 4 no arquivo clientes.csv?

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.loc[4]["IdCliente"]

# %%
# Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv?

df_clientes.iloc[9]["qtdePontos"]

# %%
# Quantos clientes tem vínculo com a Twitch?

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.head()

filtro = df_clientes["flTwitch"] == 1
qtde_twitch = df_clientes[filtro].shape[0]

print(f"Há {qtde_twitch} clientes com vínculo com a Twitch")

# %%
# Quantos clientes tem um saldo de pontos maior que 1000?

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes.head()

filtro = df_clientes["qtdePontos"] > 1000
qtde_1000 = df_clientes[filtro].shape[0]

print(f"Há {qtde_1000} clientes com saldo de pontos maior que 1000")

# %%
# Quantas transações ocorreram no dia 2025-02-01?

