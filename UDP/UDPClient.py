import socket

# Definição de IP e porta
HOST = '127.0.0.1'
PORT = 5001

# Criação do socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Realiza o envio de mensagens UDP
for i in range(5):
    msg = f"Mensagem UDP {i+1}"
    client.sendto(msg.encode(), (HOST, PORT))
    data, _ = client.recvfrom(1024)
    print(f"Servidor respondeu: {data.decode()}")

client.close()