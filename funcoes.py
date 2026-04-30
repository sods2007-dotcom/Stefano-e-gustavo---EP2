import random
def rolar_dados(dados):
    resultado = []
    for i in range(dados):
        resultado.append(random.randint(1, 6))
    return resultado

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    valor = dados_rolados[dado_para_guardar]
    
    dados_no_estoque.append(valor)
    
    nova_lista = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            nova_lista.append(dados_rolados[i])
    
    return [nova_lista, dados_no_estoque]