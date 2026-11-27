print("Caderneta de Fiado - HortiGestão")

clientes = []
cliente = input("Digite o nome do cliente (ou pressione Enter para sair): ")
while cliente != "":
    clientes.append(cliente)
    cliente = input("Digite o nome do cliente (ou pressione Enter para sair): ")
print(f"Clientes cadastrados: {clientes}")
