# 3-	Fazer um programa que retorne quantos valores digitados pelo usuario sao negativos.
# Repetir o enquanto ate o usuario digitar o valor ZERO:
contador = 0
while True:
    num = int(input("Digite numeros: "))
    if num < 0:
        contador += 1
    elif num == 0:
        print("Programa encerrado, a quantidade numeros negativos digitado é:\n " ,  (contador) )
