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
            raise ValueError("Categoria deve ser uma string não vazia") 
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__titulo = valor
        else:
            raise ValueError("Título deve ser uma string não vazia")
        
    @property
    def editora(self):
        return self.__editora
    
    @editora.setter
    def editora(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__editora = valor 
        else:
            raise ValueError("Editora deve ser uma string não vazia") 
            
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__preco = valor
        else:
            raise ValueError("Preço deve ser um número positivo (int ou float)")    
    
    def mostrar_item(self):
        return f"Categoria: {self.__categoria} | Título: {self.__titulo} | Editora: {self.__editora} | Preço: {self.__preco}"    


class Livro(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, preco, autor):
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
            raise ValueError("Autor deve ser uma string não vazia")     
        
    def mostrar_informacoes(self):
        return f"INFORMAÇÕES LIVRO\n{super().mostrar_item()} | Autor: {self.__autor}"
    

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
            raise ValueError("Edição deve ser um número inteiro positivo")    
    
    def mostrar_informacoes(self):
        return f"INFORMAÇÕES REVISTA\n{super().mostrar_item()} | Edição: {self.__edicao}"        
            
      
# Classe base Pessoa
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome        # Define o nome
        self.cpf = cpf          # Define o CPF
        self.telefone = telefone  # Define o telefone

    # --- NOME ---
    @property
    def nome(self):
        return self.__nome      # Retorna o nome

    @nome.setter
    def nome(self, valor):
        # Valida se o nome contém apenas letras e espaços
        if isinstance(valor, str) and valor.replace(" ", "").isalpha():
            self.__nome = valor
        else:
            raise ValueError("Nome deve conter apenas letras e espaços")

    # --- CPF ---
    @property
    def cpf(self):
        return self.__cpf       # Retorna o CPF

    @cpf.setter
    def cpf(self, valor):
        # Valida se o CPF tem exatamente 11 dígitos numéricos
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 11:
            self.__cpf = valor
        else:
            raise ValueError("CPF deve conter exatamente 11 dígitos numéricos")

    # --- TELEFONE ---
    @property
    def telefone(self):
        return self.__telefone  # Retorna o telefone

    @telefone.setter
    def telefone(self, valor):
        # Valida se o telefone tem 11 dígitos numéricos
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 11:
            self.__telefone = valor
        else:
            raise ValueError("Telefone deve conter apenas dígitos e ter pelo menos 11 números")

    # --- Mostrar informações ---
    def mostrar_informacoes(self):
        # Retorna string formatada com todas as informações da pessoa
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone}"   


class Bibliotecario(Pessoa):
    def __init__(self, nome, cpf, telefone, cnpj):
        super().__init__(nome, cpf, telefone)
        self.__cnpj = cnpj
        
    @property
    def cnpj(self):
        return self.__cnpj  
    
    @cnpj.setter
    def cnpj(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 14:
            self.__cnpj = valor
        else:
            raise ValueError("CNPJ deve conter exatamente 14 dígitos numéricos") 
        
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
            raise ValueError("ID do cliente deve ser um número inteiro positivo")
        
    def mostrar_informacoes_cliente(self):
        return f"INFORMAÇÕES CLIENTE\n{super().mostrar_informacoes()} | Cadastro: {self.__id_cliente}"
