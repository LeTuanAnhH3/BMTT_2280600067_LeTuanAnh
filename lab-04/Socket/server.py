import socket
import threading
from hashlib import sha256

clients = []

def handle_client(client_socket, addr):
    print(f"[+] Kết nối từ {addr}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            hashed = sha256(data).hexdigest()
            client_socket.sendall(f"SHA-256: {hashed}".encode('utf-8'))
    except:
        print(f"[-] Mất kết nối từ {addr}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 9999))
    server.listen(5)
    print("[*] Server đang lắng nghe...")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()