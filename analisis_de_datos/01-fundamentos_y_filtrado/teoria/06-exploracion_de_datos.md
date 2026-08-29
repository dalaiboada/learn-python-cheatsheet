# Métodos de Exploración Rápida

| Concepto                         | Sintaxis          | Tipo     | Salida / Propósito                                   |
| -------------------------------- | ----------------- | -------- | ----------------------------------------------------- |
| **Primeras filas**         | `df.head(n)`    | Método  | Primeras ($n$) filas                                |
| **Últimas filas**         | `df.tail(n)`    | Método  | Últimas ($n$)  filas                               |
| **Estructura general**     | `df.info()`     | Método  | Tipos, no-nulos y memoria                             |
| **Estadísticas básicas** | `df.describe()` | Método  | Media, mín, máx, percentiles, desviación estandar. |
| **Tipos de datos**         | `df.dtypes`     | Atributo | Tipo por columna (`int`, `object`, etc.)          |
| **Dimensiones**            | `df.shape`      | Atributo | Tupla que indica el número de `(filas, columnas)` |
| **Lista de columnas**      | `df.columns`    | Atributo | Nombres de los encabezados                            |
