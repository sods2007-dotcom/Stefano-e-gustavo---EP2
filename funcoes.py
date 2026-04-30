import random
def rolar_dados(dados):
    resultado = []
    for i in range(dados):
        resultado.append(random.randint(1, 6))
    return resultado