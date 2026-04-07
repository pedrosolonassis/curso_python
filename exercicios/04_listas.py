# Escreva um programa que tenha lista de números
# e conte quantas vezes um número específico aparece na lista. 
# Solicite ao usuário um número e exiba a contagem.

numeros = [1, 2, 3, 4, 5, 2, 2, 6, 7, 8, 2]

numero_especifico = int(input("Digite um número: "))

contagem = 0
for i in numeros:
    if i == numero_especifico:
        contagem += 1

print("Quantidade de", numero_especifico, "na lista:", contagem)

# %%
# Escreva um programa que solicite ao usuário uma série de idades e armazene-as em uma lista.

idades = []

while True:
    idade = input("Digite uma idade: ")
    
    if idade == "":
        break
    
    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print("Média das idades:", media)
print("Idade mínima:", minimo)
print("Idade máxima:", maximo)
print("Quantidade de idades:", qtde)

# %%
# Considere a lista: [120, "Python", 120.01, "aws", False, [10,20]]
# Fala um programa que retorne as seguintes informações:
# a) Elemento na posição -1 da lista
lista = [120, "Python", 120.01, "aws", False, [10,20]]
print(lista[-1])
# b) Elemento na primeira posição da lista
print(lista[0])
# c) O último caractere do segundo elemento da lista
print(lista[1][-1])

# %%
# Escreva um programa que solicite ao usuário duas strings
# e as concatene em uma única string. Em seguida, exiba a string resultante.
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
string_concatenada = string1 + string2
print("String concatenada:", string_concatenada)
