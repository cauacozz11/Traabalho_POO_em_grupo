class ItensBiblioteca:
    def __init__(self, categoria, titulo, autor, editora):
        self.__categoria = categoria
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        
    def mostrar_item(self):
        return f"Categoria: {self.__categoria} | Título: {self.__titulo} | Autor: {self.__autor} | Editora: {self.__editora}"    
    




class Livros(ItensBiblioteca):
     def __init__(self, categoria, titulo, autor, editora, preco):
        super().__init__(categoria, titulo, autor, editora)
        self.__preco = preco
        
        

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
        return super().mostrar_informacoes() + f"| CNPJ:{self.__cnpj}"
    

class Cliente(Pessoa):
    def __inti__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)
        
    def mostrar_informacoes_cliente(self):
        print('INFORMAÇÕES DO CLIENTE')
        print()
        return super().mostrar_informacoes()        
    
    
    
pessoa1 = Cliente('Cauã', 138468931948, 47999343288)

print(Cliente.mostrar_informacoes_cliente(pessoa1))    