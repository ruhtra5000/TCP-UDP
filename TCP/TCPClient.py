import socket
import time

# Definição de IP e porta
HOST = '127.0.0.1'
PORT = 5000

# Criação do socket do cliente 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Envio de mensagens TCP
for seq in range(5):
    timeSend = time.time_ns()
    payload = f"Mensagem TCP {seq+1}"

    # Mesangem com: número de sequencia, horário do envio, 
    # tamanho do conteúdo, e o conteúdo em si
    completeMessage = f"{seq}|{timeSend}|{len(payload)}|{payload}"
    
    client.sendall(completeMessage.encode())
    resposta = client.recv(1024).decode()
    print(f"Servidor respondeu: {resposta}")

client.close()