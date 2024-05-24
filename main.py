import random

print("+-------------------------------------+")
print("+ Bem Vindo ao Jogo do Número Secreto +")
print("+-------------------------------------+")

print("Você quer jogar na dificuldade dificil, mediano ou fácil?")
dificuldade = input("[d,m,f]:")
tentativas_maximas = 5

if dificuldade == "d":
  tentativas_maximas = 3
elif dificuldade == "m":
  tentativas_maximas = 5
elif dificuldade == "f":
  tentativas_maximas = 10
else:
  print("Você não definiu a dificuldade, sua dificuldade foi alterada para mediano")

numero_secreto = random.randint(1, 100)
tentativas = 1

while tentativas <= tentativas_maximas:
  print("Tentativa", tentativas, "de", tentativas_maximas,":")
  numero_usuario = int(input("Chute o número secreto: "))
  
  if numero_secreto == numero_usuario:
    print("Você acertou!")
    break
    # tentivas = 4
  elif numero_secreto > numero_usuario:
    print("O número secreto é maior!")
  else:
    print("O número secreto é menor!")

  # tentativas = tentativas + 1
  tentativas += 1

if tentativas > tentativas_maximas:
  print("Você perdeu! tentativas excedidas! O número secreto era", numero_secreto)
else:
  print("Parabéns! Você ganhou o jogo!")