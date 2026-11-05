#2- Controle de Temperatura de Forno
#Um forno industrial inicia com temperatura informada pelo usuario.
#A cada ciclo:
#Se temperatura < 800 = aumenta 50 graus
#Se temperatura >= 800 e < 1000 = aumenta 20 graus
#Se temperatura >= 1000 = mantem constante
#O sistema deve repetir ate:
#Atingir 1000 graus
#Exibir:
#Quantos ciclos foram necessarios
#Temperatura final
ciclo = 0
temperatura = float(input("Qual a temperatura do forno?: "))
while True:
    ciclo += 1
    if temperatura < 800:
        temperatura = temperatura + 50
    elif temperatura >= 800 and temperatura < 1000:
        temperatura = temperatura + 20
    elif temperatura >= 1000:
        print(ciclo)
        print(temperatura)
        break
   
