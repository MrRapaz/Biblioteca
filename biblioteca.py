class Leitor:
    def __init__(self, id_leitor, nome_leitor):
        self.id_leitor = id_leitor
        self.nome_leitor = nome_leitor
        
class Livro:
    def __init__(self, id_livro, nome_livro, autor_livro):
        self.id_livro = id_livro
        self.nome_livro = nome_livro
        self.autor_livro = autor_livro

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

leitores = []

def cadastrar_leitor():
    id_leitor = int(input("Digite o ID do leitor: "))
    nome_leitor = input("Digite o nome do leitor: ")
    leitor = Leitor(id_leitor, nome_leitor)
    return leitor

def listar_leitores(leitores):
    if len(leitores) == 0:
        print("Não há leitores cadastrados!")
    else:
        print("Lista de leitores:")
        for leitor in leitores:
            print(f"----------- \nID: {leitor.id_leitor}  \nNome: {leitor.nome_leitor} \n-----------")

def listar_leitor_codigo(leitores):
    if len(leitores) == 0:
        print("Não há leitores cadastrados: ")
    else:
        id_leitor = int(input("Digite o ID do leitor a ser listado: "))
        for leitor in leitores:
            if leitor.id_leitor == id_leitor:
                print(f"----------- \nID: {leitor.id_leitor}  \nNome: {leitor.nome_leitor} \n-----------")

def remover_leitor(leitores):
    id_leitor = int(input("Digite o ID do leitor a ser removido: "))
    for leitor in leitores:
        if leitor.id_leitor == id_leitor:
            leitores.remove(leitor)
            print("Leitor removido com sucesso.")
            return
    print("Leitor não encontrado.")

def atualizar_leitor(leitores):
    id_leitor = int(input("Digite o ID do leitor a ser atualizado: "))
    for leitor in leitores:
        if leitor.id_leitor == id_leitor:
            novo_nome = input("Digite o novo nome do leitor: ")
            leitor.nome_leitor = novo_nome
            print("leitor atualizado com sucesso.")
            return
    print("leitor não encontrado.")

livros = []

def cadastrar_livro():
    id_livro = int(input("Digite o ID da Livro: "))
    nome_livro = input("Digite o nome da Livro: ")
    autor_livro = input("Digite o autor da Livro: ")
    livro = Livro(id_livro, nome_livro, autor_livro)
    return livro

def listar_livros(Livros):
    if len(Livros) == 0:
        print("Não há Livros cadastradas.")
    else:
        print("Lista de Livros:")
        for Livro in Livros:
            print(f"----------- \nID: {Livro.id_livro}  \nNome: {Livro.nome_livro}  \nAutor: {Livro.autor_livro} \n-----------")

def listar_livro_codigo(Livros):
    if len(Livros) == 0:
        print("Não há livros cadastrados: ")
    else:
        id_livro = int(input("Digite o ID do Livro a ser listado: "))
        for Livro in Livros:
            if Livro.id_livro == id_livro:
                print(f"----------- \nID: {Livro.id_livro}  \nNome: {Livro.nome_livro}  \nAutor: {Livro.autor_livro} \n-----------")

def remover_livro(Livros):
    id_livro = int(input("Digite o ID do Livro a ser removido: "))
    for Livro in Livros:
        if Livro.id_livro == id_livro:
            Livros.remove(Livro)
            print("Livro removido com sucesso.")
            return
    print("Livro não encontrado.")

def atualizar_livro(Livros):
    id_livro = int(input("Digite o ID do Livro a ser atualizado: "))
    for Livro in Livros:
        if Livro.id_livro == id_livro:
            novo_nome = input("Digite o novo nome da Livro: ")
            Livro.nome_livro = novo_nome
            print("Livro atualizada com sucesso.")
            return
    print("Livro não encontrada.")

while True:
    print("\nMenu:")
    print("Digite 0 - Sair \nDigite 1 - Cadastrar leitor \nDigite 2 - Listar leitores \nDigite 3 - Listar leitor por ID \nDigite 4 - Remover leitor "
         +"\nDigite 5 - Atualizar leitor \nDigite 6 - Cadastrar livro \nDigite 7 - Listar livros \nDigite 8 - Listar livro por ID \nDigite 9 - Remover livro "
         +"\nDigite 10 - Atualizar livro \nDigite 11 - Cadastrar empréstimo \nDigite 12 - Listar empréstimo \nDigite 13 - Listar empréstimo por ID \nDigite 14 - Remover empréstimo "
         +"\nDigite 15 - Atualizar empréstimo")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        leitor = cadastrar_leitor()
        leitores.append(leitor)
        print("Leitor cadastrado com sucesso!")
    else:
        if opcao == "2":
            listar_leitores(leitores)
        else:
            if opcao == "3":
                listar_leitor_codigo(leitores)
            else:
                if opcao == "4":
                    remover_leitor(leitores)
                else:
                    if opcao == "5":
                        atualizar_leitor(leitores)
                    else:
                        if opcao == "6":
                            livro = cadastrar_livro()
                            livros.append(livro)
                            print("Livro cadastrado com sucesso!")
                        else:
                            if opcao == "7":
                                listar_livros(livros)
                            else:
                                if opcao == "8":
                                    listar_livro_codigo(livros)
                                else:
                                    if opcao == "9":
                                        remover_livro(livros)
                                    else:
                                        if opcao == "10":
                                            atualizar_livro(livros)
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