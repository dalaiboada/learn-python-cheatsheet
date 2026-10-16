import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [150, 200, 250, 180, 300],
    'Gastos': [100, 120, 130, 110, 160]
}

df = pd.DataFrame(data)

# proporciones de cada categoría respecto a un total
#df['Ventas'].plot(kind='pie')

df.set_index('Mes')['Ventas'].plot(kind='pie')

plt.show()