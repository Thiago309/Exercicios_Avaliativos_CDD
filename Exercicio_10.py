a = 0
b = 0
c = 0
while True:

    n = int(input("Digite o valor que deseja calcular: "))
    opc = int(input("Digite qual função você deseja usar [1 ~ Antecessor], [2 ~ Sucessor] & [3 ~ Sair]: "))


    if (opc == 1):
        a = n - 1
        print("Função [Antecessor] selecionada !!!")
        print(f"O antecessor de {n} é: {a}")

    elif (opc == 2):
        s = n + 1
        print("Função [Sucessor] selecionada !!!")
        print(f"O sucessor de {n} é: {s}")

    else:
        print("Obrigado(a) por usar nossos serviços, até a próxima !")
        break