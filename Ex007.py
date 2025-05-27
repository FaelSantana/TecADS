#Troca de Valores
def switch_values(fv,sv):
    tv = fv
    fv = sv
    sv = tv
    return fv,sv

firt_value = input('Digite um valor: ')
sec_value = input('Digite outro valor: ')

print(f'Valores trocados {switch_values(firt_value,sec_value)}')
