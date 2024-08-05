# Crie um jogo de adivinhação de números da seguinte forma:
# O computador deve selecionar aleatoriamente um número inteiro entre 0 e 100.
# * Pesquise como pegar valores aleatórios (randômicos no Python).

# O computador fica solicitando números ao jogador, até que ele adivinhe o número
# selecionado, sendo que a cada tentativa errada do usuário, o computador deve
# informar se o palpite digitado é maior ou menor que o número selecionado (que
# deve ser encontrado).

# Quando o jogador acertar o número, deve ser apresentada uma mensagem com o
# seguinte modelo:
# ****************************************
# Parabéns!!!! O número correto é 41
# Quantidade de tentativas --> 9
# ***************************************

# Após a finalização da partida, o computador faz a pergunta “Jogar novamente?”,
# sendo que fica em execução enquanto o usuário responder ‘s’ para essa pergunta.

import random

numero_aleatorio = random.randint(0, 100)
tentativas = 0

continuar = "s"
while continuar == "s":
    pergunta = int(input("Escolha um numero entre 0 e 100: "))
    if pergunta == numero_aleatorio:
        tentativas = tentativas + 1
        print(f"****************************************")
        print(f"Parabéns!!!! O número correto é {numero_aleatorio}")
        print(f"Quantidade de tentativas --> {tentativas}")
        print(f"****************************************")
        tentativas = 0
        numero_aleatorio = random.randint(0, 100)
        continuar = input("Jogar Novamente? ")
        
    elif pergunta > numero_aleatorio:
        tentativas = tentativas + 1
        print(f"O numero escolhido '{pergunta}' é maior que o gerado aleatoriamente")

    else:
        tentativas = tentativas + 1
        print(f"O numero escolhido '{pergunta}' é menor que o gerado aleatoriamente")
        