#12- Uma sequência de 50 números será informada pelo usuário. Escreva um programa que:
#●     Conte quantos desses números são múltiplos de 3.
#●     Exiba a soma de todos os números pares.
multiplosde3 = 0
somaPares = 0
for _ in range(50):
    numero = int(input("Digite um número: "))
    if numero % 3 == 0:
        multiplosde3 += 1
        if numero % 2 == 0:
            somaPares += numero

print(f"A quantidade de números múltiplos de 3 é: {multiplosde3}")
print(f"A soma de todos os números pares é: {somaPares}")