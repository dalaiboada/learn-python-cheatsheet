import pandas as pd 

# 1. Cargar y limpiar datos
df = pd.read_csv("titanic.csv")
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df['Embarked'] = df['Embarked'].fillna('S')
df.drop('Embarked', axis = 1, inplace = True)

# Sacar el promedio de la edad por el tipo de clase
edad_1 = df[df['Pclass'] == 1]['Age'].median()
edad_2 = df[df['Pclass'] == 2]['Age'].median()
edad_3 = df[df['Pclass'] == 3]['Age'].median()

def rellenar_edad(fila):
    if pd.isnull(fila['Age']):
        if fila['Pclass'] == 1:
            return edad_1
        elif fila['Pclass'] == 2:
            return edad_2
        else:
            return edad_3
    else:
        return fila['Age']
    
df['Age'] = df['Age'].apply(rellenar_edad)

def rellenar_genero(genero):
    if genero == 'male':
        return 1
    else:
        return 0

df['Sex'] = df['Sex'].apply(rellenar_genero)