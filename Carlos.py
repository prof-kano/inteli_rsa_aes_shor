import os
from sympy import gcd, mod_inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def read_public_key(filename):
    with open(filename, 'rb') as f:
        contents = f.read()
        half_len = len(contents) // 2
        n = int.from_bytes(contents[:half_len], 'big')
        e = int.from_bytes(contents[half_len:], 'big')
    return n, e

def factorize(n):
    """Desafio, complete aqui."""
    return None, None

def derive_private_key(n, e, p, q):
    phi_n = (p - 1) * (q - 1)
    if gcd(e, phi_n) != 1:
        raise ValueError(f"The chosen 'e'={e} is not coprime with phi(n)={phi_n}.")
    d = mod_inverse(e, phi_n)
    return d

def decrypt_aes_key(encrypted_aes_key, privkey, n):
    d = privkey
    c = int.from_bytes(encrypted_aes_key, 'big')
    m = pow(c, d, n)
    aes_key = m.to_bytes((m.bit_length() + 7) // 8, 'big')
    return aes_key.rjust(16, b'\0')

def read_encrypted_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data

def decrypt_message(ciphertext, aes_key, iv):
    """Descriptografa a mensagem usando AES com CBC."""
    print(f"Usando chave AES: {aes_key.hex()} e IV: {iv.hex()}")
    if len(aes_key) != 16:
        raise ValueError(f"Incorrect AES key length: {len(aes_key)} bytes, expected 16 bytes")
    if len(iv) != 16:
        raise ValueError(f"Incorrect IV length: {len(iv)} bytes, expected 16 bytes")
    cipher = AES.new(aes_key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    try:
        return unpad(decrypted, AES.block_size)
    except ValueError as e:
        print("Erro: Padding está incorreto.")
        raise e

def main():
    n, e = read_public_key('public/public_key.bin')
    print(f"Lido n: {n}, e: {e}")
    p, q = factorize(n)
    if not p or not q:
        print("Erro: Não foi possível fatorar n em primos distintos.")
        return
    print(f"Fatorado com sucesso: p={p}, q={q}")

    d = derive_private_key(n, e, p, q)
    print(f"Chave privada derivada: d={d}")

    encrypted_aes_key = read_encrypted_file('public/encrypted_aes_key.bin')
    aes_key = decrypt_aes_key(encrypted_aes_key, d, n)
    print(f"Chave AES descriptografada: {aes_key.hex()}")

    ciphertext = read_encrypted_file('public/encrypted_message.bin')
    iv = read_encrypted_file('public/iv.bin')
    plaintext = decrypt_message(ciphertext, aes_key, iv)

    print("Mensagem descriptografada:", plaintext.decode())

if __name__ == '__main__':
    main()
