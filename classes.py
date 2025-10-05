# ==============================
# CLASSES DO SISTEMA BIBLIOTECA
# ==============================

# Classe base para itens da biblioteca
class ItensBiblioteca:
    def __init__(self, categoria, titulo, editora):
        self.__categoria = categoria
        self.__titulo = titulo
        self.__editora = editora
        self.__disponivel = True  # Todo item começa disponível

    # --- Categoria ---
    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__categoria = valor  
        else:
            raise ValueError("Categoria deve ser uma string não vazia") 

    # --- Título ---
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__titulo = valor
        else:
            raise ValueError("Título deve ser uma string não vazia")

    # --- Editora ---
    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, valor):
        if isinstance(valor, str) and valor.strip():
            self.__editora = valor 
        else:
            raise ValueError("Editora deve ser uma string não vazia") 

    # --- Disponibilidade ---
    @property
    def disponivel(self):
        return self.__disponivel

    def status_emprestar(self):
        """Marca como emprestado (indisponível)"""
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def status_devolver(self):
        """Marca como disponível novamente"""
        self.__disponivel = True

    # --- Mostrar informações ---
    def mostrar_item(self):
        status = 'Disponível' if self.__disponivel else 'Indisponível'
        return f"Categoria: {self.__categoria} | Título: {self.__titulo} | Editora: {self.__editora} | Status: {status}"    


# ==========================
# Classe Livro
# ==========================
class Livro(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, autor):
        super().__init__(categoria, titulo, editora)
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


# ==========================
# Classe Revista
# ==========================
class Revista(ItensBiblioteca):
    def __init__(self, categoria, titulo, editora, edicao):
        super().__init__(categoria, titulo, editora)
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


# ==========================
# Classe Pessoa (base)
# ==========================
class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    # --- Nome ---
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if isinstance(valor, str) and valor.replace(" ", "").isalpha():
            self.__nome = valor
        else:
            raise ValueError("Nome deve conter apenas letras e espaços")

    # --- CPF ---
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 11:
            self.__cpf = valor
        else:
            raise ValueError("CPF deve conter exatamente 11 dígitos numéricos")

    # --- Telefone ---
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 11:
            self.__telefone = valor
        else:
            raise ValueError("Telefone deve conter apenas dígitos e ter 11 números")

    # --- Mostrar informações ---
    def mostrar_informacoes(self):
        return f"Nome: {self.__nome} | CPF: {self.__cpf} | Telefone: {self.__telefone}"   


# ==========================
# Classe Bibliotecário
# ==========================
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
            raise ValueError("CNPJ deve conter exatamente 14 dígitos numéricos") 

    def mostrar_informacoes(self):
        return f"INFORMAÇÕES BIBLIOTECÁRIO\n{super().mostrar_informacoes()} | CNPJ: {self.__cnpj}"


# ==========================
# Classe Cliente
# ==========================
class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, id_cliente):
        super().__init__(nome, cpf, telefone)
        self.id_cliente = id_cliente
        self.__itens_alugados = []

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
        info = f'INFORMAÇÕES CLIENTE\n{super().mostrar_informacoes()} | Cadastro: {self.__id_cliente}'
        if self.__itens_alugados:
            info += '\n Itens Alugados:'
            for item in self.__itens_alugados:
                info += f'\n - {item.titulo}'
        else:
            info += '\n Nenhum item alugado no momento.'
        return info
    
    def alugar_item(self, item):
        self.__itens_alugados.append(item)

    def devolver_item(self, item):
        if item in self.__itens_alugados:
            self.__itens_alugados.remove(item)
