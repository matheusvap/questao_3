from Crypto.Cipher import AES
from binascii import unhexlify
from Crypto.Util.Padding import unpad

# Dados fornecidos
chave = "thisisasecretkey"           # Chave de 128 bits (16 bytes)
codigo_hex = "a57fd9725fb53c53d5bd0b56185da50f70ab9baea5a43523b76c03e3eb989a20"  # Código em hexadecimal

# Convertendo a chave e o código hexadecimal para bytes
key_bytes = chave.encode('utf-8')
code_bytes = unhexlify(codigo_hex)

# Configurando o algoritmo AES no modo ECB
cipher = AES.new(key_bytes, AES.MODE_ECB)

# Decodificando o código
decrypted_bytes = cipher.decrypt(code_bytes)

# Removendo o padding
decrypted_bytes = unpad(decrypted_bytes, AES.block_size)

decrypted_text = decrypted_bytes.decode("utf-8")

print("Texto decodificado:", decrypted_text)