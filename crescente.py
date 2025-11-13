print("Olá usuário!") # Imprime a mensagem inicial
numeros = [] # Cria uma lista vazia para armazenar os números
for i in range(5): # Loop que repete 5 vezes
 num = int(input("Digite o {i+1}º número desejado:")) # Ped ecada número ao usuário

numeros.append(num) # Adiciona o número à lista
numeros.sort() # Ordena a lista em ordem crescente
print("Números em ordem crescente:", numeros) # Exibe a lista ordenada