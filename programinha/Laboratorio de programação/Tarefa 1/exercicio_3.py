# Desenvolva um programa que receba a idade do usuário e determine se ele é maior de
# idade (idade igual ou superior a 18 anos). Em seguida, exiba uma mensagem indicando
# se ele é maior de idade ou não

idade_usuario = int(input("Escreva sua idade: "))

print("---------------------------")

if idade_usuario >= 18:
    print(f"Voce é maior de idade: {idade_usuario} anos!")
else:
    Faltam_para_maior_idade = 18 - idade_usuario
    print(f"Voce é menor de idade: {idade_usuario} anos!")
    print(f"Faltam {Faltam_para_maior_idade} ano(s) para voce completar a maior idade!")
