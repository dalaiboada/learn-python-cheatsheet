import pandas as pd
df = pd.read_csv('GoogleApps.csv')

print('\nDatos:')
print(df)

print('\nInfo:')
print(df.info())


#1 ¿Cuántas aplicaciones hay en la 'Category' 'BUSINESS'?
# * Res. 246
print('\nCantidad de aplicaciones por cateoría:')
print(df['Category'].value_counts())


#2 ¿Cuál es la relación (división) de aplicaciones para adolescentes ('Teen') 
# y las destinadas para niños mayores de 10 años ('Everyone 10+')?
# Redondee la respuesta a la centésima más cercana.
# * Res 2.73
print('\nRelación entre las aplicaciones para adolescentes y las de mayores de 10:')
temp = df['Content Rating'].value_counts()
print('Ratio:', round(temp['Teen'] / temp['Everyone 10+'], 2))


#3.1 ¿Cuál es el 'Rating' promedio de aplicaciones 'Paid'?
#Redondee la respuesta a la centésima más cercana.
# * Res 4.25

print('\nRating promedio de aplicaciones pagas(Paid)')
temp = df.groupby('Type')['Rating'].mean()
print(temp['Paid'])


#3.2 ¿Cuánto más bajo (restar) es el 'Rating' promedio de aplicaciones 'Free' 
# que el promedio de valoración de las aplicaciones 'Paid'?

#Redondee la respuesta a la centésima más cercana.

# * Res 0.08

print('\nDiferencia entre rating promedio de aplicaciones pagas y gratis:')
print(round(temp['Paid'] - temp['Free'], 2))


#4 ¿Cuál es el 'Size' (tamaño) mínimo y máximo en la 'Category' 'COMICS'?
#Redondee la respuesta a la centésima más cercana.

# * Res min: 0.43  max 40.0

print('\nSize minimo y maximo para la categoria COMICS:')
print(df.groupby('Category')['Size'].agg(['min', 'max']))


#Bonificación 1. ¿Cuántas aplicaciones tienen un 'Rating' de más de 4.5 en la 'Category' 'FINANCE'?
print('\nBonificación 1:')

temp = df[df['Rating'] > 4.5]['Category'].value_counts()
print(temp['FINANCE'])


#Bonificación 2. ¿Cuál es la relación de juegos 'Free' y 'Paid' con un 'Rating' superior a 4.9?
print('\nBonificación 2:')

temp = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(temp['Free'] / temp['Paid'])
