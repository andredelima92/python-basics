import random

randomNumber = random.randrange(1, 10)

print(randomNumber)

choice = int(input("Selecione um numero de 1 a 10\n"))

if (choice == randomNumber):
    print("Parabéns você acertou o numero")
else:
    print("Infelizmente você errou o numero")
