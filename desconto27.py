valor = float(input("Digite o valor total da compra: R$ "))

if valor <= 100:
    percentual = 5
elif valor <= 300:
    percentual = 10
else:
    percentual = 15

desconto = valor * (percentual / 100)
valor_final = valor - desconto

print("\n--- Resultado ---")
print(f"Valor original: R$ {valor:.2f}")
print(f"Percentual de desconto aplicado: {percentual}%")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
