import os
import pyaes

# Abrir o arquivo criptografado do laboratorio
file_name = "teste.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Mesma chave usada na criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Recriar o arquivo original
new_file = "teste.txt"
new_file = open(new_file, "wb")
new_file.write(decrypt_data)
new_file.close()
