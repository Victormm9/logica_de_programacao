# 1. Feita uma pesquisa em 12 cidades para coletar dados sobre acidentes de
# trânsito. Foram obtidos os seguintes dados:
# - código da cidade
# - número de veículos de passeio
# - número de acidentes de trânsito com vítimas
# Código Cidade
# 11 Jaraguá do Sul
# 12 Joinville
# 13 Blumenau
# 14 Florianópolis
# 21 Porto Alegre
# 22 Bento Gonçalves
# 23 Garibaldi
# 24 Caxias do Sul
# 31 Curitiba
# 32 Foz do Iguaçu
# 33 Toledo
# 34 Cascavel
# Código Estado
# 1 SC
# 2 RS
# 3 PR
# Deseja-se saber:
# a) o maior e o menor índice de acidentes de trânsito e a que cidades/estado
# pertencem
# b) qual a média de veículos nas cidades brasileiras (total / por estado)
# c) qual a média de acidentes com vítimas nas cidades de Santa Catarina e o
# total por estado.
codigoCidade = 0; numeroVeiculos = 0; numeroAcidentes = 0
maiorAcidente = 0
cidadeMaior = 0
cidadeMenor = 0
somaTodasCidades = 0
somaScVeiculos = 0
somaScAcidentes = 0
qtdSC = 0
somaRsVeiculos = 0
somaRsAcidentes = 0
qtdRs = 0
somaPrVeiculos = 0
somaPrAcidentes = 0
11 == "Jaraguá do Sul"
12 == "Joinville" 
13 == "Blumenau" 
14 == "Florianópolis" 
21 == "Porto Alegre" 
22 == "Bento Gonçalves" 
23 == "Garibaldi" 
24 == "Caxias do Sul" 
31 == "Curitiba" 
32 == "Foz do Iguaçu" 
33 == "Toledo" 
34 == "Cascavel" 

qtdPr = 0
menorAcidente = float('inf')
for contador in range (1,12):
    codigoCidade = int(input("Digite o codigo da cidade: "))
    numeroVeiculos = int(input("Digite o número de veiculos: "))
    numeroAcidentes = int(input("Digite o numero de acidentes: "))

    if  numeroAcidentes > maiorAcidente:
     maiorAcidente = numeroAcidentes
     cidadeMaior = codigoCidade
    if numeroAcidentes < menorAcidente:
        menorAcidente = numeroAcidentes
        cidadeMenor = codigoCidade
        somaTodasCidades += numeroVeiculos
    print("A média de veículos no Brasil é: ", (somaTodasCidades / 12))

    if codigoCidade >= 11 and codigoCidade <= 14:
        somaScVeiculos += numeroVeiculos
        somaScAcidentes += numeroAcidentes
        qtdSC += 1
    print("A média de veiculos no Brasil é: ", (somaScVeiculos / qtdSC))
    print("A média de acidentes em SC é: ", (somaScAcidentes / qtdSC))

    if codigoCidade >= 21 and codigoCidade <= 24:
        somaRsVeiculos += numeroVeiculos
        somaRsAcidentes += numeroAcidentes
        qtdRs += 1
    print("A média de veiculos no Brasil é: ", (somaRsVeiculos / qtdRs))
    print("A média de acidentes em SC é: ", (somaRsAcidentes/ qtdRs))

    if codigoCidade >= 31 and codigoCidade <= 34:
        somaPrVeiculos += numeroVeiculos
        somaPrAcidentes += numeroAcidentes
        qtdPr += 1
    print("A média de veiculos no Brasil é: ", (somaPrVeiculos / qtdPr))
    print("A média de acidentes em SC é: ", (somaPrAcidentes / qtdPr))



    




