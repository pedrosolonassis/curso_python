# %%
# Pares de chave-valor

dados_pedro = {"nome":"Pedro", "idade":24, "cidade":"João Pessoa", "filhos":False, "formação":["Relações Internacionais", "Ciência de Dados"], "tenista": [{"classe": "quinta", "ano": 2024}, {"classe": "quinta/quarta", "ano": 2025}, {"classe": "quarta", "ano": 2026}, {"classe": "terceira", "ano": 2027}]}

# %%
print(dados_pedro)
print(dados_pedro["formação"][-1])
print(dados_pedro["tenista"][2]["classe"])

# %%
dados_pedro["estado civil"] = "solteiro"
print(dados_pedro)

# %%
print("chaves:", dados_pedro.keys()) # chaves
print("valores:", dados_pedro.values()) # valores
print("itens:", dados_pedro.items()) # chaves e valores

# %%
for i in dados_pedro:
    print(i, "->", dados_pedro[i])

# %%
for chave, valor in dados_pedro.items():
    print(chave, "->", valor)