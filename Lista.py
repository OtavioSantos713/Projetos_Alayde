itens = []

for i in range(5):
    item = input(f"Digite o {i+1}º item: ")
    itens.append(item)

print("\nVocê digitou os seguintes itens:")
for i, item in enumerate(itens, start=1):
    print(f"{i}. {item}")