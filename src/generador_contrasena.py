import secrets
import string

# =============================================
# GENERADOR SEGURO DE CONTRASEÑAS
# Proyecto Integrador - Lógica de Programación
# Autor: Ronald Xavier Aguilar Alban
# Universidad Internacional del Ecuador - 2026
# =============================================

def generar_contrasena(longitud, mayusculas, numeros, simbolos):
    """Genera una contraseña aleatoria y segura según los parámetros dados."""
    # Estructura condicional para construir el conjunto de caracteres
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    # Uso de secrets para aleatoriedad criptográficamente segura
    contrasena = "".join(secrets.choice(caracteres) for i in range(longitud))
    return contrasena


def solicitar_si_no(mensaje):
    """Solicita al usuario una respuesta de si/no con validación."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ["si", "no"]:
            return respuesta == "si"
        print("Por favor ingrese 'si' o 'no'.")


def evaluar_fortaleza(longitud, mayusculas, numeros, simbolos):
    """Evalúa y retorna la fortaleza estimada de la contraseña."""
    puntos = 0
    if longitud >= 12:
        puntos += 1
    if longitud >= 16:
        puntos += 1
    if mayusculas:
        puntos += 1
    if numeros:
        puntos += 1
    if simbolos:
        puntos += 1

    # Estructura condicional para clasificar la fortaleza
    if puntos <= 2:
        return "⚠️  DÉBIL"
    elif puntos <= 3:
        return "🟡 MEDIA"
    else:
        return "✅ FUERTE"


# =============================================
# HISTORIAL DE CONTRASEÑAS GENERADAS
# =============================================
historial_contrasenas = []

# =============================================
# MENÚ PRINCIPAL - ESTRUCTURA REPETITIVA
# =============================================
print("=" * 46)
print("   GENERADOR SEGURO DE CONTRASEÑAS")
print("=" * 46)
print("Basado en el estándar NIST SP 800-63B")
print("Recomendación: mínimo 12 caracteres\n")

while True:
    print("\n--- Nueva contraseña ---")

    # Validación de longitud con estructura repetitiva
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (min. 8): "))
            if longitud < 8:
                print("La longitud mínima recomendada es 8 caracteres.")
                continue
            break
        except ValueError:
            print("Ingrese un número válido.")

    # Preguntas de personalización con estructuras condicionales
    mayusculas = solicitar_si_no("¿Incluir mayúsculas? (si/no): ")
    numeros    = solicitar_si_no("¿Incluir números?   (si/no): ")
    simbolos   = solicitar_si_no("¿Incluir símbolos?  (si/no): ")

    # Generación y salida de la contraseña
    contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
    fortaleza  = evaluar_fortaleza(longitud, mayusculas, numeros, simbolos)

    print("\n" + "=" * 46)
    print(f"  Contraseña generada: {contrasena}")
    print(f"  Fortaleza estimada:  {fortaleza}")
    print("=" * 46)

    # Agregar al historial
    historial_contrasenas.append(contrasena)

    # Control de finalización del bucle principal
    if not solicitar_si_no("\n¿Desea generar otra contraseña? (si/no): "):
        break

# =============================================
# HISTORIAL FINAL - ESTRUCTURA REPETITIVA
# =============================================
print("\n" + "=" * 46)
print("   HISTORIAL DE CONTRASEÑAS GENERADAS")
print("=" * 46)

for incidente, contrasena in enumerate(historial_contrasenas, start=1):
    print(f"  {incidente}. {contrasena}")

print("=" * 46)
print("Programa finalizado. ¡Gracias por usar el")
print("Generador Seguro de Contraseñas!")
print("=" * 46)
