
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
        autor = input("Autor: ")
        
        try:
            novo_livro = Livro(categoria, titulo, editora, autor)
            livros.append(novo_livro)
            print("\nLivro cadastrado com sucesso!")
            print(novo_livro.mostrar_informacoes())

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
            edicao = int(input("Edição (número inteiro positivo): "))
        except ValueError:
            print("Edição deve ser um número inteiro.")
            continue  # volta para o início do while

        try:
            nova_revista = Revista(categoria, titulo, editora, edicao)
            revistas.append(nova_revista)
            print("\nRevista cadastrada com sucesso!")
            print(nova_revista.mostrar_informacoes())
        
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
        
def listar_clientes():
    print("\n--- Lista de Clientes ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for i, c in enumerate(clientes, start=1):
            print(f"{i}. {c.mostrar_informacoes_cliente()}") 
    input("\nPressione ENTER para voltar ao menu...")             

def listar_livros():
    print("\n--- Lista de Livros ---")
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for i, l in enumerate(livros, start=1):
            print(f"{i}. {l.mostrar_informacoes()}")
    input("\nPressione ENTER para voltar ao menu...") 
    
def listar_revistas():
    print("\n--- Lista de Revistas ---")
    if not revistas:
        print("Nenhuma revista cadastrada.")
    else:
        for i, r in enumerate(revistas, start=1):
            print(f"{i}. {r.mostrar_informacoes()}")       
    input("\nPressione ENTER para voltar ao menu...") 

def alugar_livro():
    print('\n--- Aluguel de Livro ---')

    if not clientes:
        print('\nERRO: Nenhum cliente cadastrado no sistema. ')
        print('Por favor, cadastre um cliente para realizar um aluguel.')
        input('Pressione ENTER para voltar ao menu.')
        return
            
    nome_cliente = input('Digite o nome completo do cliente: ').strip()
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.nome.lower() == nome_cliente.lower():
            cliente_encontrado = cliente
            break
    if not cliente_encontrado:
        print(f'\nERRO: Cliente com o nome "{nome_cliente}" não foi encontrado.')
        input('Pressione ENTER para voltar ao menu...')
        return
        
    livro_encontrado = None
    while True:
        titulo_livro = input(f'Digite o título do livro que {cliente_encontrado.nome} deseja alugar: ')
        for livro in livros:
            if livro.titulo.lower() == titulo_livro.lower():
                livro_encontrado = livro
                break
        if livro_encontrado:
            break
        else:
            print(f'\nERRO: Livro com o título {titulo_livro} não foi encontrado.')

            tentar_novamente = input('Deseja tentar de novo? [S/N]: ')
            if tentar_novamente.lower()[0] != 's':
                print('Busca cancelada. Voltando ao menu.')
                return
    if livro_encontrado.status_emprestar():
        cliente_encontrado.alugar_item(livro_encontrado)

        print('\n========================================')
        print(" Aluguel realizado com sucesso!")
        print(f'  Cliente: {cliente_encontrado.nome}')
        print(f'  Livro: {livro_encontrado.titulo}')
        print('========================================')
    else:
        print(f'\nERRO: O livro {livro_encontrado.titulo} já está alugado.')

    input('Pressione ENTER para retornar ao menu...')

def devolver_livro():
    print('\n     Devolução de Livro')

    if not clientes:
        print('\nERRO: Nenhum cliente cadastrado no sistema.')
        input('Pressione ENTER para voltar ao menu...')
        return
    
    nome_cliente = input('Digite o nome completo do cliente que está devolvendo o livro: ').strip()
    cliente_encontrado = None
    for cliente in clientes:
        if cliente.nome.lower() == nome_cliente.lower():
            cliente_encontrado = cliente
            break
    if not cliente_encontrado:
        print(f'\nERRO: Cliente com o nome {nome_cliente} não foi encontrado.')
        input('Pressione ENTER para voltar ao menu...')
        return

    if not cliente_encontrado._Cliente__itens_alugados:
        print(f'\nAVISO: {cliente_encontrado.nome} não possui nenhum item alugado no momento.')
        input('Pressione ENTER para voltar ao menu...')  
        return

    print(f'\nItens atualmente alugados por {cliente_encontrado.nome}: ')
    livros_do_cliente = []
    for item in cliente_encontrado._Cliente__itens_alugados:
        if isinstance(item, Livro):
            print(f'   Título: {item.titulo}')  
            livros_do_cliente.append(item)
    if not livros_do_cliente:
        print(f'\nAVISO: {cliente_encontrado.nome} não possui nenhum livro alugado no momento. ')
        input('Pressione ENTER para voltar ao menu...')
        return

    livro_para_devolver = None
    while True:
        titulo_devolucao = input('\nDigite o título do livro a ser devolvido ["n" para cancelar]: ').strip()
        if titulo_devolucao.lower()[0] == 'n':
            print('Operação cancelada.') 
            return
        for livro in livros_do_cliente:
            if livro.titulo.lower() == titulo_devolucao.lower():
                livro_para_devolver = livro
                break
        if livro_para_devolver:
            break
        else:
            print(f'\nERRO: Título não encontrado na lista de aluguéis de {cliente_encontrado.nome}. Tente novamente.')

    cliente_encontrado.devolver_item(livro_para_devolver)
    livro_para_devolver.status_devolver()
    print('\n========================================')
    print("  Devolução realizada com sucesso!")
    print(f'  Cliente: {cliente_encontrado.nome}')
    print(f'  Livro: {livro_para_devolver.titulo}')
    print('========================================')
    input('\nPressione ENTER para retornar ao menu...')
    
    
    
def alugar_revista():
    print("\n--- Aluguel de Revista ---")

    # 1️⃣ Verifica se há clientes cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente antes de alugar uma revista.")
        input("\nPressione ENTER para voltar ao menu.")
        return

    # 2️⃣ Solicita nome do cliente
    nome_cliente = input("Digite o nome do cliente: ").strip()
    cliente_encontrado = None

    for c in clientes:
        if c.nome.lower() == nome_cliente.lower():
            cliente_encontrado = c
            break

    if not cliente_encontrado:
        print("Cliente não encontrado. Verifique o nome ou cadastre o cliente.")
        input("\nPressione ENTER para voltar ao menu.")
        return

    # 3️⃣ Solicita título da revista
    while True:
        titulo_revista = input("Digite o título da revista que deseja alugar: ").strip()
        revista_encontrada = None

        for r in revistas:
            if r.titulo.lower() == titulo_revista.lower():
                revista_encontrada = r
                break

        if not revista_encontrada:
            opc = input("Revista não encontrada. Deseja tentar novamente? (s/n): ")
            if opc.lower() != 's':
                print("Voltando ao menu...")
                return
            continue  # volta e pergunta novamente

        # 4️⃣ Verifica disponibilidade
        if not revista_encontrada.disponivel:
            print("Desculpe, essa revista já está alugada.")
            input("\nPressione ENTER para voltar ao menu.")
            return

        # 5️⃣ Realiza o aluguel
        revista_encontrada.status_emprestar()

        print("\n✅ Aluguel realizado com sucesso!")
        print(f"Cliente: {cliente_encontrado.nome}")
        print(f"Revista: {revista_encontrada.titulo}")

        input("\nPressione ENTER para voltar ao menu.")
        break


def devolver_revista():
    print("\n--- Devolução de Revista ---")

    # 1️⃣ Verifica se há clientes cadastrados
    if not clientes:
        print("Nenhum cliente cadastrado. Cadastre um cliente antes de devolver uma revista.")
        input("\nPressione ENTER para voltar ao menu.")
        return

    # 2️⃣ Solicita o nome do cliente
    nome_cliente = input("Digite o nome do cliente: ").strip()
    cliente_encontrado = None

    for c in clientes:
        if c.nome.lower() == nome_cliente.lower():
            cliente_encontrado = c
            break

    if not cliente_encontrado:
        print("Cliente não encontrado. Verifique o nome ou cadastre o cliente.")
        input("\nPressione ENTER para voltar ao menu.")
        return

    # 3️⃣ Busca uma revista que esteja alugada
    revista_alugada = None
    for r in revistas:
        if not r.disponivel:  # revista alugada
            revista_alugada = r
            break

    if not revista_alugada:
        print("Nenhuma revista está alugada no momento.")
        input("\nPressione ENTER para voltar ao menu.")
        return

    # 4️⃣ Mostra informações
    print("\nInformações do Cliente:")
    print(cliente_encontrado.mostrar_informacoes_cliente())

    print("\nRevista Alugada:")
    print(revista_alugada.mostrar_informacoes())

    # 5️⃣ Confirma devolução
    confirmar = input("\nDeseja devolver esta revista? (s/n): ").strip().lower()
    if confirmar == 's':
        revista_alugada.status_devolver()
        print("\n✅ Revista devolvida com sucesso!")
    else:
        print("\nOperação cancelada. Revista continua alugada.")

    input("\nPressione ENTER para voltar ao menu.")
    
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
            alugar_livro() 
        elif menu == 5:
            alugar_revista()
        elif menu == 6:
            devolver_livro()  
        elif menu == 7:
            devolver_revista()
        elif menu == 8:
            listar_livros()
        elif menu == 9:
            listar_revistas()
        elif menu == 10:
            listar_clientes()
        else:
            print("Opção inválida! Tente novamente.")

# ===== Inicia o programa =====
menu_interativo()

