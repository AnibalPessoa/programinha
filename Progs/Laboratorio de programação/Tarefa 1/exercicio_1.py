# Faça um programa que solicite 5 números ao usuário e apresente a média dos valores.
# Para a leitura dos valores, utilize laços de repetição

i = 0
num = 0

while i < 5:
    numeros = int(input("Escolha um numero para entrar na média: "))
    num = numeros + num
    

    i = i + 1

media = num/5
print(f"A media dos valores dados é: {media}")