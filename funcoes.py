
import random
from classes import Livro, Revista, Bibliotecario, Cliente

clientes = []
livros = []
revistas = []

# ===== Função para cadastrar livros =====
def cadastrar_livro():
    while True:
        print("\n--- Cadastro de Livro ---")
        categoria = input("Categoria: ")
        titulo = input("Título: ")
        editora = input("Editora: ")
        
        try:
            preco = float(input("Preço: "))
        except ValueError:
            print("Preço deve ser numérico (use ponto para decimais).")
            continue  # volta para o início do while
        
        autor = input("Autor: ")
        
        try:
            novo_livro = Livro(categoria, titulo, editora, preco, autor)
            livros.append(novo_livro)
            print("\nLivro cadastrado com sucesso!")
            print(novo_livro.mostrar_informacoes())
            
            print("\nLivros cadastrados até agora:")
            for l in livros:
                print("-", l.mostrar_informacoes())
        except ValueError as e:
            print("Erro ao cadastrar livro:", e)
            continue  # volta para tentar de novo

        opc = input("\nDeseja cadastrar outro livro? (s/n): ")
        if opc.lower() != 's':
            break
        
        
# ===== Função para cadastrar Revista =====        
def cadastrar_revista():
    while True:
        print("\n--- Cadastro de Revista ---")
        categoria = input("Categoria: ")
        titulo = input("Título: ")
        editora = input("Editora: ")
        
        try:
            preco = float(input("Preço: "))
        except ValueError:
            print("Preço deve ser numérico (use ponto para decimais).")
            continue  # volta para o início do while

        try:
            edicao = int(input("Edição (número inteiro positivo): "))
        except ValueError:
            print("Edição deve ser um número inteiro.")
            continue  # volta para o início do while

        try:
            nova_revista = Revista(categoria, titulo, editora, preco, edicao)
            revistas.append(nova_revista)
            print("\nRevista cadastrada com sucesso!")
            print(nova_revista.mostrar_informacoes())
            
            print("\nRevistas cadastradas até agora:")
            for r in revistas:
                print("-", r.mostrar_informacoes())
        except ValueError as e:
            print("Erro ao cadastrar revista:", e)
            continue  # volta para tentar de novo

        opc = input("\nDeseja cadastrar outra revista? (s/n): ")
        if opc.lower() != 's':
            break

# ===== Função para cadastrar clientes =====
def cadastrar_cliente():
    while True:
        print("\n--- Cadastro de Cliente ---")
        nome = input("Nome: ")
        cpf = input("CPF (11 dígitos): ")
        telefone = input("Telefone (11 dígitos, DDD + número): ")
        id_cliente = random.randint(1, 9999)

        try:
            novo_cliente = Cliente(nome, cpf, telefone, id_cliente)
            clientes.append(novo_cliente)
            print("\nCliente cadastrado com sucesso!")
            print(novo_cliente.mostrar_informacoes_cliente())
        except ValueError as e:
            print("Erro ao cadastrar cliente:", e)
            continue

        opc = input("\nDeseja cadastrar outro cliente? (s/n): ")
        if opc.lower() != 's':
            break
        
        
    

# ===== Menu interativo =====
def menu_interativo():
    while True:
        try:
            menu = int(input("""\n
---------------------------------                         
MENU DE OPÇÕES:

1 - Cadastrar livros
2 - Cadastrar revistas
3 - Cadastrar cliente
4 - Alugar livros
5 - Alugar revistas
6 - Devolver livros
7 - Devolver revistas
8 - Listar livros
9 - Listar revistas
10 - Listar todos os clientes
0 - Sair
---------------------------------
Digite sua opção: """))
        except ValueError:
            print("Digite apenas valores numéricos!")
            continue

        # ===== AÇÕES DO MENU =====
        if menu == 0:
            print("Saindo do sistema...")
            break
        elif menu == 1:
            cadastrar_livro()
        elif menu == 2:
            cadastrar_revista()
        elif menu == 3:
            cadastrar_cliente()
        elif menu == 4:
            pass  # alugar livros
        elif menu == 5:
            pass  # alugar revistas
        elif menu == 6:
            pass  # devolver livros
        elif menu == 7:
            pass  # devolver revistas
        elif menu == 8:
            pass
        elif menu == 9:
            pass
        elif menu == 10:
            pass
        else:
            print("Opção inválida! Tente novamente.")

# ===== Inicia o programa =====
menu_interativo()

