#9- Uma empresa utiliza os códigos 1 para funcionários do setor administrativo
#  e 2 para os funcionários do setor operacional. Faça um programa que receba 
# o código e o salário de 20 funcionários. Calcule e mostre:

#●     A média salarial do setor administrativo.

#●     A média salarial do setor operacional.

#●     O total de salários pagos pela empresa.

#●     A quantidade de funcionários em cada setor.
funcionarios_adm = 0
funcionarios_op = 0
quantidade_adm = 0
quantidade_op = 0
for _ in range(20):
    codigo = int(input("Digite o codigo de funcionario: \n1 - Administrativo\n2 - operacional\n"))
    if codigo == 1:
        salario = float(input("Digite o salario do funcionario: "))
        funcionarios_adm += salario
        quantidade_adm += 1
    elif codigo == 2:
        salario = float(input("Digite o salario do funcionario: "))
        funcionarios_op += salario
        quantidade_op += 1

media_adm = funcionarios_adm / quantidade_adm if quantidade_adm > 0 else 0
media_op = funcionarios_op / quantidade_op if quantidade_op > 0 else 0
total_salarios = funcionarios_adm + funcionarios_op
print(f"Média salarial do setor administrativo: R$ {media_adm}")
print(f"Média salarial do setor operacional: R$ {media_op}")
print(f"Total de salários pagos pela empresa: R$ {total_salarios}")
print(f"Quantidade de funcionários no setor administrativo: {quantidade_adm}")
print(f"Quantidade de funcionários no setor operacional: {quantidade_op}")
