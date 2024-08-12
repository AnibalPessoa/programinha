# Faça uma função que recebe 3 valores inteiros por parâmetro e retorna-os ordenados
# em ordem crescente. Os valores retornados devem estar separados por vírgula (,) e para
# serem retornados como uma string, cada nor deve ser convertido para uma string com
# o uso da função str(), que recebe por parâmetro um número e retorna uma string



def valores(n1,n2,n3):
    valores_em_lista = [n1,n2,n3]
    valores_em_lista_em_ordem = sorted(valores_em_lista)
    resultado = ','.join(str(nor) for nor in valores_em_lista_em_ordem)
    #peguei do gpt, nao faço a menor ideia de como que faz essa linha de cima
    return resultado

n1 = int(input("Digite o primeiro valor inteiro: "))
n2 = int(input("Digite o segundo valor inteiro: "))
n3 = int(input("Digite o terceiro valor inteiro: "))

resultado = valores(n1,n2,n3)
print(resultado)