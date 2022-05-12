import socket
from Crypto.Cipher import AES
# Librería que nos permitirá obtener el firma por medio de las llaves
from nacl.signing import VerifyKey
import Aleatorios

host = '127.0.0.1'
puerto = 4000
FORMAT = "utf-8"
SIZE = 1024

# Se genera una función que nos pérmite generar un socket y conectarnos con cliente para escuhar a través de un puerto
def main():
    print("El servidor esta arrancando...")
    servertcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servertcp.bind((host, puerto))
    servertcp.listen(3)
    print("El servidor está escuchando...")

# Mientras lo demás sea verdad se acepta la conexión
    while True:
        conn, address = servertcp.accept()
        print(f"La conexión desde: {address}")

# Se generan los bytes de la key, al igual que la firma y la verificacion. Se recibe la información indicando el tamaño
        with conn:
            kbytes = servertcp.recv(32)
            firma = servertcp.recv(64)
            verificacion = VerifyKey(kbytes)
            data = conn.recv(SIZE)

            while (data):
                verificacion.verify(filename.read(), firma)

# Se cifra el archivo de texto con la key
        with open("mandar/recibido.txt", "rb") as filename:
            file = conn.recv(1024)
            key = Aleatorios.numeros
            cifrador = AES.new(key, AES.MODE_EAX)
            filecifrado, tag = cifrador.encrypt_and_digest(file)
            filename.write(filecifrado)

#Se cierra la conexión
        conn.close()
        print("Desconectado")


if __name__ == "__main__":
    main()




