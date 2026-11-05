# 6-	Peca ao usuario para fornecer um numero inicial e um intervalo. Em seguida, faça uma contagem regressiva do número
# inicial ate zero, decrementando pelo intervalo especificado.
num = int(input("Digite um numero: "))
intervalo = int(input("Digite o intervalo: "))
contador = 0
for contador in range (num , -1 , -intervalo):
    print(contador)
