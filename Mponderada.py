n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

media = (n1*2 + n2*3 + n3*5) / 10

print(f"\nMédia final: {media:.2f}")

if media >= 5:
    situacao = "Aprovado"
elif media >= 3:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Situação:", situacao)
