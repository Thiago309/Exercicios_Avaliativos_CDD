n1 = float(input("Digite o valor 1: "))
n2 = float(input("Digite o valor 2: "))

if (n1 > n2):
    print(n1, n2, end = "")

elif (n1 < n2):
    print(n2, n1, end = "")

else:
    print("Valores semelhantes, o calculo só poderá ser realizado com valores distinstos!")