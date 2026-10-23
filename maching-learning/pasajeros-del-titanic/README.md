# PASAJEROS DEL TITANIC

El conjunto de datos corresponde a los registros de los pasajeros del **RMS Titanic** (específicamente la muestra clásica de 891 registros que abarca desde el `PassengerId` 1 hasta el 891).

---

### 1. Estructura y Variables

El dataset cuenta con **891 filas** y **12 columnas**:

| Variable | Tipo de dato | Descripción | Valores representativos / Ejemplos |
| --- | --- | --- | --- |
| `PassengerId` | Entero (ID) | Identificador secuencial del pasajero | 1 a 891 |
| `Survived` | Binaria / Categórica | Supervivencia del pasajero | `0` = No sobrevivió, `1` = Sobrevivió |
| `Pclass` | Numérica ordinal | Clase del billete | `1` = Primera, `2` = Segunda, `3` = Tercera |
| `Name` | Texto (String) | Nombre, títulos y apellidos del pasajero | `"Braund, Mr. Owen Harris"` |
| `Sex` | Categórica nominal | Género del pasajero | `male`, `female` |
| `Age` | Numérica continua | Edad en años (con decimales para lactantes) | Rango: 0.42 a 80 años |
| `SibSp` | Numérica discreta | Número de hermanos / cónyuges a bordo | 0 a 8 |
| `Parch` | Numérica discreta | Número de padres / hijos a bordo | 0 a 6 |
| `Ticket` | Alfanumérica / Texto | Número identificador del boleto | `"A/5 21171"`, `"PC 17599"` |
| `Fare` | Numérica continua | Tarifa abonada por el pasaje | Rango: £0.0 a £512.33 |
| `Cabin` | Alfanumérica | Código de cabina asignada | `"C85"`, `"E46"`, `None` |
| `Embarked` | Categórica nominal | Puerto donde embarcó el pasajero | `C` (Cherburgo), `Q` (Queenstown), `S` (Southampton) |

---

### 2. Estadísticas Clave del Muestreo

* **Supervivencia global (`Survived`):**
* Tasa de supervivencia aproximada del **38.4%** (alrededor de 342 pasajeros sobrevivieron y 549 fallecieron).


* **Distribución de Género (`Sex`):**
* La tripulación de pasajeros estuvo mayoritariamente compuesta por hombres: ~**64.8% masculinos** (577) frente a ~**35.2% femeninos** (314).
* La probabilidad de supervivencia fue marcadamente mayor en mujeres (*regla de evacuación "mujeres y niños primero"*).


* **Distribución por Clase (`Pclass`):**
* **3ª Clase:** Representa la gran mayoría (~55%), con las tarifas más bajas y las menores tasas de supervivencia.
* **1ª y 2ª Clase:** Representan aproximadamente el 24% y 21% respectivamente, con mayor acceso prioritario a botes salvavidas.


* **Edad (`Age`):**
* La media de edad ronda los **29.7 años**, con una presencia notable de adultos jóvenes entre 20 y 38 años.
* Los pasajeros más jóvenes registrados son infantes menores de 1 año (ej. Thomas, Assad Alexander con 0.42 años), y el más longevo tiene 80 años (Barkworth, Mr. Algernon Henry Wilson).


* **Tarifas (`Fare`):**
* La mediana es baja (~£14.45), pero con valores atípicos muy altos que superan las £200 y £500 (ej. billetes de 1ª clase como el de Miss Anna Ward a £512.33).



---

### 3. Calidad de Datos y Valores Faltantes (Nulos)

* **`Cabin`:** Es la variable con mayor cantidad de valores ausentes (más del **77%** de los datos están vacíos), principalmente concentrada en pasajeros de 2ª y 3ª clase.
* **`Age`:** Presenta aproximadamente **177 valores nulos** (~20%), donde no se registró la edad oficial del pasajero.
* **`Embarked`:** Presenta 2 valores faltantes en este lote (ej. pasajeros 62 y 830: *Miss Amelie Icard* y *Mrs George Nelson Stone*).