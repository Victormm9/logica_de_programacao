# 5- Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao filme: ótimo=3, bom=2, regular=1. 
# Faça um programa que receba a idade e a opinião de 15 espectadores e que calcule e mostre: (2 pontos)

# A média das idades das pessoas que responderam ótimo

#A quantidade de pessoas que respondeu regular

#A percentagem de pessoas que respondeu bom entre todos os espectadores analisados
otimo = 0
bom = 0
regular = 0
for _ in range (15):
    idade = int(input("Digite sua idade: "))
    opiniao = int(input("Digite sua opinião: \n1 - Regular\n2 - Bom\n3 - Ótimo\n"))
    if opiniao == 3:
        otimo += idade
    elif opiniao == 2:
        bom += 1
    elif opiniao == 1:
        regular += 1

if otimo > 0:
    media = otimo / 15
else:
    media = 0

print(f"A média das idades das pessoas que responderam ótimo é {media}")
print(f"A quantidade de pessoas que respondeu regular é {regular}")
percentagem_bom = (bom / 15) * 100
print(f"A percentagem de pessoas que respondeu bom é {percentagem_bom}%")