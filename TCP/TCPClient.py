import socket

# Definição de IP e porta
HOST = '127.0.0.1'
PORT = 5000

# Criação do socket do cliente 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Envio de mensagens TCP
for i in range(5):
    msg = f"Mensagem TCP {i+1}"
    client.sendall(msg.encode())
    resposta = client.recv(1024).decode()
    print(f"Servidor respondeu: {resposta}")

client.close()