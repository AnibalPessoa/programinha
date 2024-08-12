# Faça uma função que verifique se um valor é perfeito ou não. Um valor é perfeito
# quando ele é igual a soma dos seus divisores, exceto ele próprio. (por exemplo, 6 é
# perfeito, pois 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor
# booleano: True se é perfeito e False se não for perfeito. Pesquise na internet por outros
# números considerados perfeitos e teste sua função.

def e_numero_perfeito(n):
    if n <= 1:
        return False
    
    soma_divisores = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            soma_divisores += i
    
    return soma_divisores == n

testes = [6, 28, 496, 8128, 12, 15, 18]

for numero in testes:
    resultado = e_numero_perfeito(numero)
    print(f"O número {numero} é perfeito? {resultado}")

#nao consegui, peguei do gpt