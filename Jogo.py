import random 

numeropc = random.randint(1, 20) 
print("Olá usuário!")
print("Tente adivinhar o número que o programa escolheu.") 

while True: 
    tentativa = int(input("Digite seu palpite: ")) 

    if tentativa == numeropc: 
        print("Parabéns, você acertou!") 
        break 
    elif tentativa > numeropc: 
        print("Você errou. O número é menor.") 
    elif tentativa < numeropc: 
        print("Você errou. O número é maior.") 