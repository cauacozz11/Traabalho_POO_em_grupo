from database.conexao import BancoDeDados
from models.item import Revista

class revistaDAO:
    def __init__(self):
        self.banco = BancoDeDados()
        
        
    def buscar_por_edicao(self, edicao):
        self.banco.conectar()    
        
        
        sql ="SELECT * FROM revistas WHERE edicao = ?"
        
        
        try:
            self.banco.cursor.execute(sql ,(edicao,))
            resultado = self.banco.cursor.fetchone()
            return resultado
        except Exception as erro:
            print(f'Erro ao buscar a Revista de edição: {edicao}')
        
    def salvar(self, revista):
        
        edicao_existe = self.buscar_por_edicao(revista.edicao)
        
        
        if edicao_existe:
            print(f'Erro: A Revista de edição {revista.edicao} já foi cadastrada em nosso sistema!')
            return False
        
        self.banco.conectar()
        
        sql = "INSERT INTO revistas (titulo, editora, categoria, edicao, is_disponivel) VALUES (?, ?, ?, ?, ?)"
        
        valores = (revista.titulo, revista.editora, revista.categoria, revista.edicao, revista.disponivel)
        
        try:
            self.banco.cursor.execute(sql, valores)
            
            self.banco.conexao.commit()
            print(f'Revista {revista.titulo} cadastrada com sucesso!')
            return True
        except Exception as erro:
            print(f"Erro ao salvar revista: {erro}")
            
        finally:
            self.banco.desconectar()