# Creación y modificación de columnas

La regla general es usar siempre: $$\text{df}[\text{'Nombre\_Columna'}] = \text{valores}$$ 

Si el nombre no existe, se crea; si ya existe, se modifica.

---

**1. Crear una columna desde cero (valor fijo)**
Asigna un valor único y se repetirá en todas las filas.

```python
# Crea la columna 'Pais' con el mismo valor para todos
df['Pais'] = 'Venezuela'

```

---

**2. Modificar una columna existente**
Asigna el nuevo valor usando el nombre de la columna que ya tienes.

```python
# Aumenta en 500 el salario existente
df['Salario'] = df['Salario'] + 500

# Convierte los nombres a mayúsculas
df['Nombre'] = df['Nombre'].str.upper()

```

---

**3. Crear una columna basada en otras**
Aplica operaciones matemáticas o de texto usando las columnas existentes.

```python
# Operación matemática: 10% del salario
df['Bono'] = df['Salario'] * 0.10

# Operación entre dos columnas: Salario + Bono
df['Total'] = df['Salario'] + df['Bono']

# Concatenar texto entre columnas
df['Nombre_Depto'] = df['Nombre'] + " - " + df['Departamento']

```