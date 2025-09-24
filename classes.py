class ItensBiblioteca:
    def __init__(self, categoria, titulo, editora, preco):
        self.__categoria = categoria
        self.__titulo = titulo
        self.__editora = editora
        self.__preco = preco
        
    def mostrar_item(self):
        return f"Categoria: {self.__categoria} | Título: {self.__titulo} | Editora: {self.__editora} | Preço: {self.__preco}"    
    

class Livro(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, autor ):
        super().__init__(categoria, titulo, editora, preco)
        self.__autor = autor
        
    def mostrar_livro(self):
        return f"{super().mostrar_item()} | Autor: {self.__autor}"
    


class Revista(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, edicao):
        super().__init__(categoria, titulo, editora, preco)
        self.__edicao = edicao
        
    def mostrar_revista(self):
        return f"{super().mostrar_item()} | Edição: {self.__edicao}"        
        

        
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone  
        
    
    def mostrar_informacoes(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone}"      
    
    
    
class Bibliotecario(Pessoa):
    def __init__(self, nome, cpf, telefone, cnpj):
        super().__init__(nome, cpf, telefone)
        self.__cnpj = cnpj
        
    def mostrar_informacoes_bibliotecario(self):
        print('INFORMÇÕES DO BIBLIOTECÁRIO')
        print()
        return f"{super().mostrar_informacoes()} | CNPJ:{self.__cnpj}"
    

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, id_cliente):
        super().__init__(nome, cpf, telefone)
        self.__id_cliente = id_cliente
        
    def mostrar_informacoes_cliente(self):
        print('INFORMAÇÕES DO CLIENTE')
        print()
        return f"{super().mostrar_informacoes()} | Cadastro: {self.__id_cliente}"        
    
    
    
pessoa1 = Cliente('Cauã', 138468931948, 47999343288, 675)

print(pessoa1.mostrar_informacoes_cliente())    