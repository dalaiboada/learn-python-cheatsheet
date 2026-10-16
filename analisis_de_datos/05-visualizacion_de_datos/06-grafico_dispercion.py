import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [150, 200, 250, 180, 300],
    'Gastos': [100, 120, 130, 110, 160]
}
df = pd.DataFrame(data)

df.plot(kind='scatter', x='Gastos', y='Ventas')

print(df[['Ventas', 'Gastos']].corr())

plt.show()