# %%
def f(x):
    resultado = 1 + x
    return resultado

f(10)

# %%

def juros_compostos(anos):
    return 1000 * (1.13) ** anos

juros_compostos(10)
# %%
def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos serve para calcular o retorno financeiro a partir de um aporte.
Deve-se considerar o valor, a taxa d ejuros e o tempo (em anos) para o cálculo do retorno financeiro.

aporte: um número inteiro que representa o valor em R$

taxa: um número float entre 0 e 1 que representa a taxa de juros

anos: um número inteiro >= que representa o tempo que o investimento ficará aplicado
    """
    return aporte * (1 + taxa) ** anos

juros_compostos(1000, 0.13, 10)

# %%
# Boa prática: nomear os parâmetros da função
juros_compostos(taxa=0.13, anos=10, aporte=1000)

# %%
# Função de soma
def soma(a: float, b: float)->float:
    return a + b

# Função de média
def media(a: float, b: float)->float:
    return soma(a, b) / 2

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

print("Média:", media(a, b))

# %%
# Uma forma mais mutável de elementos
def soma(a: float, b: float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b: float, *args)->float:
    return soma(a, b, *args) / (2 + len(args))

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

print("Média", media(a,b,c,d))


# %%
# Cálculo de Imposto
def calc_imposto(preco:float, tx_base:float, **kwargs)->float:
    imposto = preco * tx_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    return imposto

# %%

impostos_gerais = {
    "municipal": 0.01,
    "estadual": 0.005,
    "federal": 0.001,
}

calc_imposto(100, 0.03, **impostos_gerais)