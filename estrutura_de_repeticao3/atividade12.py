# 13-Simulação de Crescimento Populacional com Evento Crítico
#Duas populações A e B crescem anualmente:
#A cresce 3% ao ano
#B cresce 1,5% ao ano
#A cada 5 anos ocorre uma crise que reduz ambas em 7%.
#Determine em quantos anos A ultrapassa B, considerando valores iniciais informados pelo usuário.
A = int(input("Digite a população inicial de A: "))
B = int(input("Digite a população inicial de B: "))
anos = 0
while A <= B:
    A += A * 0.03
    B += B * 0.015
    anos += 1
    if anos % 5 == 0:
        A -= A * 0.07
        B -= B * 0.07

print(f"A ultrapassa B em {anos} anos.")
