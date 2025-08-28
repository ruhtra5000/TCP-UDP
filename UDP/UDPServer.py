import socket

# Definião de IP e porta
HOST = '127.0.0.1'
PORT = 5001

# Abertura do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

# Recebimento de mensagens UDP
print("Servidor UDP aguardando mensagens...")
while True:
    data, addr = server.recvfrom(1024)
    print(f"Recebido de {addr}: {data.decode()}")
    server.sendto("Mensagem recebida".encode(), addr)
