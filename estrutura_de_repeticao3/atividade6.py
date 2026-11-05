#7 - O cardápio de uma lanchonete é o seguinte:

#Especificação      Código     Preço
#Cachorro Quente     100      R$ 1,20
#Bauru Simples       101      R$ 1,30
#Bauru com ovo       102      R$ 1,50
#Hambúrguer          103      R$ 1,20
#Cheeseburguer       104      R$ 1,30
#Refrigerante        105      R$ 1,00
#Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço *quantidade) e o total geral do pedido.
#  Considere que o cliente deve informar quando o pedido deve ser encerrado.

total = 0
while True:
    codigo = int(input("Digite o codigo do item (ou 0 para encerrar o pedido): "))
    if codigo == 0:
        break
    elif codigo == 100:
        quantidade = int(input("Digite a quantidade desejada: "))
        valor = 1.20 * quantidade
        total += valor
    elif codigo == 101: 
        quantidade = int(input("Digite a quantidade desejada: "))
        valor = 1.30 * quantidade
        total += valor
    elif codigo == 102:
        quantidade = int(input("Digite a quantidade desejada: "))
        valor = 1.50 * quantidade
        total += valor
    elif codigo == 103:
        quantidade = int(input("Digite a quantidade desejada: "))
        valor = 1.20 * quantidade
        total += valor
    elif codigo == 104:
        quantidade = int(input("Digite a quantidade desejada: "))
        valor = 1.30 * quantidade
        total += valor
    elif codigo == 105:
        quantidade = int(input("Digite a quantidade desejada: "))
        valor = 1.00 * quantidade
        total += valor

print(f"Total do pedido: R$ {total:.2f}")