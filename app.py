from models.item import Livro
from dao.livro_dao import livroDAO

if __name__ == "__main__":
    livro2 = Livro("Ficção Científica", "Duna", "Editora Aleph", "Frank Herbert")
    dao = livroDAO()
    
    dao.salvar(livro2)
