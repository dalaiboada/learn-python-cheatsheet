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

# `isnull()`

El método `isnull()` sirve para **detectar valores faltantes**.

## Con un DataFrame

### Sintaxis

```python
df.isnull()
```

Ejemplo:

```python
print(df.isnull())
```

Resultado:

```text
   Nombre   Edad   Nota  Ciudad
0   False  False  False   False
1   False   True  False   False
2   False  False   True    True
3   False  False  False   False
4   False   True  False   False
```

`True` significa:

> Aquí falta un valor.

`False` significa:

> Aquí tenemos un valor.

---

## Con una Series

También podemos comprobar solamente una columna:

```python
print(df['Edad'].isnull())
```

Resultado:

```text
0    False
1     True
2    False
3    False
4     True
```

Una columna de un DataFrame es una **Series**.

---

## Contar valores faltantes

Podemos combinar `isnull()` con `sum()`:

```python
print(df.isnull().sum())
```

Resultado:

```text
Nombre    0
Edad      2
Nota      1
Ciudad    1
```

Esto nos permite saber cuántos datos faltan en cada columna.

---

## Argumentos de `isnull()`

`isnull()` **no necesita argumentos**.

```python
df.isnull()
```

o:

```python
df['Edad'].isnull()
```

| Objeto    | ¿Funciona?                 | Resultado                                  |
| --------- | -------------------------- | ------------------------------------------ |
| Series    | Sí                         | Comprueba cada valor                       |
| DataFrame | Sí                         | Comprueba cada celda                       |
| Fila      | No se utiliza directamente | Una fila se maneja normalmente como Series |

---
