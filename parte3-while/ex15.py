positivos = 0
numero = float(input("Digite um número (0 para parar): "))
while numero != 0:
    if numero > 0:
        positivos = positivos + 1
    numero = float(input("Digite um número (0 para parar): "))
print("Quantidade de números positivos:", positivos)
