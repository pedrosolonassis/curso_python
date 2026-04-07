# Listas: Conjunto de elementos

# %%
idades = [20, 30, 40, 50]
print(idades)

# %%
solon =["Solon", 24, "Masculino", "Programador", "João Pessoa", "Tenis", ["Amador", "Backhand Duas Mãos", "Baseline"]]
print(solon)

# %%
type(solon)

# %%
print(solon[0]) # Acessar o primeiro elemento da lista
print(solon[1]) # Acessar o segundo elemento da lista
print(solon[-1]) # Acessar o último elemento da lista
solon[4] = "Paraiba" # Modificar o elemento da lista

# %%
solon[6][:2]

# %%
idades = [20, 30, 40, 50]
print("Soma das idades:", sum(idades)) # Somar os elementos da lista
print("qtde idades:", len(idades)) # len: quantidade de elementos da lista
print("Média das idades:", sum(idades) / len(idades)) # Média das idades

# %%
# Para inverter a ordem da lista
caracteristicas = solon[6][::-1]
print(caracteristicas)

# %%
# Pular de dois em dois
caracteristicas = solon[6][::2]
print(caracteristicas)
