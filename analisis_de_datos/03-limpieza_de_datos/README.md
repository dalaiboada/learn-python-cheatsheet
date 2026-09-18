# Limpieza de datos en Pandas

Cuando trabajamos con datos reales, es común encontrar información que falta.

Por ejemplo:

- una persona no indicó su edad;
- no conocemos su salario;
- falta alguna información de una aplicación;
- una celda está vacía.

Pandas representa muchos de estos valores faltantes como `NaN`.

En esta lección aprenderemos a:

- detectar valores faltantes con `isnull()`;
- reemplazarlos con `fillna()`;
- eliminarlos con `dropna()`;
- transformar datos utilizando `apply()`.

## ¿Series, filas o DataFrame?

Es importante distinguir dónde estamos utilizando cada método.

| Método     | Series | DataFrame |                  Filas                  |
| ---------- | :----: | :-------: | :-------------------------------------: |
| `isnull()` |   ✅   |    ✅     |         Una fila es una Series          |
| `fillna()` |   ✅   |    ✅     |         Una fila es una Series          |
| `dropna()` |   ❌   |    ✅     |          Puede eliminar filas           |
| `apply()`  |   ✅   |    ✅     | `axis=1` permite trabajar fila por fila |

---

## Resumen

```python
# Detectar valores faltantes
df.isnull()

# Contar valores faltantes
df.isnull().sum()

# Rellenar valores faltantes
df['Edad'].fillna(15)

# Eliminar filas con valores faltantes
df.dropna()

# Eliminar filas según determinadas columnas
df.dropna(subset=['Edad'])

# Aplicar una función a una columna
df['Edad'].apply(funcion)

# Aplicar una función fila por fila
df.apply(funcion, axis=1)
```

## Idea principal

Los cuatro métodos responden a preguntas diferentes:

```text
isnull() → ¿Dónde faltan datos?

fillna() → ¿Qué pongo en los datos que faltan?

dropna() → ¿Qué datos que faltan puedo eliminar?

apply() → ¿Cómo transformo los datos usando mi propia función?
```
