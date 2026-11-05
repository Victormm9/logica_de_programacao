# 5-	Escreva um algoritmo que calcule a media dos numeros digitados pelo usuario, se eles forem pares.
# Termine a leitura se o usuario digitar zero (0).
contador = 0
contadorP = 0
while True:
    num = int(input("Digite seus números: "))
    if num == 0:
        break

    elif num %2 == 0:
        contador += num
        contadorP += 1
        
        
media = contador / contadorP
print("A soma dos seus números positivos é: ")
print(media)