# Faça um programa que dê bom dia, perguntando o nome da pessoa e depois dizendo que é um prazer conhecê-la.

nome = input("Bom dia! Qual é o seu nome? ")

print("Prazer em conhecê-lo,", nome + "!")

# Faça um programa que receba um número inteiro e calcule sua raiz quadrada e exiba o resultado.

numero = int(input("Digite um número inteiro para calcular a raiz quadrada: "))

raiz = round(numero ** (0.5), 2)  # Número pode ser elevado a 1/2

print ("A raiz quadrada de", numero, "é:", raiz)