# Faça uma função que recebe 3 valores reais X, Y e Z e que verifica se esses valores podem
# ser os comprimentos dos lados de um triângulo. Caso seja um triângulo, deve retornar
# o tipo que triângulo que os lados formam, caso contrário retorna uma mensagem
# informando que não é um triângulo.
# Obs: Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade
# seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do
# comprimento dos outros dois lados.
# A função deve identificar o tipo de triângulo formado observando as seguintes
# definições:
# Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
# Triângulo Isósceles: os comprimentos de 2 lados são iguais.
# Triângulo Escaleno: os comprimentos dos 3 lados são diferentes


def verificar_triangulo(x, y, z):
    if (x + y > z) and (x + z > y) and (y + z > x):
        if x == y == z:
            return "Triângulo Equilátero"
        elif x == y or y == z or x == z:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Os valores fornecidos não formam um triângulo."


x = float(input("Digite o comprimento do primeiro lado: "))
y = float(input("Digite o comprimento do segundo lado: "))
z = float(input("Digite o comprimento do terceiro lado: "))
    
resultado = verificar_triangulo(x, y, z)
print(resultado)
    
