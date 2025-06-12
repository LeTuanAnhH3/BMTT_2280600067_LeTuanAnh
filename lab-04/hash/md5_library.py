from hashlib import md5

def md5_hash(data):
    h = md5()
    h.update(data)
    return h.digest()

if __name__ == "__main__":
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed = md5_hash(text)
    print("MD5 Hash:", hashed.hex())