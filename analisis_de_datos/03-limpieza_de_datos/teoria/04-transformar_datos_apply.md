# DataFrame de prueba

Utilizaremos el siguiente DataFrame para experimentar con los métodos:

```python
import pandas as pd

datos = {
    'Nombre': ['Ana', 'Carlos', 'Lucía', 'Mateo', 'Elena'],
    'Edad': [15, None, 14, 16, None],
    'Nota': [8.5, 9.0, None, 7.5, 10.0],
    'Ciudad': ['Miami', 'Madrid', None, 'Miami', 'Madrid']
}

df = pd.DataFrame(datos)

print(df)
```

Resultado:

```text
   Nombre  Edad  Nota  Ciudad
0     Ana  15.0   8.5   Miami
1  Carlos   NaN   9.0  Madrid
2   Lucía  14.0   NaN     NaN
3   Mateo  16.0   7.5   Miami
4   Elena   NaN  10.0  Madrid
```

`NaN` representa un valor que falta.

---

# `apply()`

`apply()` permite **aplicar una función a los valores de una Series**.

La diferencia con los métodos anteriores es que aquí podemos crear nuestra propia función.

### Sintaxis

```python
df['columna'].apply(funcion)
```

Primero creamos una función:

```python
def clasificar_nota(nota):
    if nota >= 9:
        return 'Excelente'
    elif nota >= 7:
        return 'Bien'
    else:
        return 'Necesita mejorar'
```

Después la aplicamos:

```python
df['Nota'].apply(clasificar_nota)
```

Pandas ejecuta la función para cada valor:

```text
8.5  → Bien
9.0  → Excelente
7.5  → Bien
10.0 → Excelente
```

---

# Crear una nueva columna con `apply()`

Podemos guardar el resultado en una nueva columna:

```python
df['Evaluación'] = df['Nota'].apply(clasificar_nota)
```

Ahora tendremos:

```text
   Nombre  Nota  Evaluación
0     Ana   8.5        Bien
1  Carlos   9.0   Excelente
2   Lucía   NaN          ...
3   Mateo   7.5        Bien
4   Elena  10.0   Excelente
```

Los valores `NaN` necesitan ser tratados antes si nuestra función no sabe trabajar con ellos.

---

# `apply()` sobre una Series

La forma que utilizaremos principalmente en esta lección es:

```python
df['columna'].apply(funcion)
```

Por ejemplo:

```python
def convertir_nombre(nombre):
    return nombre.upper()

df['Nombre'] = df['Nombre'].apply(convertir_nombre)
```

Cada nombre será transformado:

```text
Ana     → ANA
Carlos  → CARLOS
Lucía   → LUCÍA
```

---

# `apply()` sobre un DataFrame

`apply()` también puede utilizarse directamente sobre un DataFrame.

En este caso podemos indicar si queremos trabajar **por columnas o por filas**.

### Por columnas

```python
df.apply(funcion)
```

Por defecto:

```python
axis=0
```

La función se aplica a cada columna.

### Por filas

```python
df.apply(funcion, axis=1)
```

La función se aplica a cada fila.

Por ejemplo:

```python
def obtener_nombre(fila):
    return fila['Nombre']

df.apply(obtener_nombre, axis=1)
```

Aquí `fila` representa una fila completa del DataFrame.

---

# Argumentos principales de `apply()`

Para esta lección nos interesa principalmente:

```python
df.apply(funcion, axis=0)
```

o:

```python
df.apply(funcion, axis=1)
```

### `func`

La función que queremos aplicar:

```python
df['Edad'].apply(clasificar_edad)
```

### `axis`

Indica cómo recorrer el DataFrame:

```python
axis=0
```

→ columna por columna.

```python
axis=1
```

→ fila por fila.

---
