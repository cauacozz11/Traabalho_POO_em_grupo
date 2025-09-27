from classes import Livro, Revista, Bibliotecario, Cliente

def menu_interativo():
    while True:
        try:
            menu = int(input("""
    ---------------------------------                         
    MENU DE OPÇÕES:

    1 - Cadastrar livros
    2 - Cadastrar Revistas
    3 - Cadastrar Cliente
    4 - Alugar livros
    5 - Alugar revistas
    6 - Devolver livros
    7 - Devolver revistas
    8 - Listar livros
    9 - Listar revistas
    10 - Sair do programa
    ---------------------------------
    Digite sua opção: """))
            if 1 <= menu <= 10:
                break
            else:
                print('Essa opção é inválida')
        except ValueError:
            print('Digite apenas valores válidos...')        
        
            
    if menu == 1:
        pass
    elif menu == 2:
        pass
    elif menu == 3:
        pass
    elif menu == 4:
        pass
    elif menu == 5:
        pass
    elif menu == 6:
        pass
    elif menu == 7:
        pass
    elif menu == 8:
        pass
    elif menu == 9:
        pass
    else:
        pass 
    
    
menu_interativo()    