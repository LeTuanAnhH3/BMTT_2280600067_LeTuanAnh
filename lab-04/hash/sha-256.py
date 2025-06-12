from hashlib import sha256

def sha256_hash(data):
    h = sha256()
    h.update(data)
    return h.digest()

if __name__ == "__main__":
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed = sha256_hash(text)
    print("SHA-256 Hash:", hashed.hex())