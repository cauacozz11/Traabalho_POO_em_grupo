from models.pessoa import Pessoa
from models.item import Livro, Revista
from dao.pessoa_dao import pessoaDAO
from dao.livro_dao import livroDAO
from dao.revista_dao import revistaDAO
from dao.emprestimo_dao import emprestimoDAO


if __name__ == "__main__":
    dao_pessoa = pessoaDAO()
    dao_livro = livroDAO()
    dao_revista = revistaDAO()
    dao_emprestimo = emprestimoDAO()
    
    
    print('----1. CADASTRANDO DADOS----')
    
    p1 = Pessoa("Carlos Drummond", "11122233344", "219999988j88")
    dao_pessoa.salvar(p1)
    
    
    l1 = Livro("Poesia", "Alguma Poesia", "Editora X", "Drummond")
    dao_livro.salvar(l1)

    
    r1 = Revista("Ciência", "Super Interessante", "Abril", 405)
    dao_revista.salvar(r1)
    
    
    print('----2. Buscando por ID----')
    pessoa_db = dao_pessoa.buscar_por_cpf(p1.cpf)
    livro_db = dao_livro.buscar_por_titulo(l1.titulo)
    revista_db = dao_revista.buscar_por_edicao(r1.edicao)
    
    if pessoa_db and livro_db:
        id_pessoa = pessoa_db[0]
        id_livro = livro_db[0]
        
        print(f"Pessoa ID: {id_pessoa} vai pegar o Livro: {id_livro}")
        
        sucesso = dao_emprestimo.salvar_emprestimo(id_pessoa, id_livro=id_livro)
        
        if sucesso:
            print("Tentando alugar o mesmo livro de novo (Teste de Bloqueio)...")
            dao_emprestimo.salvar_emprestimo(id_pessoa, id_livro=id_livro)
    
    else:
        print("Erro: Não foi possível recuperar os IDs para o teste.")