NOTA1 = float(input("Digite sua Primeira Nota: "))
NOTA2 = float(input("Digite sua Segunda Nota: "))
NOTA3 = float(input("Digite sua Terceira Nota: "))

SOMA = ( NOTA1 + NOTA2 + NOTA3 ) /3
print("Sua Media será: ",SOMA)

if SOMA>6:
    print("🎉Você Passou🎉")
elif SOMA<6:
    print("💀Você Reprovou💀")