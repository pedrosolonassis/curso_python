# %%

import pandas as pd

# %%
# Medias das idades

idades = [20, 21, 22, 23, 24, 25]
media = sum(idades) / len(idades)
print("Média:", media)

# %%
# Variancia das idades

diffs = 0
for i in idades:
    diffs += (i - media) ** 2
variancia = diffs / (len(idades)-1)

print("Variancia:", variancia)

# %%

series_idades = pd.Series(idades)
print(series_idades)

# %%
# Média das idades
media_idades = series_idades.mean()

# %%
# Summary idades

summary_idades = series_idades.describe()
print(summary_idades)
# %%
