# Faça uma função que recebe a idade de uma pessoa em anos, meses e dias (um
# parâmetro para anos, outro para meses e outro para dias) e retorne essa idade em dias.
# Considere que um ano tem 360 dias e os meses são de 30 dias

def idade(Ano,Meses,Dias):
    Idade_em_Dias = (Ano*360 + Meses*30 + Dias)
    print(Idade_em_Dias)

anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))
idade_em_dias = idade(anos,meses,dias)