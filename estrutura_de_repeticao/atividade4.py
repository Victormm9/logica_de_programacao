#4-	A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o número de filhos e salário. A prefeitura deseja saber:   
# a) madia do salario da populacao; 
# b) media do numero de filhos; 
# c) maior salario; 
# d) percentual de pessoas com salario ate R$100,00. 
# O final da leitura de dados se dara com a entrada de um salario negativo.  
maiorSalario = 0
contadorS = 0
contadorF = 0
contadorP = 0
while True:
    salario = float(input("Digite seu salario: "))
    if salario < 0:
        break

    filhos = int(input("Digite a quantidade de filhos: "))
    contadorS += salario
    contadorF += filhos
    contadorP += 1
    if salario > maiorSalario:
        maiorSalario = salario

mediaS = contadorS / contadorP
mediaF = contadorF / contadorP
percentual = (contadorS / contadorP) * 100

print("Média do salário:", mediaS)
print("Média de filhos:", mediaF)
print("Maior salário:", maiorSalario)
print("Percentual de pessoas com salário até R$100,00:", percentual, "%")

