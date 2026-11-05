# 1-Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive) 
numeros = 0
for _ in range (80):
    num = int(input("Digite numeros: "))
    if numeros > 10 and numeros < 150:
        numeros += 1
print(f"tem {numeros} entre 10 e 150")

