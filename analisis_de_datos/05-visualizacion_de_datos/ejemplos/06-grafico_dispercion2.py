import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Horas extras': [340, 95, 210, 809, 80, 438, 107, 180, 100, 550, 220, 50, 193, 290, 340, 115, 362, 300, 75, 93, 320, 154],
    'Porcentaje de defectuosos': [5, 3, 6, 15, 4, 10, 4, 6, 3, 13, 7, 3, 6, 8, 2, 4, 10, 9, 2, 2, 10, 7]
}

df = pd.DataFrame(data)

print(df)

df.plot(kind='scatter', x='Horas extras', y='Porcentaje de defectuosos')
print(df[['Horas extras', 'Porcentaje de defectuosos']].corr())


# r = 0.86 positiva fuerte
plt.show()