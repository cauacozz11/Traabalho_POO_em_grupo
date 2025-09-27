
from classes import Cliente

clientes = []

#Função cliente
def cadastrar_cliente():
    print("\n--- Cadastro de Cliente ---")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    id_cliente = input("ID do cliente: ")
    
    try:
        
        novo_cliente = clientes(nome,cpf, telefone, id_cliente)
        clientes.append(novo_cliente)
        print("\nCliente cadastrado com sucesso!")
        print(novo_cliente.mostrar_informacoes_cliente())
    except ValueError as resp:
       print("Erro ao cadastrar cliente:", resp)
       

while True:
  opc = input("\nDeseja cadastrar um cliente? (s/n): ")
  if opc.lower() == 's':
    cadastrar_cliente()
  else:
    break        