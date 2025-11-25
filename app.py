from dao.emprestimo_dao import emprestimoDAO

if __name__ == "__main__":
    dao = emprestimoDAO()

    # ATENÇÃO: Tu precisas saber o ID do empréstimo que fizeste.
    # Provavelmente é o 1, se for o primeiro teste.
    id_do_emprestimo = 1 
    
    print(f"Tentando devolver o Empréstimo ID {id_do_emprestimo}...")
    
    sucesso = dao.finalizar_emprestimo(id_do_emprestimo)
    
    if sucesso:
        print("✅ Tudo certo! O livro deve estar disponível de novo.")
    else:
        print("❌ Algo deu errado.")