#9-	Crie um programa de adivinhação em que o computador escolhe aleatoriamente um número entre 1 e 50, e o usuário precisa adivinhar. O programa deve fornecer feedback (maior ou menor) a cada tentativa e permitir apenas 5 tentativas para acertar. Se o usuário acertar antes do limite, exiba uma mensagem de vitória; caso contrário, revele o número ao final.
import random
contador = 0
num = random.randint (1, 50)
for contador in range (5):
    adivinhacao = int(input("Adivinhe o numero: "))
    if adivinhacao == num:
        print("Parabens acertou!")
    elif adivinhacao > num:
        print("Numero muito grande")
    elif adivinhacao < num:
        print("numero muito menor")

print("Não foi dessa vez, tente novamente")
