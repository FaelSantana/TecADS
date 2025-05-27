#Verificação de idade para dirigir
def verif_idade(idade:int)->str:
    if idade >= 18:
        return 'Maior de idade'
    else: return 'Menor de idade'


idade = int(input('Digite sua idade: '))
print(verif_idade(idade))
