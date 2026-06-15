import random
import string

print("=== Generador Seguro de Contraseñas ===")

longitud = int(input("Ingrese la longitud de la contraseña: "))

usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
usar_numeros = input("¿Incluir números? (s/n): ").lower() == "s"
usar_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

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

print("\nContraseña generada:")
print(contrasena)
