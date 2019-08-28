import random

print("*******************************")
print("Welcome to the game of guessing")
print("*******************************")


numero_secreto = random.randrange(1,101)
total_de_tentativas = 0
pontos = 1000
error = ""
print("Which level do you wanna play?",numero_secreto)
print("(1) easy (2) intermediate (3) high advanced")
try:
   level = int(input("Chose your level to play:"))
except ValueError:
    print('coloque um numero')
    exit()
if(level == 1):
    total_de_tentativas = 20
elif(level == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


print(numero_secreto)
for rodada in range(1, total_de_tentativas+1):
    print("Tentativa {} de {}". format (rodada, total_de_tentativas))
    chute_str = input("Type your number among 1 to 100:")

    print("You typed" , chute_str)
    try:
        chute = int(chute_str)
    except:
        print('coloque numeros')
        continue
    if(chute < 1 or chute > 100):
        print("You should have typed a number among 1 to 100!")
        continue
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format (pontos))
        break
    else:
        if(maior):
            print("Você errou!O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! seu numero_secreto foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) # 40-20 = 20
            pontos = pontos - pontos_perdidos
            print(error)


print("Game over")