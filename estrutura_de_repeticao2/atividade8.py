# Faça um programa que receba o valor de um carro e mostre uma tabela com
# os seguintes dados: preço final, quantidade de parcelas e valor da parcela.
# Considere o seguinte:
# ● O preço final para compra à vista tem um desconto de 20%;
# ● A quantidades de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60.
# ● Os percentuais de acréscimo seguem a tabela a seguir.
# Quantidade de parcelas Percentual de acréscimo sobre o
# preço final
# 6 3%
# 12 6%
# 18 9%
# 24 12%
# 30 15%
# 36 18%
# 42 21%
# 48 24%
# 54 27%
# 60 30%
while True:
    carro = float(input("Digite o valor do carro: "))
    print("----Tabela de formas de pagamento----")
    print(f"Seu valor a vista é: {carro * 0.80}")
    qparcela = int(input("quantas parcelas gostaria?:\n6 parcelas\n12 parcelas\n18 parcelas\n24 parcelas\n30 parcelas\n36 parcelas\n42 parcelas\n48 parcelas\n54 parcelas\n60 parcelas\n"))
    if qparcela == 6:
        carro = carro * 1.030
    elif qparcela == 12:
        carro = carro * 1.060
    elif qparcela == 18:
        carro = carro * 1.090
    elif qparcela == 24:
        carro = carro * 1.120
    elif qparcela == 30:
        carro = carro * 1.150
    elif qparcela == 36:
        carro = carro * 1.180
    elif qparcela == 42:
        carro = carro * 1.210
    elif qparcela == 48:
        carro = carro * 1.240
    elif qparcela == 54:
        carro = carro * 1.270
    elif qparcela == 60:
        carro = carro * 1.300
    else:
        break
    print(f"O valor total do seu carro é {carro} e sua parcela é {carro / qparcela}")


