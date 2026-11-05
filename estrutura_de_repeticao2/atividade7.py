# Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
# certa cidade, em um determinado dia. Para cada casa visitada foi fornecido o
# número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo
# a ele naquela casa. Se a televisão estivesse desligada, nada seria anotado,
# ou seja, esta casa não entraria na pesquisa. Faça um Programa que:
# leia um número indeterminado de dados, isto é, o número do canal e o
# número de pessoas que estavam assistindo;
# calcule e imprima a porcentagem de audiência em cada canal. Para encerrar
# a entrada de dados, digite o número do canal zero.
canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
while True:
    tv = int(input("A televisão estava ligada?\n1 - Sim\n2 - Não\n"))
    if tv == 2:
        continue
    elif tv == 1:
        canal = int(input("Qual canal foi assistido?\n1- canal 4\n2 - canal 5\n3 - canal 7\n4 - canal 12\n---digite 0 para fechar---\n"))
        if canal == 0:
            break
        if canal == 1:
            pessoas = int(input("Quantas pessoas?: "))
            canal4 += pessoas
        elif canal == 2:
            pessoas1 = int(input("Quantas pessoas?: "))
            canal5 += pessoas1
        elif canal == 3:
            pessoas2 = int(input("Quantas pessoas?: "))
            canal7 += pessoas2
        elif canal == 4:
            pessoas3 = int(input("Quantas pessoas?: "))
            canal12 += pessoas3
total = canal4 + canal5 + canal7 + canal12
p4 = (canal4 / total) * 100
p5 = (canal5 / total) * 100
p7 = (canal7 / total) * 100
p12 = (canal12 / total) * 100
print("=====RESULTADO=====")
print(f"A porcentagem do canal 4 é {p4}%")
print(f"A porcentagem do canal 5 é {p5}%")
print(f"A porcentagem do canal 7 é {p7}%")
print(f"A porcentagem do canal 12 é {p12}%")



            
