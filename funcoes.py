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

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    dados_rolados.append(dado)
    
    nova_lista = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            nova_lista.append(dados_no_estoque[i])
    
    return [dados_rolados, nova_lista]

def calcula_pontos_regra_simples(dados):
    pontos = {}
    for categoria in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == categoria:
                soma += dado
        pontos[categoria] = soma
    return pontos

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

def calcula_pontos_sequencia_baixa(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados:
        return 15
    if 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 15
    if 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 15
    return 0