# Dataset: Students Performance

Este dataset contiene información sobre el rendimiento académico de estudiantes en exámenes.

---

# Estructura general

Cada fila representa **un estudiante**.
Cada columna representa **una característica del estudiante o su desempeño**.

---

# Columnas del dataset

## 1. `gender`

* Tipo: categórico
* Valores posibles: `male`, `female`
* ¿Qué representa?

  * El género del estudiante

---

## 2. `race/ethnicity`

* Tipo: categórico
* Valores: `group A`, `group B`, `group C`, `group D`, `group E`
* ¿Qué representa?

  * Clasificación demográfica del estudiante
* ⚠️ Nota:

  * No indica raza literal, es una categorización anónima

---

## 3. `parental level of education`

* Tipo: categórico
* Valores posibles:

  * `some high school` => Algo de secundaria
  * `high school` => Secundaria
  * `some college` => Algo de universidad
  * `associate's degree` => Grado asociado
  * `bachelor's degree` => Licenciatura
  * `master's degree` => Maestría
* ¿Qué representa?

  * Nivel educativo más alto alcanzado por los padres
* 💡 Interpretación:

  * Sirve como indicador del contexto educativo del hogar

---

## 4. `lunch`

* Tipo: categórico
* Valores:

  * `standard`
  * `free/reduced`
* ¿Qué representa?

  * Tipo de alimentación del estudiante en la escuela
* 💡 Interpretación:

  * `free/reduced` suele indicar menor nivel socioeconómico

---

## 5. `test preparation course`

* Tipo: categórico
* Valores:

  * `none`
  * `completed`
* ¿Qué representa?

  * Si el estudiante realizó un curso de preparación
* 💡 Esta columna es clave para muchas hipótesis

---

## 6. `math score`

* Tipo: numérico
* Rango: 0 – 100
* ¿Qué representa?

  * Puntaje en matemáticas

---

## 7. `reading score`

* Tipo: numérico
* Rango: 0 – 100
* ¿Qué representa?

  * Puntaje en lectura

---

## 8. `writing score`

* Tipo: numérico
* Rango: 0 – 100
* ¿Qué representa?

  * Puntaje en escritura

---

## Características del estudiante

* gender
* race/ethnicity
* parental level of education
* lunch
* test preparation course

👉 Estas son **variables explicativas** (posibles causas)

---

## Resultados

* math score
* reading score
* writing score

👉 Estas son **variables de resultado**

---

# Ejemplo de análisis

Pregunta:

> ¿Los estudiantes que hacen el curso de preparación tienen mejores notas?

Columnas que usarías:

* `test preparation course`
* `math score`, `reading score`, `writing score`

---

# Ejemplo de hipótesis

> “Los estudiantes que completan el curso de preparación obtienen mejores resultados en los exámenes.”

---

# ⚙️ Qué puedes hacer con este dataset

✔ Filtrar estudiantes
✔ Agrupar datos
✔ Calcular promedios
✔ Comparar grupos
✔ Crear nuevas columnas (features)

---

# Ejemplo de nueva característica

```python
df['average_score'] = (df['math score'] + df['reading score'] + df['writing score']) / 3
```

👉 Esto crea una columna con el promedio de notas

---

### Ejemplo del dataset en formato tabla

| gender | race/ethnicity | parental level of education | lunch        | test preparation course | math score | reading score | writing score |
| ------ | -------------- | --------------------------- | ------------ | ----------------------- | ---------- | ------------- | ------------- |
| female | group B        | bachelor's degree           | standard     | none                    | 72         | 72            | 74            |
| female | group C        | some college                | standard     | completed               | 69         | 90            | 88            |
| male   | group A        | associate's degree          | free/reduced | none                    | 47         | 57            | 44            |

---

### 🌎 Traducción de las columnas

| Inglés                     | Español                      |
| --------------------------- | ----------------------------- |
| gender                      | género                       |
| race/ethnicity              | grupo demográfico            |
| parental level of education | nivel educativo de los padres |
| lunch                       | tipo de alimentación         |
| test preparation course     | curso de preparación         |
| math score                  | puntuación en matemáticas   |
| reading score               | puntuación en lectura        |
| writing score               | puntuación en escritura      |

---
