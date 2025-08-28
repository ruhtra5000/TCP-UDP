import socket
import time

# Definição de IP e porta
HOST = '127.0.0.1'
PORT = 5001

# Criação do socket do cliente
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Realiza o envio de mensagens UDP
for seq in range(5):
    timeSend = time.time_ns()
    payload = f"Mensagem UDP {seq+1}"

    # Mesangem com: número de sequencia, horário do envio, 
    # tamanho do conteúdo, e o conteúdo em si
    completeMessage = f"{seq}|{timeSend}|{len(payload)}|{payload}"
    
    client.sendto(completeMessage.encode(), (HOST, PORT))
    data, _ = client.recvfrom(1024)
    print(f"Servidor respondeu: {data.decode()}")

client.close()