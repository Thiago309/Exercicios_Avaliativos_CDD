eleitores = int(input("Digite a quantidade de eleitores: "))
v_branco = int(input("Digite a quantidade de votos em brancos: "))
v_nulo = int(input("Digite a quantidade de votos nulos: "))
v_validos = int(input("Digite a quantidade de votos invalidos: "))

percentB = v_branco / eleitores * 100
percentN = v_nulo / eleitores * 100
percentV = v_validos / eleitores * 100

print(f"{percentB:.2f}%")
print(f"{percentN:.2f}%")
print(f"{percentV:.2f}%")