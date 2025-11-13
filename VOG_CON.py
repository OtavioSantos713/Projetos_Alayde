letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("É uma vogal.")

elif letra.isalpha():
    print("É uma consoante.")
    
else:
    print("Não é uma letra.")

