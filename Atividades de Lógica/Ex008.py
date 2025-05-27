#Números negativos
def cont_neg(lista:list)->int:
    negativos = 0
    for x in lista:
        if x < 0:
            negativos += 1
            pass
    return negativos

valores = [int(input('Digite um valor: ')) for x in range(4)]
print(f'Você digitou {cont_neg(valores)} Número(s) Negativos')
