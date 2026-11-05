# 2 - Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher. No final informe total de homens e de mulheres. 
# Escrever um algoritmo que leia o nome e o sexo de 56 pessoas e informe o nome e se ela é homem ou mulher.
#  No final informe total de homens e de mulheres. 
homem = 0
mulher = 0
for _ in range (56):
    sexo = int(input("Digite seu genêro: \n1 - Homem\n2 - Mulher\n"))
    if sexo == 1:
     homem += 1
    elif sexo == 2:
      mulher += 1
    else:
        continue
    print(f"A quantidade de Homens é {homem}, e a quantidade de mulheres é {mulher}")
