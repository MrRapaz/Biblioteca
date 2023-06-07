contador = 1

while(contador!= 0):
    contador= int(input('digite 0 quando quiser sair:'))
    print('tipo de pessoa: | 1=funcionario, 2=leitor, 3=livro, 4= Emprestimo')
    pesTipo = int(input('informe o tipo da pessoa'))

    if pesTipo == 1:
        print('Digite o nome do funcionario: ')
        nomeF = input()
        print('Digite o ID funcionario: ')
        idF = input()
        print('Digite seu CPF funcionario: ')
        cpfF = input()
        print('Digite o ID da pessoa que quer movimentar: ')
        idP = input()
    else: 
        if pesTipo == 2:
            print('Digite o nome leitor: ')
            nomeP = input()
            print('Digite o ID leitor: ')
            idP = input()
            print('Digite seu CPF leitor: ')
            cpfP = input()
        else:
            if pesTipo == 3:
                print('Digite o autor do livro: ')
                nomeL = input()
                print('Digite o ID  do livro: ')
                idL = input()
            else:
                if pesTipo == 4:
                    print('Digite a data deste emprestimo: ')
                    dataEmp = input()
                    Emprestimo(idL,idF,dataEmp)


class Emprestimo(idL,idF,dataEmp):
    idEmpL: idL
    idEmpF: idF
    dataEmp : dataEmp