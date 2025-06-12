import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))

    try:
        while True:
            text = input("Nhập chuỗi cần băm: ")
            if text == 'exit':
                break
            client.sendall(text.encode('utf-8'))
            response = client.recv(1024)
            print("Từ server:", response.decode('utf-8'))
    finally:
        client.close()

if __name__ == "__main__":
    start_client()