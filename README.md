# 🔐 Generador Seguro de Contraseñas

---

## 👤 Integrantes
| Nombre | Rol |
|---|---|
| Ronald Xavier Aguilar Alban | Desarrollador principal |

**Docente:** Mónica Patricia Salazar Tapia  
**Materia:** Lógica de Programación  
**Paralelo:** 1C  
**Universidad:** Universidad Internacional del Ecuador (UIDE)  
**Fecha:** Junio 2026

---

## 🎯 Objetivo del sistema

Desarrollar un programa en Python que permita generar contraseñas seguras y personalizables, respondiendo a la necesidad real de proteger la información personal en entornos digitales. El sistema aplica el estándar **NIST SP 800-63B** para contraseñas robustas y demuestra el impacto positivo que la tecnología puede tener en la seguridad cotidiana de las personas.

---

## 📋 Descripción del problema

En la actualidad, la ciberseguridad es un aspecto fundamental del uso de plataformas digitales. Sin embargo, muchas personas siguen utilizando contraseñas débiles, repetidas o predecibles —como fechas de nacimiento, nombres o secuencias numéricas— lo que incrementa significativamente el riesgo de accesos no autorizados y robo de información.

Este programa surge como respuesta a esa problemática, proporcionando una solución automatizada, accesible y segura para la generación de contraseñas.

---

## ⚙️ Descripción de funcionalidades

| Funcionalidad | Descripción |
|---|---|
| **Configurar longitud** | El usuario define la cantidad de caracteres (mínimo 8, recomendado 12+) |
| **Incluir mayúsculas** | Agrega letras mayúsculas (A-Z) al conjunto de caracteres |
| **Incluir números** | Incorpora dígitos (0-9) para mayor complejidad |
| **Incluir símbolos** | Añade caracteres especiales (`!@#$%^&*...`) |
| **Generación segura** | Usa el módulo `secrets` de Python (criptográficamente seguro) |
| **Evaluación de fortaleza** | Clasifica la contraseña como Débil, Media o Fuerte |
| **Historial de sesión** | Muestra todas las contraseñas generadas al finalizar |
| **Validación de entrada** | Controla errores de entrada del usuario con estructuras repetitivas |

---

## 🛠️ Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3.x** | Lenguaje de programación principal |
| **Módulo `secrets`** | Generación criptográficamente segura de aleatoriedad |
| **Módulo `string`** | Conjuntos de caracteres predefinidos |
| **GitHub** | Control de versiones y colaboración |
| **Lucidchart** | Elaboración de diagramas UML y de flujo |

---

## 🌍 Relación con el impacto tecnológico en la sociedad

La ciberseguridad es uno de los retos más importantes de la era digital. Según el NIST y múltiples estudios de seguridad informática, el uso de contraseñas débiles representa uno de los vectores de ataque más comunes. Este proyecto demuestra cómo una solución de software simple puede tener un impacto directo en la protección de la información personal de millones de personas, siendo una aplicación concreta del conocimiento informático al servicio de la sociedad.

---

## ▶️ Cómo ejecutar el programa

```bash
# Clonar el repositorio
git clone https://github.com/Ronaldaguilar-design/Generador-de-contrase-as-segura.git

# Navegar al directorio
cd Generador-de-contrase-as-segura/src

# Ejecutar el programa (requiere Python 3.x)
python generador_contrasenas.py
```

---

## ⚠️ Limitaciones e implicaciones

**Limitaciones:**
- El programa opera en entorno de consola (CLI), sin interfaz gráfica
- Las contraseñas generadas no se almacenan de forma persistente entre sesiones
- No incluye integración con gestores de contraseñas externos
- La evaluación de fortaleza es estimada, no basada en análisis de entropía formal

**Implicaciones:**
- Fomenta buenas prácticas de seguridad digital en usuarios no técnicos
- Puede ser extendido con una interfaz gráfica (Tkinter/web) en futuras versiones
- El uso de `secrets` garantiza que las contraseñas no sean predecibles por ataques de fuerza bruta simple

---

*Proyecto desarrollado como parte del curso de Lógica de Programación — UIDE 2026*
