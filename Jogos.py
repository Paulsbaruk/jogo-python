print("*******************************")
print("******Escolha o seu jogo!******")
print("*******************************")

print("(1) Forca (2) adivinhação")

jogo = int(input("Qual jogo?"))
if(jogo == 1):
    print("jogando forca")
    import jogodaforca
elif(jogo == 2):
    print("jogando adivinhação")
    import advinhacao