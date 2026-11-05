# 7-	Crie um programa que solicite numeros ao usuario continuamente ate que ele insira um número negativo.
# Em seguida, exiba a media dos numeros positivos fornecidos.
contador = 0
contadorN = 0
while True:
    num = int(input("Digite numeros: "))
    if num < 0:
        break
    elif num >= 0:
        contador += num
        contadorN += 1
print ("Sua media é: " , contador / contadorN)
        
