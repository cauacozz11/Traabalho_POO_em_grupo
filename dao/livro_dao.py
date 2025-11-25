from database.conexao import BancoDeDados
from models.item import Livro

class livroDAO:
    def __init__(self):
        self.banco = BancoDeDados()
        
        
    def buscar_por_titulo(self, titulo):
        self.banco.conectar()
        
        sql = "SELECT * FROM livros WHERE titulo = ?"
        
        try:
            self.banco.cursor.execute(sql,(titulo,))
            resultado = self.banco.cursor.fetchone()
            return resultado
        except:
            print(f'Erro ao buscar o Livro:  {titulo}')   
        
        
    def salvar(self, livro):
        
        livro_existe = self.buscar_por_titulo(livro.titulo)
        
        if livro_existe:
            print(f'Erro: O livro já foi cadastrado em nosso sistema!')
            return False
        
        
        self.banco.conectar()
        
        sql = "INSERT INTO livros (titulo, editora, categoria, autor, is_disponivel) VALUES (?, ?, ?, ?, ?)"      
        
        valores = (livro.titulo, livro.editora, livro.categoria, livro.autor, livro.disponivel)
        
        try:
            self.banco.cursor.execute(sql, valores)
            
            self.banco.conexao.commit()
            
            print(f'Livro {livro.titulo} cadastrado com sucesso!')
            return True
        except Exception as erro:
            print(f"Erro ao salvar livro {erro}")
            
        finally:
            self.banco.desconectar()
            
           
    def listar_todos(self):
        self.banco.conectar()
        
        try:
            self.banco.cursor.execute("SELECT * FROM livros") 
            lista = self.banco.cursor.fetchall()
            return lista
        except Exception as erro:
            print(erro)
            return []
        finally:
            self.banco.desconectar()             
        
        
        