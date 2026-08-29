# 🐍 Python Core Concepts & Cheat Sheet

Repositorio de referencia técnica para mis estudiantes. Aquí encontrarás un resumen conciso de los conceptos fundamentales de Python, organizados como "píldoras" de rápido acceso.

Incluyen tabla comparativas, definiciones y ejemplos prácticos de sintaxis.

---

## 📁 Contenido del Repositorio

Explora los módulos especializados del repositorio:

| Carpeta de referencia    | Tema                                                                                                          | Descripción                                                                                                                                                                            | Enlace                                 |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| `01-tipos_de_datos`    | Tipos de Datos                                                                                                | Introducción a los tipos de datos en Python y su mutabilidad.                                                                                                                          | [Ver](./01-tipos_de_datos/README.md)    |
| `02-funciones_nativas` | Herramientas esenciales (print, input), conversión de tipos, inspección (dir, help) y cálculo matemático. | Funciones integradas (print, input), concatenación y manejo de entrada de datos.                                                                                                       | [Ver](./02-funciones_nativas/README.md) |
| `03-operadores`        | Operadores                                                                                                    | Cálculos aritméticos, comparaciones lógicas y manejo de valores booleanos.                                                                                                           | [Ver](./03-operadores/README.md)        |
| `04-condicionales`     | Condicionales                                                                                                 | Toma de decisiones usando`if`, `elif` y `else`.                                                                                                                                   | [Ver](./04-condicionales/README.md)     |
| `05-ciclos`            | Ciclos                                                                                                        | Repetición de código con`while` y `for`, uso de `range` y control de flujo.                                                                                                     | [Ver](./05-ciclos/README.md)            |
| `06-cadenas`           | Cadenas                                                                                                       | Manipulación de strings, slicing, métodos de objeto y operaciones de secuencia.                                                                                                       | [Ver](./06-cadenas/README.md)           |
| `07-listas`            | Listas                                                                                                        | Gestión de colecciones ordenadas: creación, acceso, métodos y funciones nativas.                                                                                                     | [Ver](./07-listas/README.md)            |
| `08-diccionarios`      | Diccionarios                                                                                                  | Estructuras clave-valor para búsquedas rápidas y gestión de datos complejos.                                                                                                         | [Ver](./08-diccionarios/README.md)      |
| `09-tuplas`            | Tuplas                                                                                                        | Colecciones inmutables, optimización de memoria y uso de desempaquetado.                                                                                                               | [Ver](./09-tuplas/README.md)            |
| `10-conjuntos`         | Conjuntos                                                                                                     | Colecciones únicas, eliminación de duplicados y operaciones matemáticas (unión, intersección).                                                                                     | [Ver](./10-conjuntos/README.md)         |
| `11-funciones`         | Funciones                                                                                                     | Modularización del código, parámetros, retorno y reutilización.                                                                                                                     | [Ver](./11-funciones/README.md)         |
| `pygame`               | Pygame                                                                                                        | Módulo de videojuegos 2D: ventana, eventos, sprites y más.                                                                                                                            | [Ver](./pygame/README.md)               |
| `analisis_de_datos`    | Análisis de Datos                                                                                            | Módulo para análisis de datos con pandas y numpy.                                                                                                                                     | [Ver](./analisis_de_datos/README.md)    |
| `Desarrollo web`       | Desarrollo web                                                                                                | Módulo para el desarrollo de software web con interfaces, backend y base de datos usando herramientas como HTML, css, python, SQL y sqlite, Flask, motores de plantillas y mucho más. | [Ver](./desarrollo_web/README.md)       |

---

# 📘Conceptos Fundamentales de Python

## Tipos de Dato

