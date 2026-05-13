# %% 
# Importando o arquivo CSV para um DataFrame

import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df

# %%
# Exportando o DataFrame para um arquivo CSV

df.to_csv("../data/clientes_copy.csv", index=False)
# %%
# Exportando o DataFrame para um arquivo Parquet (binario)

df.to_parquet("../data/clientes_copy.parquet", index=False)

# %%
