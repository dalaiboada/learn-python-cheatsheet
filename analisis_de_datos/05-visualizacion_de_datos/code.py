import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("StudentsPerformance.csv")

print('\n\nINFORMACION DE DATASET: \n')
print(df.info())

resumen_nulos = df.isnull().sum()
print('\n\nRESUMEN DE VALORES NULOS: \n')
print(resumen_nulos)

print('\nNumero de estudiantes', df.shape[0])

# Hipotesis
""" 
1. Asistir a cursos de preparación mejora resultados del examen para postulantes 
de familias donde ambos padres no tienen educación superior
"""

print('\nDistribución del nivel educativo de los padres:')
print(df['parental level of education'].value_counts())
# bachelor's degree y master's degree

df_no_uni = df[
    (df['parental level of education'] != "bachelor's degree") &
    (df['parental level of education'] != "master's degree")
]

print('Estudiantes sin educacion superior:', df_no_uni.shape[0])

# crear nueva columna promedio
df_no_uni['promedio'] = (
    df_no_uni['reading score'] + 
    df_no_uni['writing score'] + 
    df_no_uni['math score']
) / 3

df_no_uni['promedio2'] = df[['reading score', 'writing score', 'math score']].mean(axis=1)

print('\nResultados de hipotesis: \n')

agrupado = df_no_uni.groupby('test preparation course')['promedio'].mean()

print(agrupado)

# Promedio de notas según si los estudiantes hicieron el curso
agrupado.plot(
    kind='bar', 
    title='Promedio de notas según preparación para el examen', 
    ylabel='Promedio de notas', 
    xlabel='Curso de preparación'
)

df_no_uni.plot(
    kind='hist',
    title='Distribución de promedios',
    xlabel='Promedio de notas',
)

# grafico de materias
plt.figure(figsize=(15, 4))

# grafico matematicas
plt.subplot(1, 3, 1)
df['math score'].plot(
    kind='hist',
    title='Distribución de notas de matemáticas',
    xlabel='Notas de matemáticas',
)

# lectura
plt.subplot(1, 3, 2)
df['reading score'].plot(
    kind='hist',
    title='Distribución de notas de lectura',
    xlabel='Notas de lectura',
)

# escritura
plt.subplot(1, 3, 3)
df['writing score'].plot(
    kind='hist',
    title='Distribución de notas de escritura',
    xlabel='Notas de escritura',
)

plt.show()