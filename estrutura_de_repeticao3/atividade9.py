#10- Um professor registrou as notas de 35 alunos em uma prova. 
# Faça um algoritmo que:
#●     Leia o nome e a nota de cada aluno.
#●     Informe a média geral da turma.
#●     Conte quantos alunos tiveram nota acima de 7.
total_notas = 0
alunosacima = 0
for _ in range(35):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    total_notas += nota
    if nota > 7:
        alunosacima += 1
mediaGeral = total_notas / 35
print(f"A média geral da turma é: {mediaGeral}")
print(f"A quantidade de alunos com nota acima de 7 é: {alunosacima}")