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
