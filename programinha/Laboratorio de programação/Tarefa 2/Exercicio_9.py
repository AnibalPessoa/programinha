# Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e
# retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal
# = 72.7 x alt - 58 e ,para mulheres, peso ideal = 62.1 x alt - 44.7

def calcular_peso_ideal(altura, sexo):
   
    if sexo == 'M':
        peso_ideal = 72.7 * altura - 58
    elif sexo == 'F':
        peso_ideal = 62.1 * altura - 44.7
    
    return peso_ideal

altura = float(input("Digite a altura em metros: "))
sexo = input("Digite o sexo ('M' para masculino e 'F' para feminino): ")
peso_ideal = calcular_peso_ideal(altura, sexo)
print(f"O peso ideal é: {peso_ideal} kg")