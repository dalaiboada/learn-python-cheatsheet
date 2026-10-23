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

# `fillna()`

`fillna()` sirve para **reemplazar valores faltantes**.

## Con una Series

Podemos reemplazar los valores faltantes de `Edad`:

```python
df['Edad'] = df['Edad'].fillna(15)
```

Antes:

```text
15
NaN
14
16
NaN
```

Después:

```text
15
15
14
16
15
```

---

## Con un DataFrame

También podemos rellenar los valores faltantes de todo el DataFrame:

```python
df = df.fillna(0)
```

Esto reemplazaría todos los `NaN` por `0`.

Sin embargo, normalmente queremos utilizar un valor apropiado para cada columna.

Por ejemplo:

```python
df['Edad'] = df['Edad'].fillna(df['Edad'].mean())
```

Aquí los valores faltantes de `Edad` se reemplazan por la edad promedio.

---

## Argumentos principales de `fillna()`

La forma básica es:

```python
df.fillna(value)
```

### `value`

Indica qué valor utilizar para reemplazar los datos faltantes.

```python
df['Edad'].fillna(15)
```

También puede ser un diccionario cuando trabajamos con varias columnas:

```python
df.fillna({
    'Edad': 15,
    'Nota': 0,
    'Ciudad': 'Desconocida'
})
```

Cada columna recibe su propio valor.

---

## ¿Dónde podemos utilizar `fillna()`?

| Objeto    | ¿Funciona?             | Ejemplo                 |
| --------- | ---------------------- | ----------------------- |
| Series    | Sí                     | `df['Edad'].fillna(15)` |
| DataFrame | Sí                     | `df.fillna(0)`          |
| Fila      | Una fila es una Series | `fila.fillna(0)`        |

---
