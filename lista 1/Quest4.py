
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2)/2

if media >= 10:
    print(f"Aprovado com distição, sua media foi: {media}!")
elif media >= 7:
    print(f"Aprovado, sua media foi: {media}!")
else:
    print(f"reprovado, sua media foi: {media}!")
