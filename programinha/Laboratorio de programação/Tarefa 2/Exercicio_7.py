# Faça uma função que recebe por parâmetro o tempo representado em segundos e
# retorne esse tempo em horas, minutos e segundos. A hora completa deve ser retornada
# em uma variável no seguinte formato “Horas:Minutos:Segundos”, por exemplo, se for
# passado por parâmetro 3800 segundos para o método, este deverá retornar “1:3:20”,
# que indica, 1 hora, 3 minutos e 20 segundos. ATENÇÃO: Para formatar a variável de
# retorno, você precisará converter os valores para string. Para isso, utilize a função
# str(), que recebe um número inteiro por parâmetro e o converte para string

def tempo(segundos):
    hora = segundos // 3600
    minuto = (segundos % 3600) // 60 
    segundo = (segundos % 3600) % 60 

    resultado = f"{hora}:{minuto}:{segundo}"
    return resultado

tempo_resultado = int(input("Tempo em segundos: "))
resultado = tempo(tempo_resultado)
print(resultado)