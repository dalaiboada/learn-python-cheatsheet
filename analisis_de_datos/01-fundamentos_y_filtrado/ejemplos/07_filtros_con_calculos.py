import pandas as pd

datos = {
    'Nombre': 
        ['Ana', 'Carlos', 'Lucia', 'Mateo', 'Elena'],
    'Departamento': 
        ['Ventas', 'TI', 'TI', 'Ventas', 'Marketing'],
    'Edad': 
        [28, 35, 30, 28, 42],
    'Salario': 
        [3200, 4100, 3800, 2900, 4800]
}

df = pd.DataFrame(datos)

""" 
--- FILTROS CON CALCULOS

    Filtrar y luego calcular(aplicar operación)

    1. Seleccionar la columna por la que se va a filtrar
    2. Seleccionar la columna a la que se le va a aplicar la operación 
        (sum, count, min, mean, max, etc)
        
    Formula: df[(condicion de filtro)]['columna_operacion'].operacion()
"""
print(df)

# eg. ¿Cuál es la edad promedio de los emplados de TI?
print(df[df['Departamento'] == 'TI']['Edad'].mean())

# eg. Salario promedio de los empleados de Ventas
print(df[df['Departamento'] == 'Ventas']['Salario'].mean())