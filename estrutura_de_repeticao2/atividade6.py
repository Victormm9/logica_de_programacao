# Faça uma Programa que receba, como entrada, uma lista de números
# positivos ou negativos finalizada com o número zero e forneça, como saída, a
# soma dos números positivos, a soma dos números negativos e a soma das
# duas somas parciais e mostre os números pares e ímpares ao final.
pos = 0
neg = 0
par = []
imp = []
while True:
    num = int(input("Escreva varios numeros: "))
    if num == 0:
        break
    if num > 0:
        pos += num
    elif num < 0:
        neg += num
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
total = pos + neg
print("\n--- RESULTADOS ---")
print(f"Soma dos positivos: {pos}")
print(f"Soma dos negativos: {neg}")
print(f"Soma total (positivos + negativos): {total}")
print(f"Números pares digitados: {par}")
print(f"Números ímpares digitados: {imp}")