| Tipo                | Ejemplo                                   | ¿Qué es?                                   |
| :------------------ | :---------------------------------------- | :------------------------------------------- |
| **`int`**   | `42`, `-7`, `0`                     | Números enteros. Sin decimales.             |
| **`float`** | `3.14`, `-0.5`, `1e3`               | Números con decimales.                      |
| **`str`**   | `"hola"`, `'Python'`, `f"{nombre}"` | Cadenas de texto. Se definen con comillas.   |
| **`bool`**  | `True`, `False`                       | Solo dos valores: verdadero o falso.         |
| **`list`**  | `[1, 2, 3]`, `["a", "b"]`             | Colección ordenada y**mutable**.      |
| **`tuple`** | `(1, 2, 3)`, `("x", "y")`             | Colección ordenada e**inmutable**.    |
| **`dict`**  | `{"nombre": "Ana", "edad": 20}`         | Pares clave-valor.                           |
| **`set`**   | `{1, 2, 3}`                             | Colección**sin duplicados** ni orden. |

### Conversión entre tipos

```python
int("10")       # str → int → 10
str(3.14)       # float → str → "3.14"
float("2.5")    # str → float → 2.5
list("abc")     # str → list → ["a", "b", "c"]
tuple([1,2])    # list → tuple → (1, 2)
```

---

## Entrada y Salida de Datos

| Operación                   | Código                                   | Resultado                         |
| :--------------------------- | :---------------------------------------- | :-------------------------------- |
| **Imprimir**           | `print("Hola")`                         | Muestra texto en consola.         |
| **Imprimir variables** | `print(f"Tengo {edad} años")`          | Inserta valores con f-strings.    |
| **Imprimir múltiple** | `print("A", "B", sep="-")`              | Personaliza el separador:`A-B`. |
| **Pedir datos**        | `nombre = input("¿Cómo te llamas? ")` | Siempre devuelve un**str**. |
| **Pedir número**      | `edad = int(input("Edad: "))`           | Convierte la entrada a entero.    |

### Formateo de strings (f-strings)

```python
nombre = "Ana"
edad = 20
print(f"Me llamo {nombre} y tengo {edad} años")
print(f"Pi ≈ {3.14159:.2f}")          # 2 decimales: 3.14
print(f"{'centro':^20}")               # Centrado en 20 espacios
print(f"{255:#b}", f"{255:#x}")       # Binario: 0b11111111, Hex: 0xff
```

---

## Operadores

### Aritméticos

| Operador | Ejemplo    | Resultado                    |
| :------- | :--------- | :--------------------------- |
| `+`    | `5 + 3`  | `8`                        |
| `-`    | `5 - 3`  | `2`                        |
| `*`    | `5 * 3`  | `15`                       |
| `/`    | `5 / 3`  | `1.666...` (siempre float) |
| `//`   | `5 // 3` | `1` (división entera)     |
| `%`    | `5 % 3`  | `2` (módulo / residuo)    |
| `**`   | `5 ** 3` | `125` (potencia)           |

### Comparación

| Operador        | Significado                   |
| :-------------- | :---------------------------- |
| `==`          | Igual que                     |
| `!=`          | Diferente de                  |
| `>` / `<`   | Mayor / menor que             |
| `>=` / `<=` | Mayor o igual / menor o igual |

### Lógicos

| Operador | Ejemplo            | Resultado |
| :------- | :----------------- | :-------- |
| `and`  | `True and False` | `False` |
| `or`   | `True or False`  | `True`  |
| `not`  | `not True`       | `False` |

---

## Estructuras de Control

### Condicional

```python
if condicion:
    # se ejecuta si es True
elif otra_condicion:
    # se ejecuta si la primera falla y esta es True
else:
    # se ejecuta si ninguna fue True
```

### Bucle `for`

```python
# Recorrer una lista
for fruta in ["manzana", "plátano", "uva"]:
    print(fruta)

# Recorrer un rango
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

# Recorrer un diccionario
for clave, valor in {"a": 1, "b": 2}.items():
    print(f"{clave}: {valor}")
```

### Bucle `while`

