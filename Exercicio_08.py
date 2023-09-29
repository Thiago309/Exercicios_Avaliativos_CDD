n = 0
soma = 0
media = 0

qtd = int(input("Informe a quantidade de vezes para repetir: "))

for i in range(qtd):
    n = float(input(f"Digite o valor {i + 1}: "))
    soma += n

media = soma / qtd
print(f"A sua média é: {media:.2f}")
