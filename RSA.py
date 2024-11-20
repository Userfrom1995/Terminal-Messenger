import random
from math import gcd



def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def generate_keys(bits=8):
    p = q = 0
    while not is_prime(p):
        p = random.getrandbits(bits)
    while not is_prime(q) or p == q:
        q = random.getrandbits(bits)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537
    while gcd(e, phi_n) != 1:
        e = random.randrange(2, phi_n)

    d = mod_inverse(e, phi_n)

    public_key = (n, e)
    private_key = (n, d)

    return public_key, private_key



def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message



def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message



if __name__ == "__main__":

    public_key, private_key = generate_keys(bits=8)

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")


    message = "Hello"
    print(f"Original Message: {message}")


    encrypted_message = encrypt(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")


    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
