import pandas as pd
df = pd.read_csv ('GoogleApps.csv')

# ¿Cuál es el precio (Price) de la aplicación de pago más barata (Type == 'Paid')?
# * Res: 0.99
print(df[df['Type'] == 'Paid']['Price'].min())


# Cuál es la mediana (median) del número de instalaciones (Installs)
# de aplicaciones de la categoría "ART_AND_DESIGN" (Category)?
# * Res: 100000.0
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())

# ¿Por cuánto el número máximo de reseñas para las aplicaciones gratuitas (Type == 'Free')
# rebasa el número máximo de reseñas para las aplicaciones de pago (Type == 'Paid')?
# * Res: 44703802

free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()
print(free - paid)

# ¿Cuál es el tamaño mínimo (Size) de una aplicación para adolescentes (Content Rating == 'Teen')?
# * Res: 0.315
print(df[df['Content Rating'] == 'Teen']['Size'].min())


# (Extra) ¿Cuál es la categoría (Category) de una aplicación con el mayor número de reseñas (Reviews)?
# * Res: GAME
print(df[df['Reviews'] == df['Reviews'].max()]['Category'])


# (Extra) ¿Cuál es la valoración (Rating) media (mean) de las aplicaciones con un precio (Price) superior a $ 20 y 
# con el número de instalaciones (Installs) más de 10.000?
# * Res: 4.25
print(df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean())
