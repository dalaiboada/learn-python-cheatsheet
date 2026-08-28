# Selección

La selección de datos consiste en extraer subconjuntos específicos de un `DataFrame` (columnas, filas o celdas individuales) mediante etiquetas, índices numéricos o condiciones lógicas.

---

### Selección de Columnas

Hay dos formas principales de extraer columnas:

* **Como Serie:** Usar corchetes simples `df['Columna']` o notación de punto `df.Columna` (si no tiene separaciones). Devuelve un objeto unidimensional.
* 
* **Como DataFrame:** Usar corchetes dobles `df[['Columna1', 'Columna2']]`. Es obligatorio cuando se seleccionan dos o más columnas.

```python
# Extraer una sola columna como Serie
edades = df['Edad']

# Extraer varias columnas como un nuevo DataFrame
subconjunto = df[['Nombre', 'Salario']]

```