h_inicio = int(input("Digite a hora inicial do jogo: "))
h_fim = int(input("Digite a hora final do jogo: "))
qtd_h = 0

if (h_inicio <= h_fim):
    qtd_h = h_fim - h_inicio
else:
    qtd_h = 24 - h_inicio + h_fim

print(f"O total de horas jogadas foi de: {qtd_h} horas !")

