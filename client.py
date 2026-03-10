import socket

"""
SOCKET API - CLIENT TCP
Vedi README.md per la teoria completa e il diagramma Socket API
"""

# ===== CONFIGURAZIONE =====
ADDRESS_FAMILY = socket.AF_INET     # IPv4
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SERVER_HOST = 'localhost'           # Indirizzo del server
SERVER_PORT = 5000                  # Porta del server

print("\n=== CLIENT TCP - Avvio ===")

# FASE 1: socket() - Crea socket
client = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print(f"[1] Socket creato")

# FASE 2: connect() - Connessione al server (Three-way handshake)
client.connect((SERVER_HOST, SERVER_PORT))
print(f"[2] Connesso a {SERVER_HOST}:{SERVER_PORT}")

# FASE 3: write/send() - Invia dati (Client/Server Session)
messaggio = "Ciao Server sono un Client!"
client.send(messaggio.encode('utf-8'))  # str → bytes
print(f"[3] Write: '{messaggio}'")

# FASE 4: read/recv() - Riceve risposta (Client/Server Session)
data = client.recv(1024)  # Max 1024 bytes
print(f"[4] Read: '{data.decode('utf-8')}'")

# FASE 5: close() - Chiude connessione
client.close()
print(f"[5] Connessione chiusa\n")
