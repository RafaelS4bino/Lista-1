numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
numero_3 = float(input("Digite o terceiro numero: "))

if numero_1 >= numero_2 and numero_1 >= numero_3:
    print(f"O {numero_1} é maior!")
elif numero_2 > numero_1 and numero_2 >= numero_3:
    print(f"O {numero_2} é maior!")
else:
    print(f"o {numero_3} é maior!")
