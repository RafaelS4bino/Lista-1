turno = input("Em qual turno você estuda? ").lower()

if turno in 'm':
    print("Bom dia!")

elif turno in 'v':
    print("Boa tarde!")

elif turno in 'n':
    print("Boa Noite!")

else:
    print("Valor inválido!")