#Converte de Decimal pra Binário
def dec_bin(n:int)->list:
    bin = []
    while n > 0:
        rest = n % 2
        n = n // 2
        bin.append(str(rest))
        pass
    bin.reverse()
    return '-'.join(bin)

#Converte de Binário pra Decimal
def bin_dec(bin:str)->int:
    cont = len(bin)
    dec = 0
    for n in bin:
        cont -= 1
        dec += int(n)*(2**cont)
        pass
    return dec

number = input('Digite um Número: ')
if int(input('\tDigite [1] para Converter pra Binário\n\tDigite [2] para converter para Decimal: ')) == 1:
    print(f'O Número {number} em Binário é: {dec_bin(number)}')
else:
    print(f'O Número {number} em Decimal é {bin_dec(number)}')
    pass
