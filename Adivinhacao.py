print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 51
numero_tentativas = 5

for rodada in range(1, numero_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, numero_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Que Pena! Tente um número Menor na próxima vez!")
        elif(menor):
            print("Que Pena! Tente um número Maior na próxima vez!")

print("Fim do jogo")