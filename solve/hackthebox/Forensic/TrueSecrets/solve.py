from Crypto.Cipher import DES
import base64

def restore_log(file_path, key, iv):
    with open(file_path, 'r') as file:
        encrypted_lines = file.readlines()

    retstr = []
    for encrypted_line in encrypted_lines:
        decrypted_line = decrypt(encrypted_line.strip(), key, iv)
        print(decrypted_line)
        retstr.append(decrypted_line)
    with open(file_path + ".decoded.log", "w") as fout:
        fout.write("\n".join(retstr))


def decrypt(ciphertext, key, iv):
    # Base64デコード
    encrypted_data = base64.b64decode(ciphertext)
    
    # DES復号器を作成
    des = DES.new(key.encode('utf-8'), DES.MODE_CBC, iv.encode('utf-8'))
    
    # 復号化してパディングを除去
    decrypted_data = des.decrypt(encrypted_data)
    return decrypted_data.rstrip(b'\x00').decode('utf-8')


if __name__ == "__main__":
    # キーとIV
    key = "AKaPdSgV"
    iv = "QeThWmYq"

    # 暗号化されたログファイルのパス
    log_file = "log/5818acbe-68f1-4176-a2f2-8c6bcb99f9fa.log.enc"
    restore_log(log_file, key, iv)

    log_file = "log/c65939ad-5d17-43d5-9c3a-29c6a7c31a32.log.enc"
    restore_log(log_file, key, iv)

    log_file = "log/de008160-66e4-4d51-8264-21cbc27661fc.log.enc"
    restore_log(log_file, key, iv)
