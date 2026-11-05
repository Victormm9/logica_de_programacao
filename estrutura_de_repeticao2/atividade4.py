# Faça um algoritmo que leia vários códigos do jogador (1 ou 2) que ganhou o
# ponto em uma partida de pingue-pongue, e responda quem ganha a partida.
# A partida chega ao final se um dos jogadores chega a 21 pontos e a
# diferença de pontos entre os jogadores é maior ou igual a dois. Caso
# contrário, ganha aquele que, com mais de 21 pontos, consiga colocar uma
# vantagem de dois pontos sobre o adversário
j1 = 0
j2 = 0
while True:
    ponto = int(input("Qual jogador fez o ponto?\n1- jogador 1\n2 - jogador 2\n"))
    if ponto == 1:
        j1 += 1
    elif ponto == 2:
        j2 += 2
    else:
        print("Opção invalida")
        continue
    print("---PLACAR---\njogador 1:" , j1 , "  jogador 2:" , j2 , "\n")
    if j1 >= 21 and (j1 - j2) >= 2:
        print("Jogador 1 venceu a partida!")
        break
    elif j2 >= 21 and (j2 - j1) >= 2:
        print("Jogador 2 venceu a partida!")
        break


