n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2:
   if n1 > n3:
       print(n1)
   else:
       print(n3)

elif n2 > n3:
   print(n2)

else:
   print (n3)