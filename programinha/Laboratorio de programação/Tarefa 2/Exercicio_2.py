# Crie uma função que que receba como parâmetro um valor lido do teclado e imprima para
# o usuário, a mensagem “O valor {N} informado é positivo” ou a mensagem “O valor {N}
# informado é negativo”

def Verificar_numero():
    numero = int(input("Numero: "))
    
    if numero > 0:
        print(f"O Numero {numero} é positivo.")
    elif numero < 0:
        print(f"O Numero {numero} é negativo.")
    else:
        print(f"O Numero {numero} é zero.")

Verificar_numero()