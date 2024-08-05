# Faça um programa que solicite ao usuário o valor de um produto e aplique um
# desconto de 10%. Em seguida, exiba o valor final com o desconto aplicado

Valor = float(input("Insira o valor do produto a ser aplicado o desconto: "))

desconto = Valor * 0.1
Valor_Com_Desconto = Valor - desconto

print(f"O valor é {Valor}\nO valor com desconto será {Valor_Com_Desconto}\nO desconto foi de {desconto}")