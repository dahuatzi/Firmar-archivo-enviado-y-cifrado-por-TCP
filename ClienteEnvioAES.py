import socket
# Librería que nos permitirá obtener el firma por medio de las llaves
from nacl.signing import SigningKey


host = '127.0.0.1'
puerto = 4000
FORMAT = "utf-8"
SIZE = 1024

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, puerto))
    archivo = "recibido.txt"

    with open(archivo, "wb") as filename:
        send = filename.read(SIZE)
        kbyte = SigningKey.generate()
        firma = kbyte.sign(send)
        verificacion = kbyte.verify_key
        verificacionhex = verificacion.encode()

        cliente.send(verificacionhex)
        cliente.send(firma.signature)
        cliente.send(send)

    print("Se envió exitosamente")
    cliente.close()