```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Control de flujo

| Palabra      | Qué hace                        |
| :----------- | :------------------------------- |
| `break`    | Sale del bucle completamente.    |
| `continue` | Salta a la siguiente iteración. |
| `pass`     | No hace nada (placeholder).      |

---

### Resumen de Estructuras de Datos

| Estructura          | Mutable | Ordenada | Duplicados | Ejemplo              | Acceso               |
| :------------------ | :------ | :------- | :--------- | :------------------- | :------------------- |
| **`list`**  | Sí     | Sí      | Sí        | `[1, 2, 3]`        | lista[0] = 1         |
| **`tuple`** | No      | Sí      | Sí        | `(1, 2, 3)`        | tupla[0]             |
| `dict`            | Sí     | No       | No         | `{"a": 1, "b": 2}` | diccionario["a"] = 1 |
| **`set`**   | Sí     | No       | No         | `{1, 2, 3}`        | conjunto.add(4)      |

---

## Funciones

```python
def saludar(nombre, saludo="Hola"):
    """Saluda a una persona."""
    return f"{saludo}, {nombre}!"

print(saludar("Ana"))                  # "Hola, Ana!"
print(saludar("Ana", saludo="Hey"))    # "Hey, Ana!"
```

### Parámetros especiales

| Sintaxis     | Qué hace                               | Ejemplo de llamada     |
| :----------- | :-------------------------------------- | :--------------------- |
| `*args`    | Argumentos posicionales extras (tuple). | `func(1, 2, 3)`      |
| `**kwargs` | Argumentos con nombre extras (dict).    | `func(nombre="Ana")` |

```python
def registrar(nombre, *cursos, **datos):
    print(nombre, cursos, datos)

registrar("Ana", "POO", "Pygame", edad=20, ciudad="Bogotá")
# Ana ('POO', 'Pygame') {'edad': 20, 'ciudad': 'Bogotá'}
```

---

## Programación Orientada a Objetos (POO)

> Para el contenido completo, revisa la carpeta [`00-introduccion_poo`](./00-introduccion_poo/).

| Concepto               | Ejemplo                 | Descripción                                   |
| :--------------------- | :---------------------- | :--------------------------------------------- |
| **Clase**        | `class Persona:`      | Molde / plantilla para crear objetos.          |
| **Objeto**       | `p = Persona("Ana")`  | Instancia concreta de una clase.               |
| **Atributo**     | `p.nombre`            | Variable que pertenece al objeto.              |
| **Método**      | `p.saludar()`         | Función dentro de una clase.                  |
| **`__init__`** | `def __init__(self):` | Constructor. Se ejecuta al crear el objeto.    |
| **`self`**     | `self.nombre`         | Referencia al objeto actual.                   |
| **Herencia**     | `class Hijo(Padre):`  | La hija hereda atributos y métodos del padre. |
| **`super()`**  | `super().__init__()`  | Llama al constructor de la clase padre.        |

---

## Módulos y Paquetes

```python
import math                    # Importa el módulo completo
print(math.pi)                 # 3.141592653589793

from random import randint     # Importa solo una función
print(randint(1, 10))          # Número aleatorio entre 1 y 10

import datetime as dt          # Alias corto
print(dt.date.today())         # Fecha de hoy
```

### Módulos útiles de la biblioteca estándar

| Módulo         | Para qué sirve                                          |
| :-------------- | :------------------------------------------------------- |
| `math`        | Funciones matemáticas (sqrt, ceil, floor, pi...).       |
| `random`      | Números aleatorios (randint, choice, shuffle...).       |
| `datetime`    | Fechas y horas.                                          |
| `os`          | Interacción con el sistema operativo (rutas, archivos). |
| `json`        | Leer y escribir archivos JSON.                           |
| `collections` | Estructuras de datos extras (Counter, defaultdict...).   |

---

## 💡 Comandos especiales

#### Verifica la **versión de Python** instalada en tu sistema:

```bash
python --version
```

---

## 🆘 Cómo obtener ayuda

- **`help(objeto)`**: Escríbelo en la consola (ej. `help(list)`) y Python te mostrará la documentación oficial de lo que necesites.
- **`dir(objeto)`**: Te lista todos los métodos disponibles para ese objeto.

## 📌 Recursos Adicionales

1. [Documentación oficial de Python](https://docs.python.org/3/)
2. [LabEx - Python CheatSheet](https://labex.io/pythoncheatsheet/cheatsheet/basics)
3. [W3 School](https://www.w3schools.com/python/default.asp)
4. [Python Playground](https://python-playground.com/)

---

**Nota:** Este es un documento vivo. Si algo no queda claro o encuentras un error, ¡Avísame!
