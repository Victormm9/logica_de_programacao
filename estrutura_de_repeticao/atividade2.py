# 2-	Fazer um programa que calcule a tabuada de qualquer numero, 
# e o limite de calculo deve ser definido pelo usuario:
tabu = int(input("Digite o numero da tabuada: "))
limite = int(input("Digite o numero limite: "))
num = tabu * limite
contador = 0
while contador <= num:
    print(contador)
    contador += tabu