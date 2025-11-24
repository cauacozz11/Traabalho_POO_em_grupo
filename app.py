from models.item import Revista
from dao.revista_dao import revistaDAO

if __name__ == "__main__":
    livro2 = Revista("Wired", "Tecnologia", "Navus", 155)
    dao = revistaDAO()
    
    dao.salvar(livro2)
