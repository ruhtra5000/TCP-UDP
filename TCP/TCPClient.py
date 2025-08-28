import socket

HOST = '127.0.0.1'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

for i in range(5):
    msg = f"Mensagem TCP {i+1}"
    client.sendall(msg.encode())
    resposta = client.recv(1024).decode()
    print(f"Servidor respondeu: {resposta}")

client.close()