# Faça uma função que recebe um n1 inteiro e retorna uma mensagem que informa se
# o n1 é par ou ímpar

def funcao_n1(n1):
    if n1 % 2 == 0:
        print("par")
    else:
        print("impar")
    return n1


v1 = int(input("n1 Inteiro: "))
funcao_n1(v1)