# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50

texto = """Escolha o tipo de água:
1 - Mineral Natural
2 - Mineral com Gás
"""

opcao = int(input(texto))

if opcao == 1:
    print("Você escolheu água mineral natural. O valor é R$1,50")
elif opcao == 2:
    print("Você escolheu água mineral com gás. O valor é R$2,50")
else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

# Outra maneira com lógica

texto = """Escolha o tipo de água:
1 - Mineral Natural
2 - Mineral com Gás
"""

opcao = int(input(texto))

conta = 0
if opcao == 1:
    conta = 1.50
elif opcao == 2:
    conta = 2.50

if conta == 0:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
else:
    print("Sua conta é: R$", conta)

# Altere o programa anterior para considerar a quantidade de água
texto = """Escolha o tipo de água:
1 - Mineral Natural
2 - Mineral com Gás
"""

opcao = int(input(texto))

valor_item = 0
if opcao == 1:
    valor_item = 1.50
elif opcao == 2:
    valor_item = 2.50

if valor_item == 0:
    print("Opção inválida. Por favor, escolha 1 ou 2.")
else:
    qtde = int(input("Quantas garrafas você deseja? "))
    valor_total = valor_item * qtde
    print("Sua conta é: R$", valor_total)

# %%
# Faça um programa que receba um número. Verifique se o número informado é par ou ímpar.
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# %%
# Outra maneira com função:
def par_impar(numero:int):
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
numero = int(input("Digite um número: "))

par_impar(numero)

# %%
# Com retorno:
def par_impar(numero:int)->str:
    if numero % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."
numero = int(input("Digite um número: "))
resultado = par_impar(numero)

print("O valor", numero, "é", resultado)

# %%
# Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:
notas = []
for i in range(4):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print("A média das notas é:", media)
print("A menor nota é:", menor)
print("A maior nota é:", maior)