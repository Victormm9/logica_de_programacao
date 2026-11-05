#8 - Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

#Os juros e a quantidade de parcelas seguem a tabela abaixo:

#Qtd parcelas	% Juros sobre o valor inicial da dívida
#1	0
#3	10
#6	15
#9	20
#12	25
#Saída do programa

#Valor da Dívida - Valor dos Juros - Qtd de Parcelas - Valor da Parcela R$ 1.000 0 1 R$ 1.000,00 R$ 1.100 100 3 R$ 366,00 R$ 1.150 150 6 R$ 191,67

valor = float(input("Digite o valor da dívida: "))
print("Valor da Dívida - Valor dos Juros - Qtd de Parcelas - Valor da Parcela")
print(f"R$ {valor} - 0 - 1 - R$ {valor}")
print(f"R$ ({valor * 1.10:.2f}) - {valor * 0.10:.2f} - 3 - R$ {(valor * 1.10) / 3:.2f}")
print(f"R$ ({valor * 1.15:.2f}) - {valor * 0.15:.2f} - 6 - R$ {(valor * 1.15) / 6:.2f}")
print(f"R$ ({valor * 1.20:.2f}) - {valor * 0.20:.2f} - 9 - R$ {(valor * 1.20) / 9:.2f}")
print(f"R$ ({valor * 1.25:.2f}) - {valor * 0.25:.2f} - 12 - R$ {(valor * 1.25) / 12:.2f}")
