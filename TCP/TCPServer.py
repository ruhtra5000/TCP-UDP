import socket

# Definição de IP e porta
HOST = '127.0.0.1'
PORT = 5000

# Abertura do socket do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Handshake TCP
print("Servidor TCP aguardando conexões...")
conn, addr = server.accept()
print(f"Conectado por {addr}")

# Recebimento de mensagens TCP
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Recebido: {data}")
    conn.sendall("Mensagem recebida".encode())

conn.close()