from database.conexao import BancoDeDados
from models.pessoa import Pessoa


class PessoaDAO:
    def __init__(self) :
        self.banco = BancoDeDados()
 
 
           
    def buscar_por_cpf(self, cpf):
        self.banco.conectar()
        
        sql = "SELECT * FROM pessoas WHERE cpf = ?"
        
        
        try:
            self.banco.cursor.execute(sql,(cpf,))
            resultado = self.banco.cursor.fetchone()
            return resultado
        except:
            print(f'Erro ao buscar o CPF: {cpf}')        
    
    
    
        
    def salvar(self, pessoa):
        
        pessoa_existe = self.buscar_por_cpf(pessoa.cpf)
        
        
        if pessoa_existe:
            print(f'Erro: O CPF {pessoa.cpf} já foi cadastrado em nosso sistema!')
            return False
        
        # Abrir a conexão
        self.banco.conectar()
        
        # O Comando SQL (Seguro com ?)
        sql = "INSERT INTO pessoas (nome, cpf, telefone) VALUES (?, ?, ?)"
        
        # Os Dados (Extrair do objeto pessoa)
        valores = (pessoa.nome, pessoa.cpf, pessoa.telefone)
        
        try:
            # Executar o comando
            self.banco.cursor.execute(sql, valores)
            
            # Salvar de verdade (Carimbar)
            self.banco.conexao.commit()
            
            print(f"Pessoa {pessoa.nome} cadastrada com sucesso!")
            return True
            
        except Exception as erro:
            print(f"Erro ao salvar pessoa: {erro}")
            return False
            
        finally:
            # Fechar a porta
            self.banco.desconectar()
            
        
