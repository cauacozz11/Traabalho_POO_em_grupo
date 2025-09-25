class ItensBiblioteca:
    def __init__(self, categoria, titulo, editora, preco):
        self.__categoria = categoria
        self.__titulo = titulo
        self.__editora = editora
        self.__preco = preco
        
        
    @property
    def categoria(self):
        return self.__categoria
        
    @categoria.setter
    def categoria(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__categoria = valor  
        else:
            print('Categoria deve ser uma string não vazia') 
        
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__titulo = valor
        else:
            print('Titulo deve ser uma string não vazia')
        
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def titulo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__titulo = valor
        else:
            print('Título deve ser uma string não vazia')
        
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__editora = valor 
        else:
            print('Editora não pode ser uma string não vazia') 
            
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, int, float) and valor > 0:
            self.__preco = valor
        else:
            print('Preço deve ser um inteiro não negativo')    
    
    
                                                   
        
    def mostrar_item(self):
        return f"Categoria: {self.__categoria} | Título: {self.__titulo} | Editora: {self.__editora} | Preço: {self.__preco}"    
    

class Livro(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, autor ):
        super().__init__(categoria, titulo, editora, preco)
        self.__autor = autor
        
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__autor = valor
        else:
            print('Autor deve ser uma string não vazia')     
        
    def mostrar_livro(self):
        return f"{super().mostrar_item()} | Autor: {self.__autor}"
    
    
class Revista(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, edicao):
        super().__init__(categoria, titulo, editora, preco)
        self.__edicao = edicao
        
    @property
    def edicao(self):
        return self.__edicao
    
    @edicao.setter
    def edicao(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__edicao = valor
        else:
            print('Edição deve ser um inteiro não negativo')    
    
    @edicao.setter
    def edicao(self):
        return self.__edicao   
        
    def mostrar_revista(self):
        return f"{super().mostrar_item()} | Edição: {self.__edicao}"        
            
            
#Classe Pessoa-----------------------------------            
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    # --- NOME -----------------------------------
    @property
    def nome(self):
        return self.__nome
    
    #Valida para não passar valores vazio 
    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__nome = valor
        else:
            print("Nome deve ser uma string não vazia")

    # --- CPF -----------------------------
    @property
    def cpf(self):
        return self.__cpfs

    @cpf.setter
    def cpf(self, valor):
        if isinstance(valor, int) or (isinstance(valor, str) and valor.isdigit()):
            self.__cpf = valor
        else:
            print("CPF deve conter apenas números")

    # --- TELEFONE ---
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        if isinstance(valor, int) or (isinstance(valor, str) and valor.isdigit()):
            self.__telefone = valor
        else:
            print("Telefone deve conter apenas números")

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