# Faça uma função que recebe as 3 notas de um aluno por parâmetro e uma letra, que
# indicará o tipo da média a ser calculada. Caso a letra seja A, a função deve calcular a
# média aritmética das notas do aluno, se for P, deve ser calculada a média ponderada
# (pesos: 5, 3 e 2 respectivamente). O cálculo da média deve ser retornado pela função.
# Na chamada da função, as 3 notas devem ser informadas pelo usuário e as notas podem
# ser fracionadas (por exemplo, 7.5 ou 8.5).

def funcao(n1,n2,n3,L):
    if L == "A":
        Media = (n1 + n2 + n3)/3
    if L == "P":
        Media = ((n1*5+n2*3+n3*2)/(5+2+3))
    return Media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
tipo_media = input("Digite o tipo de média ('A' para aritmética ou 'P' para ponderada): ")

resultado = funcao(nota1,nota2,nota3,tipo_media)

print(resultado)
