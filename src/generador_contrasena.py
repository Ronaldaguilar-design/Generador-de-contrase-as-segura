import random
import string

# Función para generar la contraseña
def generar_contrasena(longitud, mayusculas, numeros, simbolos):

    caracteres = string.ascii_lowercase

    if mayusculas:
        caracteres += string.ascii_uppercase

    if numeros:
        caracteres += string.digits

    if simbolos:
        caracteres += string.punctuation

    contrasena = ""

    for i in range(longitud):
        contrasena += random.choice(caracteres)

    return contrasena


# Menú principal
while True:

    print("\n===== GENERADOR SEGURO DE CONTRASEÑAS =====")

    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))

        if longitud <= 0:
            print("La longitud debe ser mayor que cero.")
            continue

    except ValueError:
        print("Ingrese un número válido.")
        continue

    mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    numeros = input("¿Incluir números? (s/n): ").lower() == "s"
    simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    contrasena = generar_contrasena(
        longitud,
        mayusculas,
        numeros,
        simbolos
    )

    print("\nContraseña generada:")
    print(contrasena)

    repetir = input(
        "\n¿Desea generar otra contraseña? (s/n): "
    ).lower()

    if repetir != "s":
        print("Programa finalizado.")
        break
