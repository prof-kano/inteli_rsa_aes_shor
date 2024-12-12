import random
import os
from sympy import isprime, mod_inverse, gcd
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def generate_prime(bits=8):
    while True:
        p = random.getrandbits(bits)
        if isprime(p):
            return p

def rsa_key_generation(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while p == q:
        q = generate_prime(bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi_n) != 1:
        e += 2  # Caso de fallback
    d = mod_inverse(e, phi_n)
    return (n, e, d, p, q)

def rsa_encrypt(msg, pubkey):
    n, e = pubkey
    m = int.from_bytes(msg, 'big')
    c = pow(m, e, n)
    return c.to_bytes((c.bit_length() + 7) // 8, 'big')

def rsa_decrypt(ciphertext, privkey):
    n, d = privkey
    c = int.from_bytes(ciphertext, 'big')
    m = pow(c, d, n)
    return m.to_bytes((m.bit_length() + 7) // 8, 'big').rjust(16, b'\0')

def aes_encrypt(msg, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(msg, AES.block_size)), iv

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

def save_keys_and_data(pubkey, privkey, aes_key, encrypted_aes_key, message, ciphertext, iv):
    os.makedirs('public', exist_ok=True)
    os.makedirs('private', exist_ok=True)
    with open('public/public_key.bin', 'wb') as f:
        f.write(pubkey[0].to_bytes((pubkey[0].bit_length() + 7) // 8, 'big'))
        f.write(pubkey[1].to_bytes((pubkey[1].bit_length() + 7) // 8, 'big'))
    with open('public/encrypted_aes_key.bin', 'wb') as f:
        f.write(encrypted_aes_key)
    with open('public/encrypted_message.bin', 'wb') as f:
        f.write(ciphertext)
    with open('public/iv.bin', 'wb') as f:
        f.write(iv)
    with open('private/private_key.bin', 'wb') as f:
        f.write(privkey[0].to_bytes((privkey[0].bit_length() + 7) // 8, 'big'))
        f.write(privkey[1].to_bytes((privkey[1].bit_length() + 7) // 8, 'big'))
    with open('private/aes_key.bin', 'wb') as f:
        f.write(aes_key)
    with open('private/clean_message.bin', 'wb') as f:
        f.write(message)

def main():
    n, e, d, p, q = rsa_key_generation()
    pubkey = (n, e)
    privkey = (n, d)
    aes_key = os.urandom(16)
    encrypted_aes_key = rsa_encrypt(aes_key, pubkey)
    decrypted_aes_key = rsa_decrypt(encrypted_aes_key, privkey)
    message = b'COLOQUE A FRASE DO SEU GRUPO AQUI'
    ciphertext, iv = aes_encrypt(message, decrypted_aes_key)
    plaintext = aes_decrypt(ciphertext, decrypted_aes_key, iv)
    save_keys_and_data(pubkey, privkey, aes_key, encrypted_aes_key, message, ciphertext, iv)
    print(f"Mensagem original: {message}")
    print(f"Mensagem criptografada (AES): {ciphertext}")
    print(f"Mensagem descriptografada (AES): {plaintext}")

if __name__ == "__main__":
    main()
