import sqlite3


class BancoDeDados:
    # Função construtora que serve como molde para a inicialização do Banco de Dados.
    def __init__(self, nome_banco="meu_banco.db"):
        self.nome_banco = nome_banco
        self.conexao = None
        self.cursor = None
        
    
    def conectar(self):
        # Faz a conexão com o Banco se existir, e caso não exista cria um banco no Back-End da operação
        try:
            self.conexao = sqlite3.connect(self.nome_banco)
            self.cursor = self.conexao.cursor()
            print('Banco conectado com sucesso...')
        except sqlite3.Error as erro:
            print(f'Ocorreu um erro na conexão {erro}')
         
    def desconectar(self):
        # Faz a desconexão com o Banco 
        try:
            if self.conexao:
                self.conexao.close()
                print('Banco desconectado com sucesso')
            else:
                print('O Banco já está desconectado')
        except sqlite3.Error as erro:
            print(f'Ocorreu um erro na conexão {erro}')            
                     
    def criar_tabelas(self):
            self.conectar()

            # Tabela genérica de Pessoas (Serve para Clientes e Bibliotecários)
            sql_pessoas = """
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR(14) UNIQUE,
                telefone VARCHAR(15)
            );
            """

            # Tabela de Livros (Com coluna 'autor')
            # Nota: is_disponivel usamos INTEGER (0 = Falso, 1 = Verdadeiro)
            sql_livros = """
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                editora TEXT,
                categoria TEXT,
                autor TEXT,
                is_disponivel BOOLEAN DEFAULT 1
            );
            """

            # Tabela de Revistas (Com coluna 'edicao')
            sql_revistas = """
            CREATE TABLE IF NOT EXISTS revistas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                editora TEXT,
                categoria TEXT,
                edicao INTEGER,
                is_disponivel BOOLEAN DEFAULT 1
            );
            """

            try:
                # Executamos as 3 ordens de criação
                self.cursor.execute(sql_pessoas)
                self.cursor.execute(sql_livros)
                self.cursor.execute(sql_revistas)
                
                self.conexao.commit()
                print("Tabelas (Pessoas, Livros, Revistas) verificadas/criadas com sucesso!")
                
            except sqlite3.Error as erro:
                print(f"Erro ao criar tabelas: {erro}")
            finally:
                self.desconectar()


# Faz o arquivo rodar de fato
if __name__ == "__main__":
    banco = BancoDeDados()
    
    banco.criar_tabelas()