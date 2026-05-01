import random
from funcoes import guardar_dado, remover_dado, calcula_pontos_regra_simples, calcula_pontos_soma, calcula_pontos_sequencia_baixa, calcula_pontos_sequencia_alta, calcula_pontos_full_house, imprime_cartela

def rolar_dados(quantidade):
    dados = []
    for i in range(quantidade):
        dados.append(random.randint(1, 6))
    return dados

def calcular_pontos_combinacao(combinacao, todos_dados):
    if combinacao == "sem_combinacao":
        return calcula_pontos_soma(todos_dados)
    if combinacao == "sequencia_baixa":
        return calcula_pontos_sequencia_baixa(todos_dados)
    if combinacao == "sequencia_alta":
        return calcula_pontos_sequencia_alta(todos_dados)
    if combinacao == "full_house":
        return calcula_pontos_full_house(todos_dados)
    if combinacao == "quadra":
        contagens = {}
        for dado in todos_dados:
            if dado not in contagens:
                contagens[dado] = 0
            contagens[dado] += 1
        for valor in contagens:
            if contagens[valor] >= 4:
                return calcula_pontos_soma(todos_dados)
        return 0
    if combinacao == "cinco_iguais":
        contagens = {}
        for dado in todos_dados:
            if dado not in contagens:
                contagens[dado] = 0
            contagens[dado] += 1
        for valor in contagens:
            if contagens[valor] == 5:
                return 50
        return 0
    pontos = calcula_pontos_regra_simples(todos_dados)
    return pontos[int(combinacao)]

def imprimir_estado(dados_rolados, dados_guardados):
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

cartela = {
    'regra_simples': {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

combinacoes_validas_simples = ['1', '2', '3', '4', '5', '6']
combinacoes_validas_avancadas = ['sem_combinacao', 'quadra', 'full_house', 'sequencia_baixa', 'sequencia_alta', 'cinco_iguais']

imprime_cartela(cartela)

for rodada in range(12):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    imprimir_estado(dados_rolados, dados_guardados)

    rodada_finalizada = False
    while not rodada_finalizada:
        opcao = input(">")

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input(">"))
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            imprimir_estado(dados_rolados, dados_guardados)

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input(">"))
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            imprimir_estado(dados_rolados, dados_guardados)

        elif opcao == "3":
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rerrolagens += 1
            imprimir_estado(dados_rolados, dados_guardados)

        elif opcao == "4":
            imprime_cartela(cartela)
            imprimir_estado(dados_rolados, dados_guardados)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            jogada_feita = False
            while not jogada_feita:
                combinacao = input(">")
                todos_dados = dados_rolados + dados_guardados

                if combinacao in combinacoes_validas_simples:
                    chave = int(combinacao)
                    if cartela['regra_simples'][chave] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela['regra_simples'][chave] = calcular_pontos_combinacao(combinacao, todos_dados)
                        jogada_feita = True
                        rodada_finalizada = True

                elif combinacao in combinacoes_validas_avancadas:
                    if cartela['regra_avancada'][combinacao] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela['regra_avancada'][combinacao] = calcular_pontos_combinacao(combinacao, todos_dados)
                        jogada_feita = True
                        rodada_finalizada = True

                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

pontuacao = 0
soma_simples = 0

for i in range(1, 7):
    if cartela['regra_simples'][i] != -1:
        pontuacao += cartela['regra_simples'][i]
        soma_simples += cartela['regra_simples'][i]

for combinacao in cartela['regra_avancada']:
    if cartela['regra_avancada'][combinacao] != -1:
        pontuacao += cartela['regra_avancada'][combinacao]

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")