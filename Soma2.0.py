N1=int(input("Digite o Primeiro Numero:"))
print("\n")
OPERACAO = input("Digite a operação (+, -, *, /): ") 
print("\n")
N2=int(input("Digite o Segundo Numero:"))
print("\n")
if OPERACAO == "+":
    resultado = N1+N2
elif OPERACAO == "-":
    resultado = N1-N2
elif OPERACAO == "*":
    resultado = N1*N2
elif OPERACAO == "/":
    if N2 != 0:
     resultado = N1/N2
    else:
       print("Impossível dividir por 0")
else:
   print("Operação indisponível")

print(f"Resultado: {resultado}")
