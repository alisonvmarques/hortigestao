print("Caderneta de Fiado - HortiGestão")

clientes = []
nome_cliente = input("Digite o nome do cliente (ou pressione Enter para sair): ")
while nome_cliente != "":
    telefone_cliente = input("Digite o telefone do cliente (ou pressione Enter para sair): ")
    clientes.append({"nome_cliente":nome_cliente, "telefone_cliente": telefone_cliente})
    nome_cliente = input("Digite o nome do cliente (ou pressione Enter para sair): ")
print(f"Clientes cadastrados: {clientes}")
