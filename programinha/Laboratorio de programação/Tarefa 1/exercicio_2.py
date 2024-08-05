# Escreva um programa que solicite um número ao usuário e determine se o número é
# par ou ímpar. Em seguida, imprima na tela uma mensagem indicando o resultado

numero = int(input("ESCREVA UM NUMERO: "))

resto = numero % 2

if resto == 0:
    print(f"O numero {numero} é par")
else:
    print(f"O numero {numero} é impar")