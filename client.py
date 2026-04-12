import socket

# Client Side
# TCP che si connette a un server, invia un messaggio e riceve una risposta.

# ===== CONFIGURAZIONE =====
ADDRESS_FAMILY = socket.AF_INET     # IPv4
SOCKET_TYPE = socket.SOCK_STREAM    # TCP
SERVER_HOST = 'localhost'           # (da modificare)Indirizzo del server
SERVER_PORT = 5000                  # (da modificare)Porta del server

print("\n=== CLIENT TCP - Avvio ===")

# Primitiva 1: socket() - Crea socket
client = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
print(f"Primitiva 1: Socket creato")

# Primitiva 2: connect() - Connessione al server (Three-way handshake)
client.connect((SERVER_HOST, SERVER_PORT))
print(f"Primitiva 2: Connesso a {SERVER_HOST}:{SERVER_PORT}")

# ===== SESSIONE =====
while True:
    # Primitiva 3: write/send() - Invia dati (Client/Server Session)
    messaggio = input("Digita exit per uscire oppure inserisci un messaggio: ")
    client.send(messaggio.encode('utf-8'))  # str → bytes
    print(f"Primitiva 3: Client invia: '{messaggio}'")

    # Primitiva 4: read/recv() - Riceve risposta (Client/Server Session)
    data = client.recv(1024)  # Max 1024 bytes
    print(f"Primitiva 4: Client riceve: '{data.decode('utf-8')}'")
    
    if (messaggio.lower() == 'exit'): #Protocollo di uscita.
                print(f"Chiusura sessione con {SERVER_HOST}:{SERVER_PORT}")
                break
# ===== SESSIONE =====

# Primitiva 5: close() - Chiude connessione (Double 2-way handshake) 
client.close()
print(f"Primitiva 5: Connessione Client chiusa\n")
