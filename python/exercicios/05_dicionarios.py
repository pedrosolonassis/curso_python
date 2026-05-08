# %%
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
fruta = input("Digite o nome de uma fruta: ")

frutas = {"Maçã": "R$1,50", 
          "Banana": "R$2,75",   
          "Uva": "R$1,90",
          "Pera": "R$1,25",
          "Laranja": "R$0,65",
          "Limão": "R$1,25",
          "Goiaba": "R$2,15",
          "Abacaxi": "R$3,20",
          "Jaca": "R$5,80",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Fruta não encontrada.")

# %%
# Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases, ele pode apenas apertar o “enter”.
# Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
frases = {}

while True:
    frase = input("Digite uma frase: ")
    if frase == "":
        break
    if frase in frases:
        frases[frase] += 1
    else:
        frases[frase] = 1

items = list(frases.items())
items.sort(key=lambda x: x[1], reverse=True)

for frase, quantidade in items:
    print(frase, "->", quantidade)