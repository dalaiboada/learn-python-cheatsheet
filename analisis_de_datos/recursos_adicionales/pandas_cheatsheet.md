# Pandas (CheatSheet)

## 1. Creación de DataFrames y Series

| Código                                                                           | Descripción                                          |
| --------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `pd.DataFrame({"a": [4, 5, 6], "b": [7, 8, 9]}, index=[1, 2, 3])`               | Crear un DataFrame especificando valores por columna. |
| `pd.DataFrame([[4, 7, 10], [5, 8, 11]], index=[1, 2], columns=['a', 'b', 'c'])` | Crear un DataFrame especificando valores por fila.    |
| `pd.Series([1, 3, 5, np.nan, 6, 8])`                                            | Crear una Serie (columna unidimensional).             |
| `pd.MultiIndex.from_tuples([('d', 1), ('d', 2)], names=['n', 'v'])`             | Crear un índice multinivel (MultiIndex).             |

---

## 2. Remodelación de Datos (Reshaping)

| Código                                                 | Descripción                                         |
| ------------------------------------------------------- | ---------------------------------------------------- |
| `pd.melt(df)`                                         | Convierte columnas en filas (aplana el DataFrame).   |
| `df.pivot(columns='var', values='val')`               | Convierte filas en columnas (tabla dinámica).       |
| `pd.concat([df1, df2], axis=0)`                       | Concatena DataFrames por filas (verticalmente).      |
| `pd.concat([df1, df2], axis=1)`                       | Concatena DataFrames por columnas (horizontalmente). |
| `df.sort_values('columna')`                           | Ordena las filas por los valores de una columna.     |
| `df.sort_values('columna', ascending=False)`          | Ordena de forma descendente.                         |
| `df.rename(columns={'viejo_nombre': 'nuevo_nombre'})` | Renombra las columnas.                               |
| `df.sort_index()`                                     | Ordena el DataFrame por su índice.                  |
| `df.reset_index()`                                    | Restablece el índice a enteros numéricos.          |
| `df.drop(columns=['col1', 'col2'])`                   | Elimina las columnas especificadas.                  |

---

## 3. Manejo de Datos Faltantes (Missing Data)

| Código            | Descripción                                                      |
| ------------------ | ----------------------------------------------------------------- |
| `df.dropna()`    | Elimina las filas que contienen valores nulos (`NaN`).          |
| `df.fillna(val)` | Reemplaza todos los valores nulos (`NaN`) con el valor `val`. |

---

## 4. Selección de Subconjuntos (Filtrado)

**Filtrar Filas (Observaciones):**

* `df[df['Length'] > 7]` — Selecciona filas donde el valor sea mayor a 7.
* `df.drop_duplicates()` — Elimina filas duplicadas.
* `df.head(n)` — Devuelve las primeras $n$ filas.
* `df.tail(n)` — Devuelve las últimas $n$ filas.
* `df.sample(frac=0.5)` — Selecciona una fracción aleatoria del DataFrame.
* `df.sample(n=10)` — Selecciona $n$ filas aleatorias.
* `df.iloc[10:20]` — Selecciona filas por posición numérica.
* `df.nlargest(n, 'columna')` — Selecciona las $n$ filas con mayores valores.
* `df.nsmallest(n, 'columna')` — Selecciona las $n$ filas con menores valores.

**Filtrar Columnas (Variables):**

* `df[['width', 'length', 'species']]` — Selecciona múltiples columnas específicas.
* `df['width']` o `df.width` — Selecciona una sola columna como Serie.
* `df.filter(regex='regex')` — Selecciona columnas que coincidan con una expresión regular.
* `df.loc[:, 'x2':'x4']` — Selecciona rango de columnas por nombre.
* `df.iloc[:, [0, 2]]` — Selecciona columnas por su posición numérica.

---

## 5. Creación de Nuevas Columnas

| Código                                                | Descripción                                           |
| ------------------------------------------------------ | ------------------------------------------------------ |
| `df.assign(Area = lambda df: df.Length * df.Height)` | Calcula y añade una o más columnas nuevas.           |
| `df['Volume'] = df.Length * df.Height * df.Depth`    | Añade una columna de forma directa.                   |
| `pd.qcut(df['col'], n, labels=False)`                | Divide una columna en$n$ cuantiles de igual tamaño. |
| `pd.cut(df['col'], bins)`                            | Divide una columna en rangos numéricos especificados. |

---

## 6. Resumen y Estadísticas (Summarizing Data)

* `df['columna'].value_counts()` — Cuenta la frecuencia de cada valor único.
* `len(df)` — Retorna el número de filas del DataFrame.
* `df.shape` — Retorna una tupla con la dimensión `(filas, columnas)`.
* `df['columna'].nunique()` — Número de valores únicos en la columna.
* `df.describe()` — Calcula estadísticas descriptivas básicas de todas las columnas.

**Funciones de Agregación Comunes:**

* `df.sum()` — Suma de valores.
* `df.count()` — Conteo de valores no nulos.
* `df.median()` — Mediana.
* `df.quantile([0.25, 0.75])` — Cuantiles especificados.
* `df.min()` / `df.max()` — Valor mínimo / máximo.
* `df.mean()` — Promedio o media aritmética.
* `df.var()` / `df.std()` — Varianza y desviación estándar.

---

## 7. Agrupamiento de Datos (Group By)

| Código                                       | Descripción                                     |
| --------------------------------------------- | ------------------------------------------------ |
| `df.groupby(by='columna')`                  | Agrupa los datos por los valores de una columna. |
| `df.groupby('columna').aggregate('mean')`   | Aplica una función de agregación a cada grupo. |
| `df.groupby('columna').size()`              | Retorna el tamaño de cada grupo.                |
| `df.groupby('columna').transform(función)` | Transforma datos manteniendo la forma original.  |

---

## 8. Combinación de Datasets (Joins / Merges)

| Tipo de Join         | Código Pandas                                  |
| -------------------- | ----------------------------------------------- |
| **Left Join**  | `pd.merge(df1, df2, how='left', on='llave')`  |
| **Right Join** | `pd.merge(df1, df2, how='right', on='llave')` |
| **Inner Join** | `pd.merge(df1, df2, how='inner', on='llave')` |
| **Outer Join** | `pd.merge(df1, df2, how='outer', on='llave')` |

---

## 9. Visualización (Plotting)

| Código                           | Tipo de Gráfico             |
| --------------------------------- | ---------------------------- |
| `df.plot.hist()`                | Histograma de distribución. |
| `df.plot.scatter(x='x', y='y')` | Gráfico de dispersión.     |
| `df.plot.bar()`                 | Gráfico de barras.          |
| `df.plot.line()`                | Gráfico de líneas.         |
| `df.plot.box()`                 | Diagrama de caja (Boxplot).  |
