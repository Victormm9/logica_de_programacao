#8-	Peca ao usuario um numero inteiro positivo e exiba todos os numeros pares de forma decrescente até chegar a zero. O programa deve exibir a sequência de forma organizada,
# considerando que o numero de entrada pode ser par ou impar.
num = int(input("Digite um numero inteiro positivo: "))
contador = 0
intervalo = -2
for contador in range (num ,-1,-1):
    if contador %2 == 0:
        print(contador)