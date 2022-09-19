

numero_secreto= 42



chute_str = input("Digite o seu número: ")
print("você digitou", chute_str)

chute= int(chute_str)

if(numero_secreto == chute):
    print("Você Acertoou !!")

else:
    print("Que Pena, tente de novo!!")
