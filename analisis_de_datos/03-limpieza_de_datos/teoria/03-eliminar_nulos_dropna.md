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

# `dropna()`

`dropna()` sirve para **eliminar datos que contienen valores faltantes**.

Por defecto, cuando lo usamos sobre un DataFrame, elimina las **filas** que contienen al menos un `NaN`.

### Sintaxis

```python
df.dropna()
```

Por ejemplo:

```python
nuevo_df = df.dropna()

print(nuevo_df)
```

Nuestro DataFrame tenía:

```text
Ana       → completo
Carlos    → falta Edad
Lucía     → falta Nota y Ciudad
Mateo     → completo
Elena     → falta Edad
```

Después de `dropna()` solamente quedan:

```text
Ana
Mateo
```

Porque son las únicas filas que no tienen ningún valor faltante.

---

# `dropna()` y el argumento `axis`

`dropna()` puede eliminar **filas o columnas**.

### Filas

Es el comportamiento predeterminado:

```python
df.dropna(axis=0)
```

También podemos escribir simplemente:

```python
df.dropna()
```

`axis=0` significa:

> Trabajar con las filas.

---

### Columnas

```python
df.dropna(axis=1)
```

Significa:

> Eliminar las columnas que contienen valores faltantes.

En nuestro ejemplo, eliminaría:

```text
Edad
Nota
Ciudad
```

porque esas columnas contienen `NaN`.

---

# `dropna()` con `how`

El argumento `how` indica **cuándo eliminar**.

## `how='any'`

Es el comportamiento predeterminado.

```python
df.dropna(how='any')
```

Significa:

> Elimina la fila si tiene **al menos un** valor faltante.

---

## `how='all'`

```python
df.dropna(how='all')
```

Significa:

> Elimina la fila solamente si **todos sus valores** son `NaN`.

Por ejemplo:

```text
Nombre    Edad    Nota
Ana       15      8.5
NaN       NaN     NaN
Carlos    16      9.0
```

Con:

```python
df.dropna(how='all')
```

se eliminaría solamente la segunda fila.

---

# `dropna()` con `subset`

A veces no queremos comprobar todas las columnas.

Podemos decirle a Pandas qué columnas revisar.

### Sintaxis

```python
df.dropna(subset=['columna'])
```

Por ejemplo:

```python
df.dropna(subset=['Edad'])
```

Esto elimina solamente las filas donde falta `Edad`.

También podemos indicar varias columnas:

```python
df.dropna(subset=['Edad', 'Nota'])
```

Ahora se eliminarán las filas donde falte `Edad` o `Nota`.

---

# Argumentos principales de `dropna()`

La sintaxis que necesitamos conocer es:

```python
df.dropna(
    axis=0,
    how='any',
    subset=None
)
```

### `axis`

Indica si trabajamos con:

```python
axis=0  # filas
axis=1  # columnas
```

### `how`

Indica cuándo eliminar:

```python
how='any'
```

→ si falta al menos un valor.

```python
how='all'
```

→ si faltan todos los valores.

### `subset`

Indica qué columnas revisar:

```python
subset=['Edad']
```

---

## Resumen de `dropna()`

| Código                       | Qué hace                     |
| ---------------------------- | ---------------------------- |
| `df.dropna()`                | Elimina filas con algún`NaN` |
| `df.dropna(axis=0)`          | Elimina filas                |
| `df.dropna(axis=1)`          | Elimina columnas             |
| `df.dropna(how='any')`       | Elimina si falta algún valor |
| `df.dropna(how='all')`       | Elimina si todos faltan      |
| `df.dropna(subset=['Edad'])` | Comprueba solamente`Edad`    |

---
