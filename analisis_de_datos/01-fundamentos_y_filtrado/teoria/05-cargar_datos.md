# Cargar Datos

Para cargar datos en pandas, primero importa la librería y luego usa la función específica según el formato de tu archivo:

```python
import pandas as pd
```

**Formatos más comunes**

* **CSV:**

```python
df = pd.read_csv('archivo.csv')
```

* **Excel (`.xlsx` o `.xls`):**

```python
df = pd.read_excel('archivo.xlsx', sheet_name='Hoja1')
```

* **JSON:**

```python
df = pd.read_json('archivo.json')
```

* **SQL (Base de datos):**

```python
df = pd.read_sql('SELECT * FROM tabla', conexion)
```

* **Diccionario de Python:**

```python
datos = {'nombre': ['Ana', 'Luis'], 'edad': [28, 34]}
df = pd.DataFrame(datos)
```
