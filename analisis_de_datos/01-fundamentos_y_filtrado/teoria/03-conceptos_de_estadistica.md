# Conceptos de Estadística Descriptiva

## Población y Muestra

### Población
El conjunto completo de individuos, elementos o datos que se desea estudiar y sobre el cual se quieren hacer inferencias estadísticas.

### Muestra
Un subconjunto representativo que se extrae de un grupo más grande (llamado **población**) para estudiarlo y obtener conclusiones sin necesidad de analizar a cada uno de los individuos del grupo total.

* **Ejemplo:** Para conocer la estatura promedio de los **10,000 estudiantes** de una universidad (**población**), seleccionas y mides a **150 estudiantes** (**muestra**).

## Indicadores Estadísticos

**Conjunto de datos de muestra:** `[5, 6, 7, 7, 10]`

### Mínimo
El valor **más bajo** dentro del conjunto de datos.
* **Ejemplo:** En la muestra, el mínimo es **5**.

### Máximo
El valor **más alto** dentro del conjunto de datos.
* **Ejemplo:** En la muestra, el máximo es **10**.

### Moda
El valor que aparece **con mayor frecuencia**.
* **Ejemplo:** En la muestra, la moda es **7** (se repite 2 veces).

### Media (Promedio)
La suma de todos los valores dividida entre la cantidad total de datos.
* **Ejemplo:** $\frac{5 + 6 + 7 + 7 + 10}{5} = \frac{35}{5} = \mathbf{7}$.

### Mediana
El número ubicado justo en el centro cuando los datos están ordenados de menor a mayor.

* **Si es impar:** se organza y se toma el **valor del medio**.  
  En `[5, 6, 7, 7, 10]`, el valor central es **7**.
* **Si es par:** se organiza y se **promedian los dos valores centrales**.  
  En `[5, 6, 7, 8]`, la mediana sería $\frac{6 + 7}{2} = \mathbf{6.5}$.

No le afectan los valores atípicos, es una **Media robusta**.

### Desviación estándar
Mide qué tan **dispersos** o alejados están los datos **respecto a la media**. 

Una desviación baja indica que los valores están agrupados cerca del promedio, mientras que una alta señala mayor variabilidad.

> Indica si los miembros de un grupo son muy parecidos entre sí (baja desviación) o si son muy diferentes (alta desviación).

* **Ejemplo:** 
  * **Notas del estudiante A:** `[8, 8, 8, 8, 8]`
    * La **media** es $\mathbf{8}$
    * Todos iguales, la **desviación estándar** es $\mathbf{0}$.
  * **Notas del estudiante B:** `[6, 6, 7, 8, 9]`
    * La **media** es $\mathbf{7.2}$
    * La **desviación estándar** es $\mathbf{1.30384}$.

  > 💡**Conclusión:** *Estudiante A* es predecible. *Estudiante B* es más variable.

#### Coeficiente de Variación (CV)
Para determinar con precisión si es grande respecto a tus datos, se suele calcular el **Coeficiente de Variación (CV)**:

$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$

* **$CV$ (Coeficiente de Variación):** Es la medida de dispersión relativa. Se expresa en porcentaje ($\%$) y te dice qué porcentaje representa la variabilidad respecto al promedio.
* **$\sigma$ (Sigma minúscula) o $s$ (Desviación estándar):** Representa cuánto se alejan los datos de la media en las unidades originales de tu variable.
* **$\bar{x}$ ("x con barra") o $\mu$ (Mu):** Es la **media** o promedio de tus datos.

La media de Estudiante B es **$\bar{x} = 7.2$** y su desviación estándar es **$\sigma = 1.30384$**. Por lo tanto, el Coeficiente de Variación es:

$$CV = \frac{1.30384}{7.2} \times 100\% \approx 18.11\%$$

Nivel de dispersión **moderado**. La variabilidad de $1.30384$ es **aceptable** respecto a la media de $7.2$.

##### ¿Cómo interpretar el resultado?
* **$CV \le 10\% - 15\%$:** Dispersión **baja** (los datos son muy homogéneos, la varianza de $1.30384$ es **poca**).
* **$15\% < CV \le 30\%$:** Dispersión **moderada** (la media es representativa).
* **$CV > 30\%$:** Dispersión **alta** (los datos son heterogéneos, la varianza de $1.30384$ es **mucha** en relación a su promedio).