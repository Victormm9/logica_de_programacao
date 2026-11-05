# 1- Balanceamento Dinâmico de Linha de Produção
# Uma linha tem 5 estações.
# Cada estação:
# Recebe peças
# Processa no máximo X por ciclo
# Pode quebrar se operar acima de 90% da capacidade por 5 ciclos seguidos
# Regras:
# Peças não processadas acumulam
# Se uma estação quebra:
# Toda a linha para
# Produção continua até:
# Meta diária atingida
# Ou falha estrutural
# Exibir:
# Produção total
# Estação que falhou (se houver)
# Ciclos executados
ciclo = 0
pecasnao = 0
pecas = int(input("Quantas peças recebe?: "))
processa = int(input("Qual o maximo por ciclo?: "))
meta = int(input("Qual a meta diaria?: "))
quebra = pecas * 0.9
while True:
    ciclo += 1
    if pecas > 0:
        if pecas >= processa:
            pecas = pecas - processa
            pecasnao = pecasnao + 0
        elif pecas < processa:
            pecasnao = pecasnao + (processa - pecas)
            pecas = 0
        if pecas > quebra:
            print("Estação quebrou")
            print("Produção total:", (ciclo * processa) - pecasnao)
            print("Ciclos executados:", ciclo)
            break
    if (ciclo * processa) - pecasnao >= meta:
        print("Meta atingida")
        print("Produção total:", (ciclo * processa) - pecasnao)
        print("Ciclos executados:", ciclo)
        break