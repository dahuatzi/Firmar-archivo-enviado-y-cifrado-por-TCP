# importamos las librerías de pynacl para generar lo numeros aleatorios
import nacl.utils
import nacl.hash
import nacl.encoding

# generamos la variable numeros que nos dará la extenxión de 73 (este numero se puede cambiar) numeros aleatorios
numeros = nacl.utils.random(13)
print("Numeros random:\n")

# for para que imprima la cadena
for char in numeros:
    print(str(char), end=" ")

# imprimir los número en byte
print("\n\nNumeros en byte:\n")
print(numeros)

# utilicé el código de caracteres ascii para obtener un hash
ascii = "".encode('ascii')
print("\n\nNumeros codificados con ascii:\n")
# generamos la variable que nos arroja el hash
numascii = nacl.hash.sha256(ascii, encoder=nacl.encoding.HexEncoder)
print(numascii)
