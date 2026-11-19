numero = int(input("Digite um número: "))
fatorial = 1
for i in range(2, numero + 1):
    fatorial = fatorial * i
print(f"Fatorial de {numero}: {fatorial}")
