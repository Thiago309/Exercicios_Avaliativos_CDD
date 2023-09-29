qtd_macas = int(input("Digite a quantidade de maçãs que deseja comprar: "))

duzia = 12
Preco_D = 1

m_duzia = 6
Preco_MD = 1.30


if qtd_macas < duzia:
    valor = qtd_macas * Preco_MD

else:
    valor = qtd_macas * Preco_D

print(f"O valor das maçãs é: R${valor:.2f}")