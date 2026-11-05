#3- Máquina com Desgaste Acumulativo
#Uma máquina começa com desgaste 0.
#A cada ciclo:
#Desgaste aumenta 7 unidades
#Se operar acima de 70 ciclos, desgaste aumenta 10 por ciclo
#Se desgaste ≥ 500 → máquina quebra
#Simular até quebrar.
#Exibir:
#Quantos ciclos durou
#Desgaste final
ciclo = 0
desgaste = 0
while True:
    ciclo += 1
    if ciclo <= 70:
        desgaste += 7
    elif ciclo > 70:
        desgaste += 10
    if desgaste >= 500:
        print("Máquina quebrou")
        print("Ciclos durou:", ciclo)
        print("Desgaste final:", desgaste)
        break