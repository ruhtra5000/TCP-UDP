import socket
import time

# Definião de IP e porta
HOST = '127.0.0.1'
PORT = 5001

# Tempo de timeout (segundos)
timeoutTime = 5

# Abertura do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.settimeout(timeoutTime)
server.bind((HOST, PORT))

# Dicionário de informações relevantes
info = {"amount_pck": 0, "lost_pck": 0}

# Vetor de dados recebidos
dataRecieved = []

# Calculo de RTT
def calculateRTT(timeSend):
    return time.time_ns() - int(timeSend)

# Calculo de Jitter 
def calculateJitter(rtt):
    if not dataRecieved:
        return 0

    jitter = rtt - dataRecieved[-1]["RTT"]
    
    return jitter if jitter > 0 else 0

# Checagem da ordenação dos pacotes
def verifyPackageOrder(actualSeq):
    if dataRecieved:
        if int(actualSeq) != dataRecieved[-1]["seq"] + 1:
            return False # Ordem errada
        
        return True # Ordem correta
    else:
        # Deve ser o pacote com seq 0 (Primeiro pacote)
        if int(actualSeq) != 0:
            return False
        
        return True
    
# Calculo de Throughput
def calculateThroughput(totalTime):
    sizeRecieved = 0
    
    for data in dataRecieved:
        sizeRecieved += data["len"]

    return (sizeRecieved*8) / totalTime

# "Main"
# Recebimento de mensagens UDP
def UDPServer():
    print("Servidor UDP aguardando mensagens...")
    while True:
        try:
            data, addr = server.recvfrom(1024)
            data = data.decode()

            seq, timeSend, len, payload = data.split('|', 3) # Divisão da mensagem
                
            rtt = calculateRTT(timeSend)
            jitter = calculateJitter(rtt)
                
            if not verifyPackageOrder(seq):
                info["lost_pck"] += 1

            # Salvando dados do pacote recebido
            dataRecieved.append({
                "seq": int(seq), 
                "timeSend": int(timeSend), 
                "len": int(len), 
                "payload": payload, 
                "RTT": rtt, 
                "jitter": jitter
            })
            info["amount_pck"] += 1

            # Resposta do servidor
            server.sendto("Mensagem recebida".encode(), addr)

        except ValueError:
            print("Mensagem mal formatada:", data)
        except socket.timeout:
            print("Timeout atingido. Encerrando servidor.")
            break

# Inicialização do servidor (marcando tempo total de operação)
start = time.time()
UDPServer()
end = time.time()

# Impressão de dados pós-operação
print(f'\n\ninfo: {info}\n')

for data in dataRecieved:
    print(f"{data}\n")

print(f"Throughput (bytes/s): {calculateThroughput(end - start - timeoutTime)}\n")