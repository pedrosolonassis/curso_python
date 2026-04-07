# while: comparação lógica, laço de repetição

# %%
# Teste Mesa

numero = 2
count = 1

while count <= 100:
    print(numero, "X", count, "=", numero * count)
    count = count + 1 # Ou count += 1

print ("Fim da tabuada do", numero)

# %%
# Valores divisíveis por 4

count = 4
while count <= 100:
    resto = count % 4
    if resto == 0:
        print(count, "é divisível por 4")
    count += 1