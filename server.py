import socket

# Server Side
# TCP iterativo che accetta connessioni da un client alla volta.

# ===== CONFIGURAZIONE =====
ADDRESS_FAMILY = socket.AF_INET     # IPv4
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SERVER_HOST = '0.0.0.0'             # Indirizzo di ascolto
SERVER_PORT = 5000                  # Porta di ascolto

print("=== SERVER TCP - Avvio ===")
# Primitiva 1: socket() - Crea socket (Open Listen)
server = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print(f"Primitiva 1: Socket creato")

# FASE 2: bind() - Associa socket a (IP, porta) (Open Listen)
server.bind((SERVER_HOST, SERVER_PORT))
print(f"Primitiva 2: Bind su {SERVER_HOST}:{SERVER_PORT}")

# Primitiva 3: listen() - Mette in ascolto (Open Listen)
server.listen(20)  # backlog = 20 connessioni in coda
print(f"Primitiva 3: Server in ascolto...")

try:
    while True:  # Server iterativo (un client alla volta)
        # Primitiva 4: accept() - Accetta connessione (Connection Request completato)
        # Ritorna una NUOVA socket per questo client specifico
        client_socket, client_address = server.accept()
        print(f"Primitiva 4: Accept: connessione da {client_address}")

        # ===== SESSIONE =====
        while True:
            # Primitiva 5: read/recv() - Riceve dati dal Client
            data = client_socket.recv(1024)  # Max 1024 bytes
            messaggio = data.decode('utf-8')  # bytes -> str
            print(f"Primitiva 5: Server riceve dal Client {client_address}: '{messaggio}'")

            # Primitiva 6: write/send() - Invia risposta (Client/Server Session)
            risposta = "Messaggio ricevuto!"
            client_socket.sendall(risposta.encode('utf-8'))  # str -> bytes
            print(f"Primitiva 6: Server invia al Client {client_address}: '{risposta}'")
            
            # Protocollo di uscita:
            if (messaggio.lower() == 'exit'):
                print(f"Chiusura sessione con {client_address}")
                break
        # ===== CHIUSURA =====

        #Chiude connessione col Client ma resta in ascolto (Double 2-way handshake) 
        client_socket.close()
        print(f"Socket client chiusa {client_address} chiusa")

except KeyboardInterrupt:
    print("Server interrotto (Ctrl+C)")
finally:
    # Primitiva 7: close() - Chiude socket server
    server.close()
    print(f"Primitiva 7: Socket server chiusa\n")