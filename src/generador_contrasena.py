#print("hola mundo")

#IMportamos los recursos necesarios
import random
import string
#menu Principal
print("=== Generador Seguro de Contraseñas ===")
#configuraciones a aleccion del usuario
longitud = int(input("Ingrese la longitud de la contraseña: "))
usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"
#condicionales
caracteres = string.ascii_lowercase

if usar_mayusculas:
    caracteres += string.ascii_uppercase

if usar_numeros:
    caracteres += string.digits

if usar_simbolos:
    caracteres += string.punctuation

contrasena = ""

for _ in range(longitud):
    contrasena += random.choice(caracteres)
#resultado
print("Contraseña generada:")
print(contrasena)
