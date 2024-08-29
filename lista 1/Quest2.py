num1 = input("Digite um numero: ")
num2 = input("Digite outro numero: ")

if (int(num1 > num2)):
    print(f"o {num1} é maior")
elif (int(num1 < num2)):
    print(f"o {num2} é maior")
else:
    print("Numeros iguais")