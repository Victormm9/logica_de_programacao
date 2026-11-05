# 4- Uma loja utiliza o código 1 para transação à vista e 2 para transação a prazo. Faça um programa que receba o código e o valor de 15 transações. Calcule e mostre: 
# O valor total das compras à vista
# O valor total as compras a prazo
# O valor total das compras efetuadas
# O valor da primeira prestação das compras a prazo, sabendo se que essas serão pagas em três vezes
somaavista = 0
somalongo = 0
for _ in range (15):
    tra = int(input("Digite a transação: \n1 - a vista\n2 - a prazo\n"))
    if tra == 1:
        avista = float(input("Digite o valor da compra: "))
        somaavista += avista
    elif tra == 2:
        alongo = float(input("Digite o valor da compra: "))
        somalongo += alongo
print("---- Valores -----")
print(f"O valor das compras a vista é {somaavista}")
print(f"O valor das compras a longo prazo é {somalongo}")
print(f"O valor total das compras é {somaavista + somalongo}")
print(f"A primeira prestação é de {somalongo / 3}")
