print("Seja muito bem vindo ao quiz!")
answer_user = input("Quer começar? (S/N)")

if answer_user != 'S':
    quit()

score = 0

print("Começando...\n")
print("Quem desenvolveu o jogo Grand Theft Auto(GTA)? \n (A) Rockstar Game \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == 'A':
    print("Correto!\n")
    score = score + 1
else:
    print('Incorreto!')

print("Qual o nome do protagonista do jogo Grand Theft Auto(GTA)? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n")
answer_2 = input("Resposta: ")

if answer_2 == 'B':
    print("Correto!\n")
    score = score + 1
else:
    print('Incorreto!')

print("Qual foi o ano de lançamento do jogo Grand Theft Auto(GTA)? \n (A) 1998 \n (B) 2000 \n (C) 1989 \n (D) 2002 \n")
answer_3 = input("Resposta: ")

if answer_3 == 'A':
    print("Correto!\n")
    score = score + 1
else:
    print('Incorreto!')

print(f'Quiz acabou...\nPontuação: {score}/3')