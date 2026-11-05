#  João tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10
# metro e cresce 3 centímetros por ano. Construa um algoritmo que calcule e
# imprima quantos anos serão necessários para que Zé seja maior que João.
joao = 1.50
ze = 1.10
for ano in range (1, 101):
    joao += 0.02
    ze += 0.03
    if ze > joao:
        print(f"serão necessários {ano} anos para que zé seja maior que joão")
        break

