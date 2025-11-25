from database.conexao import BancoDeDados
from datetime import datetime, timedelta


class emprestimoDAO:
    def __init__(self):
        self.banco = BancoDeDados()


    def buscar_por_emprestimo(self, is_disponivel):
        self.banco.conectar()


    def salvar_emprestimo(self, id_pessoa, id_livro=None, id_revista=None):
        self.banco.conectar()

        item_disponivel = False

        if id_livro:
            self.banco.cursor.execute("SELECT is_disponivel FROM livros WHERE id = ?", (id_livro,))
            resultado = self.banco.cursor.fetchone()
            if resultado and resultado[0] == 1:
                item_disponivel = True

        elif id_revista:
            self.banco.cursor.execute("SELECT is_disponivel FROM revistas WHERE id = ?", (id_revista,))
            resultado = self.banco.cursor.fetchone()
            if resultado and resultado[0] == 1:
                item_disponivel = True
                

        if not item_disponivel:
            print('Erro: Esse item já está alugado ou não existe!')
            self.banco.desconectar()
            return False

        data_hoje = datetime.now().strftime("%Y-%m-%d")

        sql = """
        INSERT INTO emprestimos
        (id_pessoa, id_livro, id_revista, data_emprestimo, data_devolucao)
        VALUES (?,?,?,?,?)
        """  

        valores = (id_pessoa, id_livro, id_revista, data_hoje, None)

        try:
            self.banco.cursor.execute(sql, valores)

            if id_livro:
                sql_UPDATE = "UPDATE livros SET is_disponivel = 0 WHERE id = ?"
                self.banco.cursor.execute(sql_UPDATE, (id_livro,))
            elif id_revista:
                sql_UPDATE = "UPDATE revistas SET is_disponivel = 0 WHERE id = ?"
                self.banco.cursor.execute(sql_UPDATE, (id_revista,))

            self.banco.conexao.commit()
            print(f"Empréstimo registrado em {data_hoje}")
        except Exception as erro:
            print(f"Erro ao registrar o empréstimo: {erro}")        

        finally:
            self.banco.desconectar()
            
            
            
    def finalizar_emprestimo(self, id_emprestimo):
        self.banco.conectar()
            
        try:
            sql_busca = "SELECT id_livro, id_revista FROM emprestimos WHERE id = ?"
            self.banco.cursor.execute(sql_busca, (id_emprestimo,))
            resultado = self.banco.cursor.fetchone()
                
            id_livro = resultado[0]
            id_revista = resultado[1]
                
            if id_livro:
                sql_liberar = "UPDATE livros SET is_disponivel = 1 WHERE id = ?"
                self.banco.cursor.execute(sql_liberar, (id_livro,))
                    
            elif id_revista:
                sql_liberar = "UPDATE revistas SET is_disponivel = 1 WHERE id = ?"
                self.banco.cursor.execute(sql_liberar, (id_revista,))
            
            self.banco.conexao.commit()
            print(f"Empréstimo {id_emprestimo} finalizado! Item devolvido à estante.")
            return True
            
        except Exception as erro:
            self.banco.conexao.rollback()
            print(f"Erro ao devolver: {erro}")
            return False
                
        finally:
            self.banco.desconectar()