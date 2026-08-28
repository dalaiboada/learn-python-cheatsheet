## Serie

Es una estructura de datos unidimensional (1D) similar a una **columna individual**.

**Visualización de la Serie `Edad`**

| Índice | Valor        |
| ------- | ------------ |
| `0`   | **28** |
| `1`   | **34** |
| `2`   | **22** |

* **Nombre de la Serie:** `Edad`
* **Tipo de dato (`dtype`):** `int64`
* **Longitud (`length`):** `3`

**En python**

```python
import pandas as pd

serie = pd.Series([28,34,22])
```

## DataFrame

Es una **estructura bidimensional** (2D) organizada en **filas** y **columnas**, similar a una hoja de cálculo de Excel.

**Visualización de DataFrame**

Cada columna (`Nombre`, `Edad`, `Ciudad`) es una **Serie** independiente; la tabla completa es el **DataFrame**:

| Índice (Index) | Serie: Nombre | Serie: Edad | Serie: Ciudad |
| --------------- | ------------- | ----------- | ------------- |
| **0**     | Ana           | 28          | Madrid        |
| **1**     | Carlos        | 34          | Bogotá       |
| **2**     | Lucía        | 22          | Buenos Aires  |

**En python**

```python
import pandas as pd

# Definir los datos mediante un diccionario de listas
data = {
    'Nombre': ['Ana', 'Carlos', 'Lucia'],
    'Edad': [28, 34, 22],
    'Ciudad': ['Madrid', 'Bogota', 'Buenos Aires']
}

# Crear el DataFrame (el índice 0, 1, 2 se genera automáticamente)
df = pd.DataFrame(data)
```
