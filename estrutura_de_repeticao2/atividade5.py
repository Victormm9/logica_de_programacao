#  Supondo que a população de um país A seja 90 milhões de habitantes,
# crescendo com uma taxa anual de 3.5 % e que a população de um país B
# seja 140 milhões de habitantes, crescendo a uma taxa anual de 1 %. Faça
# um algoritmo que calcule e mostre quantos anos serão necessários para que
# a população do país A ultrapasse a população do país B.
paisA = 90000000
paisB = 140000000
for ano in range (1, 101):
    paisA *= 1.035
    paisB *= 1.010
    if paisA > paisB:
        print(f"serão necessários {ano} anos para que pais A ultrapasse pais B")
        break
