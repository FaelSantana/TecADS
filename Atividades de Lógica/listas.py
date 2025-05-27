from time import sleep
#Listas
'''
alunos = ['Thiago','Pedro','Bianca','Jessica','Bruno']
alunos.insert(1,'Daniela')
print(alunos)
'''
#Programa
Cadastro = []
while True:
    print('-'*20)
    print(f'{"Cadastrando Pessoas":^20}')
    print('-'*20)
    print('\t1- Adicionar Nome\n\t2- Listar nomes\n\t3- Remover Nome\n\t4- Sair')
    opt = int(input('Digite uma opção: '))

    if opt == 1:
        Cadastro.append(input('Digite o Nome da pessoa: '))
        print('\033[0;32;40mPessoa Cadastrada com sucesso\033[0m')
    elif opt == 2:
        print(f'\033[0;33;40mNomes Cadastrados{Cadastro}\033[0m')
    elif opt == 3:
        try:
            print(Cadastro)
            pos = input('Digite o Nome na lista: ')
            Cadastro.pop(Cadastro.index(pos))
            print('\033[0;32;40mPessoa Removida com sucesso\033[0m')
        except ValueError:
            print('\033[0;31;40mEssa pessoa não está Cadastrada!\033[0m')
    elif opt == 4:
        print('\033[0;33;40mEncerrando Programa...\033[0m')
        sleep(0.3)
        print('\033[0;31;40mPrograma Encerrado!!\033[0m')
        break
    else: print('Opção Inválida!! Tente Novamente')

