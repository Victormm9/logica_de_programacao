# Uma loja tem 150 clientes cadastrados e deseja mandar uma
# correspondência a cada um deles anunciando um bônus especial. Escreva
# um algoritmo que leia o nome do cliente e o valor das suas compras no ano
# passado e calcule um bônus de 10% se o valor das compras for menor que
# 500.000 e de 15 %, caso contrário.
for _ in range (150):
    nome = input("DIgite seu nome: ")
    valor = float(input("Digite o valor da sua compa do ano anterior: "))
    if valor < 500000:
        print(f"Parabéns {nome}, você acabou de ganhar um cupom de 10% de desconto em nossa loja!")
    else:
        print(f"Parabéns {nome}, você acabou de ganhar um cupom de 15% de desconto em nossa loja!")