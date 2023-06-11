class Emprestimo:
    def __init__(self, id_emprestimo, nome_leitor, nome_livro):
        self.id_emprestimo = id_emprestimo
        self.nome_leitor = nome_leitor
        self.nome_livro = nome_livro

emprestimos = [] 

def cadastrar_emprestimo():
    id_emprestimo = int(input("Digite o ID do empréstimo: "))
    nome_livro = input("Digite o nome do livro: ")
    nome_leitor = input("Digite o nome do leitor: ")
    emprestimo = Emprestimo(id_emprestimo, nome_livro, nome_leitor)
    return emprestimo

def listar_emprestimo(emprestimos):
    if len(emprestimos) == 0:
        print("Não há empréstimos cadastrados!")
    else:
        print("Lista de empréstimos:")
        for emprestimo in emprestimos:
            print(f"----------- \nID: {emprestimo.id_emprestimo} \nNome Livro: {livro.nome_livro} \nNome Leitor: {leitor.nome_leitor}")

def listar_emprestimo_codigo(emprestimos):
    if len(emprestimos) == 0:
        print("Não há empréstimos cadastrados!")
    else:
        id_emprestimo = int(input("Digite o ID do empréstimo a ser listado: "))
        for emprestimo in emprestimos:
            if emprestimo.id_emprestimo == id_emprestimo:
                print(f"----------- \nID: {emprestimo.id_emprestimo} \nNome Livro: {livro.nome_livro} \nNome Leitor: {leitor.nome_leitor}")

def remover_emprestimo(emprestimos):
    id_emprestimo = int(input("Digite o ID do empréstimo a ser removido: "))
    for emprestimo in emprestimos:
        if emprestimo.id_emprestimo == id_emprestimo:
            emprestimos.remove(emprestimo)
            print("Empréstimo removido com sucesso.")
            return
    print("Empréstimo não encontrado.")

def atualizar_emprestimo(emprestimos):
    id_emprestimo = int(input("Digite o ID do empréstimo a ser atualizado: "))
    for emprestimo in emprestimos:
        if emprestimo.id_emprestimo == id_emprestimo:
            novo_nome_livro = input("Digite o nome do livro para atualizar o empréstimo: ")
            emprestimo.nome_emprestimo = novo_nome_livro
            print("Empréstimo atualizado com sucesso.")
            return
    print("Empréstimo não encontrado.")

while True:
    print("\nMenu:")
    print("Digite 0 - Sair \nDigite 1 - Cadastrar leitor \nDigite 2 - Listar leitores \nDigite 3 - Listar leitor por ID \nDigite 4 - Remover leitor "
         +"\nDigite 5 - Atualizar leitor \nDigite 6 - Cadastrar livro \nDigite 7 - Listar livros \nDigite 8 - Listar livro por ID \nDigite 9 - Remover livro "
         +"\nDigite 10 - Atualizar livro \nDigite 11 - Cadastrar empréstimo \nDigite 12 - Listar empréstimo \nDigite 13 - Listar empréstimo por ID \nDigite 14 - Remover empréstimo "
         +"\nDigite 15 - Atualizar empréstimo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pass
    else:
        if opcao == "2":
            pass
        else:
            if opcao == "3":
                pass
            else:
                if opcao == "4":
                    pass
                else:
                    if opcao == "5":
                        pass
                    else:
                        if opcao == "6":
                            pass
                        else:
                            if opcao == "7":
                                pass
                            else:
                                if opcao == "8":
                                    pass
                                else:
                                    if opcao == "9":
                                        pass
                                    else:
                                        if opcao == "10":
                                            pass
                                        else:
                                            if opcao == "11":
                                                emprestimo = cadastrar_emprestimo()
                                                emprestimos.append(emprestimo)
                                                print("Empréstimo cadastrado com sucesso!")
                                            else:
                                                if opcao == "12":
                                                    listar_emprestimo(emprestimos)
                                                else:
                                                    if opcao == "13":
                                                        listar_emprestimo_codigo(emprestimos)
                                                    else:
                                                        if opcao == "14":
                                                            remover_emprestimo(emprestimos)
                                                        else:
                                                            if opcao == "15":
                                                                atualizar_emprestimo(emprestimos)
                                                            else:
                                                                if opcao == "0":
                                                                    exit()
                                                                else:
                                                                    print("Opção inválida. Tente novamente.")