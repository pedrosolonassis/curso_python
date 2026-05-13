# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes

# %%
# Para evitar que o DataFrame seja exibido por completo.

df_clientes.head() # Início
df_clientes.tail() # Final
df_clientes.sample(5) # Aleatório

# %%

df_clientes.shape # Dimensão do DataFrame (linhas, colunas)
df_clientes.columns # Colunas do DataFrame
df_clientes.dtypes # Tipos de dados de cada coluna
df_clientes.info() # Resumo do DataFrame
df_clientes.info(memory_usage="deep") # Uso de memória detallhado