# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

import random

LIMITE_MIN = 1
LIMITE_MAX = 15
TENTATIVAS_TOTAIS = 3

def get_input():
    """Valida a entrada do usuário para garantir que seja um inteiro no intervalo correto."""
    while True:
        try:
            chute = int(input(f"Digite um número entre {LIMITE_MIN} e {LIMITE_MAX}: "))
            if LIMITE_MIN <= chute <= LIMITE_MAX:
                return chute
            print(f"Erro! O número deve estar entre {LIMITE_MIN} e {LIMITE_MAX}.")
        except ValueError:
            print("Erro! Entrada inválida. Por favor, digite apenas números inteiros.")

def verificar_acerto(sorteado, chute):
    """Compara o chute com o número sorteado e dá feedback ao usuário."""
    if sorteado == chute:
        print("🎉 Parabéns! Você acertou o número sorteado!")
        return True
    
    dica = "menor" if sorteado < chute else "maior"
    print(f"O número sorteado é {dica} que o seu chute.")
    return False

def jogar():
    numero_sorteio = random.randint(LIMITE_MIN, LIMITE_MAX)
    
    for tentativa in range(TENTATIVAS_TOTAIS):
        chute_usuario = get_input()
        
        if verificar_acerto(numero_sorteio, chute_usuario):
            break
        
        restantes = TENTATIVAS_TOTAIS - 1 - tentativa
        if restantes > 0:
            print(f"Tente novamente! Você tem {restantes} chance(s) restante(s).")
    else:
        print(f"❌ Suas chances acabaram! O número era: {numero_sorteio}")

if __name__ == "__main__":
    jogar()