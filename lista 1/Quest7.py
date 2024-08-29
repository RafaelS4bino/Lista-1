classificação = 0

print("Você está sendo interrogado!")
print("Perguntas seram feitas para saber o seu paradeiro sobre o caso, por favor responda as perguntas com Verdadeiro ou Falso!")

pergunta_1 = input("Telefonou para a vítima? ").lower()

if pergunta_1 == "verdadeiro":
    classificação += 1

pergunta_2 = input("Esteve no local do crime? ").lower()

if pergunta_2 == "verdadeiro":
    classificação += 1

pergunta_3 = input("Mora perto da vitima? ").lower()

if pergunta_3 == "verdadeiro":
    classificação += 1

pergunta_4 = input("Devia para a vitima? ").lower()

if pergunta_4 == "verdadeiro":
    classificação += 1

pergunta_5 = input("Ja trabalhou com a vitima? ").lower()

if pergunta_5 == "verdadeiro":
    classificação += 1



if classificação == 5:
    print("Assassino!")

elif classificação == 2:
    print("Suspeito!")

elif classificação == 0:
    print("Inocente!")

else:
    print("cumplice!")