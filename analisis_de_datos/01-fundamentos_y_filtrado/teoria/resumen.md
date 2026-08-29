# Fundamentos y Ciclo del Análisis de Datos

> **Definición:** Proceso de inspeccionar, limpiar y modelar datos para extraer información útil, comprender el pasado y respaldar la toma de decisiones estratégicas en el presente y futuro.

---

### Visión General

* **Objetivo principal:** Transformar datos brutos en respuestas e informes claros para la toma de decisiones.
* **Flujo clave:** Obtener datos $\rightarrow$ Explorar $\rightarrow$ Plantear preguntas $\rightarrow$ Encontrar respuestas.
* **Entregables:** Informes ejecutivos y visualizaciones de impacto.
* **Stack común:** Excel, SQL, Tableau, Power BI, Python (Pandas).
* **Caso práctico (ej. Netflix):** Identificar qué series ve la audiencia, actores preferidos y géneros más rentables.

---

### Pipeline de un Proyecto de Datos

| Fase                         | Etapa                                  | Acciones Clave                                                                                                                                    |
| ---------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0. Estructuración** | **Estructurar datos**            | Definir la arquitectura y formato base de los datos.                                                                                              |
| **1. Planteamiento**   | **Definir el problema**          | Delimitar objetivos del negocio, necesidades de información e hipótesis de trabajo.                                                             |
| **2. Ingesta**         | **Cargar datos**                 | Importar fuentes estructuradas y semiestructuradas (`CSV`, `XLSX`, `SQL`, `JSON`, etc.).                                                  |
| **3. Exploración**    | **Explorar datos (EDA)**         | Inspeccionar dimensiones, patrones iniciales y distribución de variables.                                                                        |
| **4. Preparación**    | **Limpiar y transformar**        | 1. • Tratamiento de valores nulos y duplicados. 2. • Conversión y casteo de tipos de datos.  3. • Filtrado y selección de variables clave. |
| **5. Procesamiento**   | **Agrupar datos** *(Opcional)* | Segmentar por categorías para resúmenes estadísticos o agregaciones.                                                                           |
| **6. Visualización**  | **Visualizar datos**             | Crear gráficos y dashboards para revelar tendencias y patrones visuales.                                                                         |
| **7. Analítica**      | **Modelar y predecir**           | Aplicar modelos analíticos o predictivos sobre la data procesada.                                                                                |
| **8. Entrega**         | **Comunicar resultados**         | Presentar conclusiones y recomendaciones a los interesados.                                                                                       |

### Conceptos Clave de Estadística

| Concepto                                 | Definición Clave                                                                  | Fórmula / Cálculo                                                | Ejemplo del Texto                                                                                                   |
| ---------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Población**                     | Conjunto completo de individuos o datos a estudiar para inferencias estadísticas. | —                                                                 | 10,000 estudiantes de una universidad                                                                               |
| **Muestra**                        | Subconjunto representativo extraído de la población para obtener conclusiones.   | —                                                                 | 150 estudiantes seleccionados                                                                                       |
| **Mínimo**                        | El valor más bajo dentro del conjunto de datos.                                   | $\min(X)$                                                        | En `[5, 6, 7, 7, 10]`, el mínimo es **5**                                                                  |
| **Máximo**                        | El valor más alto dentro del conjunto de datos.                                   | $\max(X)$                                                        | En `[5, 6, 7, 7, 10]`, el máximo es **10**                                                                 |
| **Moda**                           | El valor que aparece con mayor frecuencia en la muestra.                           | Frecuencia más alta                                               | En `[5, 6, 7, 7, 10]`, la moda es **7** (repite 2 veces)                                                    |
| **Media (Promedio)**               | Suma de todos los valores dividida entre el total de datos.                        | $\bar{x} = \frac{\sum x_i}{n}$                                   | $\frac{5+6+7+7+10}{5} = \frac{35}{5} = \mathbf{7}$                                                                |
| **Mediana**                        | Valor central ordenado de menor a mayor.                                           | • Impar: dato central • Par: promedio de los dos datos centrales | Impar `[5,6,7,7,10]` $\rightarrow \mathbf{7}$ • Par `[5,6,7,8]` $\rightarrow \frac{6+7}{2} = \mathbf{6.5}$ |
| **Desviación Estándar**          | Medida de dispersión/alejamiento de los datos respecto a la media.                | $\sigma \text{ o } s$                                            | • Estudiante A `[8,8,8,8,8]`: $\bar{x}=8$, $\sigma = \mathbf{0}$                                             |
| **Coeficiente de Variación (CV)** | Medida de dispersión relativa expresada en porcentaje respecto a la media.        | $CV = \frac{\sigma}{\bar{x}} \times 100\%$                       | $CV = \frac{1.30384}{7.2} \times 100\% \approx \mathbf{18.11\%}$ (Dispersión moderada)                           |
