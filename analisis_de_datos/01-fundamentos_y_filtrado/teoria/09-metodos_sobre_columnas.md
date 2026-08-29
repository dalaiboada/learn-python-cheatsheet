| Método                 | Definición                                                              | Ejemplo                     | Tipo de salida                          |
| ----------------------- | ------------------------------------------------------------------------ | --------------------------- | --------------------------------------- |
| **`.min()`**    | Obtiene el**valor más bajo** de la columna.                       | `df['Edad'].min()`        | Escalar (`int` / `float` / `str`) |
| **`.max()`**    | Obtiene el**valor más alto** de la columna.                       | `df['Edad'].max()`        | Escalar (`int` / `float` / `str`) |
| **`.mean()`**   | Calcula el**promedio** aritmético de los valores numéricos.      | `df['Edad'].mean()`       | `float`                               |
| **`.count()`**  | Cuenta la cantidad de**registros no nulos** presentes.             | `df['Edad'].count()`      | `int`                                 |
| **`.sum()`**    | Suma la**totalidad de los valores numéricos** de la columna.      | `df['Salario'].sum()`     | Escalar (`int` / `float`)           |
| **`.std()`**    | Mide el**nivel de dispersión** de los datos respecto a la media.  | `df['Edad'].std()`        | `float`                               |
| **`.median()`** | Obtiene el la **mediana**.                                              | `df['Edad'].median()`     | `float`                               |
| **`.mode()`**   | Devuelve el valor o **valores que más veces se repiten**.              | `df['Edad'].mode()`       | `Series`                              |
| **`.var()`**    | Calcula la **varianza** estadística de los datos.                      | `df['Edad'].var()`        | `float`                               |
| **`.apply()`**  | **Aplica una función** elemento por elemento a lo largo de la columna. | `df['Nombre'].apply(len)` | `Series`                              |
