import random




print("===========================================")
print("JOGO DE ADIVINHAÇÃO COM PYTHON - PROJETO 01")
print("===========================================")

pontos = 500
numero_secreto = round(random.random() * 100)
numero_tentativas = 0

print("Qual o Nível de Dificuldade?")
print("(1) Fácil   (2) Médio  (3) Difícil")

nivel=int(input("Digite o número para definir nível:"))
if nivel == 1:
    numero_tentativas=10
elif nivel == 2:
    numero_tentativas=8
else:
    numero_tentativas=5


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
        print("Você acertou! e consegui incríveis ", pontos," pontos!!")
        break
    else:
        if(maior):
            print("Que Pena! Tente um número Menor na próxima vez!")
        elif(menor):
            print("Que Pena! Tente um número Maior na próxima vez!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    if rodada >= numero_tentativas:
        print("O número Secreto Era", numero_secreto)

print("Fim do jogo")
