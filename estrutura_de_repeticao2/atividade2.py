# 2. Construa um algoritmo que receba o código de vários produtos e os
# classifique de acordo com a tabela:
# CÓDIGO CLASSIFICAÇÃO
# 1 Alimento não-perecível
# 2 a 4 Alimento perecível
# 5 e 6 Vestuário
# 7 Higiene pessoal
# 8 a 15 Limpeza e utensílios domésticos
# Qualquer outro código inválido exibe uma mensagem ao usuário.
# Quando o usuário digitar 0 (zero) o programa finaliza e exibe o número total
# de produtos classificados em cada categoria.

while True:
    cod = int(input("Digite o codigo do produto: "))
    if cod == 0:
     break
    elif cod < 0 or cod > 15:
     print("Codigo inválido")
    match cod:
        case 1:
         print("Alimento não perecível")
        case 2 | 3 | 4:
         print("Alimento perecível")
        case 5 | 6:
         print("Vestuário")
        case 7:
         print("Higiene pessoal")
        case 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
         print("Limpeza e utensílios domésticos")

