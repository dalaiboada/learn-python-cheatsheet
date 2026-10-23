import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [150, 200, 250, 180, 300],
    'Gastos': [100, 120, 130, 110, 160]
}
df = pd.DataFrame(data)

df.plot(
    kind='bar', 
    x='Mes', 
    y='Ventas', 
    figsize=(12, 5),          # Cambiar tamaño
    grid=True,               # Agregar cuadrícula
    color='orange',          # Cambiar color
    title='Ventas por Mes'   # Agregar título
)
plt.savefig('grafico.png', dpi=300)

plt.show()