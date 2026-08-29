# Filtrado de Datos

Permite seleccionar filas que cumplan con criterios lógicos específicos.

### 1. Condición simple

Evalúa una columna para generar una serie de booleanos (`True`/`False`).

$$
\text{df}[\text{condición}]
$$

**Ejemplo**: Personas (Filas) mayores de edad.
Seleccionar solo las filas que tengan en edad (columna) más de 18 `df['Edad'] > 18`

```python
df_mayores = df[df['Edad'] > 18]
```

---

### 2. Múltiples condiciones:

**Operadores lógicos para múltiples condiciones:**

* `&` para **AND** (ambas deben cumplirse).
* `|` para **OR** (al menos una debe cumplirse).
* `~` para **NOT** (negación).
* *Regla obligatoria:* Cada condición individual debe envolverse entre paréntesis `()`.

$$
\text{df}[(\text{condición}_1) \mid (\text{condición}_2)]
$$

$$
\text{df}[(\text{condición}_1) \ \& \ (\text{condición}_2)]
$$

```python
# Filtrar empleados del departamento 'TI' AND con edad menor a 32
ti_jovenes = df[(df['Departamento'] == 'TI') & (df['Edad'] < 32)]

# Filtrar empleados de 'Ventas' OR de 'Marketing'
ventas_o_marketing = df[(df['Departamento'] == 'Ventas') | (df['Departamento'] == 'Marketing')]
```

---

### Resumen de Sintaxis

| Operación                                | Sintaxis                                            |
| ----------------------------------------- | --------------------------------------------------- |
| **Una columna (Serie)**             | `df['Nombre']`                                    |
| **Múltiples columnas (DataFrame)** | `df[['Nombre', 'Edad']]`                          |
| **Filtro simple**                   | `df[df['Edad'] >= 30]`                            |
| **Filtro múltiple**                | `df[(df['Edad'] >= 30) & (df['Salario'] > 3500)]` |
