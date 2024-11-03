from Crypto.Cipher import AES
from binascii import unhexlify
from Crypto.Util.Padding import unpad

def aes_decrypt_ecb(hex_code, key):
    """
    Decodifica um texto hexadecimal criptografado com AES em modo ECB.

    Parâmetros:
    - hex_code: Texto hexadecimal codificado (string).
    - key: Chave AES de 128 bits (16 caracteres, string).

    Retorna:
    - Texto decodificado (string).
    """
    # Convertendo a chave e o código hexadecimal para bytes
    key_bytes = key.encode('utf-8')
    code_bytes = unhexlify(hex_code)

    # Configurando o algoritmo AES no modo ECB
    cipher = AES.new(key_bytes, AES.MODE_ECB)

    # Decodificando o código
    decrypted_bytes = cipher.decrypt(code_bytes)

    # Removendo o padding
    decrypted_bytes = unpad(decrypted_bytes, AES.block_size)
    
    return decrypted_bytes.decode("utf-8")