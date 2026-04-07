# Faça um programa que receba 4 alturas usando um laço de repetição e realize a soma dessas alturas.

soma = 0 # Valor final
qtde_entradas = 4 # Contador de entradas

while qtde_entradas > 0:
    altura = float(input("Digite a altura: "))
    soma += altura # Ou soma = soma + altura
    qtde_entradas -= 1 # Ou qtde_entradas = qtde_entradas - 1

print("A soma das alturas é:", soma)

# Com o for:

soma = 0 # Valor final
qtde_entradas = 4 # Contador de entradas

for i in range(qtde_entradas): # range(0, qtde_entradas) -> 0, 1, 2, 3
    altura = float(input("Digite a altura: "))
    soma += altura # Ou soma = soma + altura

print("A soma das alturas é:", soma)

# Faça um programa que receba 5 alturas usando um laço de repetição e realize a média dessas alturas.

soma = 0 # Valor final
qtde_entradas = 5 # Contador de entradas

for i in range(qtde_entradas):
    altura = float(input("Digite a altura: "))
    soma += altura # Ou soma = soma + altura
media = soma / qtde_entradas

print("A média das alturas é:", media)

# Faça um programa que receba uma quantidade indefinida de valores correspondentes a "saldo em conta", 
# mas quando o usuário apertar "enter" sem digitar valor algum, 
# o programa para de receber valores e exibe a soma de todos os valores digitados anteriormente.

saldo_total = 0 # Valor final

while True:
    saldo = input("Digite o saldo em conta: ")
    if saldo == "":
        break
    saldo_total += float(saldo) # Ou saldo_total = saldo_total + float(saldo)

print("O saldo total é:", saldo_total)

# Faça um programa que conte quantas vezes a letra "a" aparece em uma frase digitada pelo usuário.

frase = input("Digite uma frase: ")
contador_a = 0 # Contador de letras "a"

for letra in frase:
    if letra == "a":
        contador_a += 1

print("A letra 'a' aparece", contador_a, "vezes na frase.")


