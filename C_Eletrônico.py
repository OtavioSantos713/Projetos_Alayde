print("Olá usuário!")
valor = int(input("Digite o valor: ")) 

notas = [200, 100, 50, 20, 10, 5] 

for nota in notas: 
 quantidade = valor // nota 
 if quantidade > 0: 
  print(f"Notas de {nota}: {quantidade}") 
  valor = valor % nota 