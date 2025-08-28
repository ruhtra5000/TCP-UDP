import socket

HOST = '127.0.0.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Servidor TCP aguardando conexões...")
conn, addr = server.accept()
print(f"Conectado por {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Recebido: {data}")
    conn.sendall("Mensagem recebida".encode())

conn.close()