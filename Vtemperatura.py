temperaturas = []

soma = 0

for i in range(30):
    temp = float(input(f"Temperatura do dia {i+1}: "))
    temperaturas.append(temp)
    soma += temp

media_mes = soma / 30
maior = max(temperaturas)
menor = min(temperaturas)
dias_acima = sum(1 for t in temperaturas if t > 27.3)

print("\n--- Resultados ---")
print(f"Média do mês: {media_mes:.2f}°C")
print(f"Maior temperatura: {maior:.2f}°C")
print(f"Menor temperatura: {menor:.2f}°C")
print(f"Dias acima de 27,3°C: {dias_acima}")
