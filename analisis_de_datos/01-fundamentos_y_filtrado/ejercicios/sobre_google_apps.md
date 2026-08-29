# Guía del Dataset: Aplicaciones de Google Play Store

Utilizaremos una tabla (dataset) que contiene información real sobre diferentes aplicaciones disponibles en la tienda **Google Play Store**.

---

## ¿De qué trata este conjunto de datos?

Cada fila representa una **aplicación móvil** y recopila detalles sobre su popularidad, tamaño, precio y compatibilidad con teléfonos Android. Nos servirá para responder preguntas como:

* ¿Cuáles son las categorías con más descargas?
* ¿Las aplicaciones de pago tienen mejores calificaciones que las gratuitas?
* ¿Qué tanto espacio ocupan los juegos más populares?

---

## 📋 Diccionario de Columnas (Datos explicados paso a paso)

A continuación se muestra el nombre original en inglés, su traducción y qué representa cada dato:

| Columna Original         | Traducción / Nombre        | ¿Qué significa?                                                                                  | Ejemplo en la tabla                                |
| :----------------------- | :-------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| **App**            | Nombre de la App            | El nombre oficial de la aplicación.                                                               | *Subway Surfers*, *ibis Paint X*               |
| **Category**       | Categoría                  | El género o tema de la aplicación.                                                               | `GAME` (Juegos), `EDUCATION` (Educación)      |
| **Rating**         | Calificación               | Nota promedio dada por los usuarios (de 1.0 a 5.0 estrellas).                                      | `4.5` ⭐                                         |
| **Reviews**        | Reseñas                    | Número total de opiniones escritas por los usuarios.                                              | `27722264`                                       |
| **Size**           | Tamaño del archivo         | Espacio que ocupa la app al descargarse (en Megabytes, MB).                                        | `76.0` (76 MB)                                   |
| **Installs**       | Descargas                   | Cantidad estimada de veces que se ha instalado.                                                    | `1000000000.0` (Mil millones)                    |
| **Type**           | Tipo de acceso              | Si la aplicación se puede descargar gratis o es de pago.                                          | `Free` (Gratis) o `Paid` (De pago)             |
| **Price**          | Precio                      | Costo de la aplicación en dólares ($ USD). Si es gratis, es `0.0`. | `0.0`, `4.99` ($4.99) |                                                    |
| **Content Rating** | Clasificación de contenido | Edad recomendada para usar la aplicación según su contenido.                                     | `Everyone` (Para todos), `Teen` (Adolescentes) |
| **Last Updated**   | Última actualización      | Fecha en la que los creadores publicaron la última mejora.                                        | *"July 12, 2018"*                                |
| **Current Ver**    | Versión actual             | Número de versión de la aplicación.                                                             | `1.90.0`, `Varies with device`                 |
| **Android Ver**    | Versión mínima de Android | La versión mínima del sistema operativo que necesita tu teléfono.                               | `4.1 and up` (Android 4.1 o superior)            |

---

## Ejemplo de un Registro (Una fila de la tabla)

Veamos cómo se lee una fila completa de nuestra tabla:

> **Aplicación:** *Subway Surfers*
>
> * **Categoría:** Juegos (`GAME`)
> * **Calificación:** 4.5 / 5.0 estrellas
> * **Reseñas:** Más de 27 millones de comentarios
> * **Tamaño:** 76 MB
> * **Descargas:** Más de 1,000,000,000 instalaciones
> * **Tipo y Precio:** Gratis (`Free`, $0.0)
> * **Público:** Mayores de 10 años (`Everyone 10+`)
> * **Actualización:** 12 de julio de 2018
> * **Versión de la app:** 1.90.0
> * **Requisito del celular:** Android 4.1 o superior

---

## 💡 Ideas para explorar

1. **El Top 5:** Encuentra los 5 juegos con mayor cantidad de descargas.
2. **Juegos vs. Educación:** Compara el promedio de calificación entre las apps de `GAME` y `EDUCATION`.
3. **¿Vale la pena pagar?:** Identifica cuál es la app de pago más cara y cuántas descargas tiene.
