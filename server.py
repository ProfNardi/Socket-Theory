import socket

"""
SOCKET API - SERVER TCP
Vedi README.md per la teoria completa e il diagramma Socket API
"""

# ===== CONFIGURAZIONE =====
ADDRESS_FAMILY = socket.AF_INET     # IPv4
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SERVER_HOST = 'localhost'           # Indirizzo di ascolto
SERVER_PORT = 5000                  # Porta di ascolto

print("\n=== SERVER TCP - Avvio ===")

# FASE 1: socket() - Crea socket (Open Listen)
server = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print(f"[1] Socket creato")

# FASE 2: bind() - Associa socket a (IP, porta) (Open Listen)
server.bind((SERVER_HOST, SERVER_PORT))
print(f"[2] Bind su {SERVER_HOST}:{SERVER_PORT}")

# FASE 3: listen() - Mette in ascolto (Open Listen)
server.listen(5)  # backlog = 5 connessioni in coda
print(f"[3] Server in ascolto...")

try:
    while True:  # Server iterativo (un client alla volta)
        # FASE 4: accept() - Accetta connessione (Connection Request completato)
        # Ritorna una NUOVA socket per questo client specifico
        client_socket, client_address = server.accept()
        print(f"\n[4] Accept: connessione da {client_address}")

        # FASE 5: read/recv() - Riceve dati (Client/Server Session)
        data = client_socket.recv(1024)  # Max 1024 bytes
        messaggio = data.decode('utf-8')  # bytes -> str
        print(f"[5] Read: '{messaggio}'")

        # FASE 6: write/send() - Invia risposta (Client/Server Session)
        risposta = "Messaggio ricevuto correttamente!"
        client_socket.sendall(risposta.encode('utf-8'))  # str -> bytes
        print(f"[6] Write: '{risposta}'")

        # FASE 7: close() - Chiude connessione client (End Of File)
        client_socket.close()
        print(f"[7] Connessione con {client_address} chiusa")

except KeyboardInterrupt:
    print("\n\n[!] Server interrotto (Ctrl+C)")
finally:
    # FASE 8: close() - Chiude socket server
    server.close()
    print("[8] Socket server chiusa\n")