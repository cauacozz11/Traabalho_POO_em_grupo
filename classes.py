class ItensBiblioteca:
    def __init__(self, categoria, titulo, editora, preco):
        self.categoria = categoria
        self.titulo = titulo
        self.editora = editora
        self.preco = preco
        
    @property
    def categoria(self):
        return self.__categoria
        
    @categoria.setter
    def categoria(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__categoria = valor  
        else:
            print("Categoria deve ser uma string não vazia") 
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__titulo = valor
        else:
            print("Título deve ser uma string não vazia")
        
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__editora = valor 
        else:
            print("Editora deve ser uma string não vazia") 
            
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__preco = valor
        else:
            print("Preço deve ser um número positivo (int ou float)")    
    
    def mostrar_item(self):
        return f"Categoria: {self.__categoria} | Título: {self.__titulo} | Editora: {self.__editora} | Preço: {self.__preco}"    


class Livro(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, autor):
        super().__init__(categoria, titulo, editora, preco)
        self.autor = autor
        
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__autor = valor
        else:
            print("Autor deve ser uma string não vazia")     
        
    def mostrar_informacoes(self):
        return f"INFORMAÇÕES LIVRO\n{super().mostrar_item()} | Autor: {self.__autor}"
    

class Revista(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, edicao):
        super().__init__(categoria, titulo, editora, preco)
        self.edicao = edicao
        
    @property
    def edicao(self):
        return self.__edicao
    
    @edicao.setter
    def edicao(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__edicao = valor
        else:
            print("Edição deve ser um número inteiro positivo")    
    
    def mostrar_informacoes(self):
        return f"INFORMAÇÕES REVISTA\n{super().mostrar_item()} | Edição: {self.__edicao}"        
            
      
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    # --- NOME ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__nome = valor
        else:
            print("Nome deve ser uma string não vazia")

    # --- CPF ---
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 11:
            self.__cpf = valor
        else:
            print("CPF deve conter exatamente 11 dígitos numéricos")    
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) >= 8:
            self.__telefone = valor 
        else:
            print("Telefone deve conter apenas dígitos e ter pelo menos 8 números")       
    
    def mostrar_informacoes(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone}"      


class Bibliotecario(Pessoa):
    def __init__(self, nome, cpf, telefone, cnpj):
        super().__init__(nome, cpf, telefone)
        self.cnpj = cnpj
        
    @property
    def cnpj(self):
        return self.__cnpj  
    
    @cnpj.setter
    def cnpj(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 14:
            self.__cnpj = valor
        else:
            print("CNPJ deve conter exatamente 14 dígitos numéricos") 
        
    def mostrar_informacoes(self):
        return f"INFORMAÇÕES BIBLIOTECÁRIO\n{super().mostrar_informacoes()} | CNPJ: {self.__cnpj}"
    

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, id_cliente):
        super().__init__(nome, cpf, telefone)
        self.id_cliente = id_cliente
    
    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @id_cliente.setter
    def id_cliente(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__id_cliente = valor
        else:
            print("ID do cliente deve ser um número inteiro positivo")
        
    def mostrar_informacoes(self):
        return f"INFORMAÇÕES CLIENTE\n{super().mostrar_informacoes()} | Cadastro: {self.__id_cliente}"
