from hashlib import blake2s

def blake2_hash(data):
    h = blake2s()
    h.update(data)
    return h.digest()

if __name__ == "__main__":
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed = blake2_hash(text)
    print("Blake2s Hash:", hashed.hex())