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
    
df['Age'] = df.apply(rellenar_edad, axis=1)

def rellenar_genero(genero):
    if genero == 'male':
        return 1
    else:
        return 0

df['Sex'] = df['Sex'].apply(rellenar_genero)

# Creacion del modelo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

escalador = StandardScaler()

X_train = escalador.fit_transform(X_train)
X_test = escalador.transform(X_test)

clasificador = KNeighborsClassifier(n_neighbors=10)
clasificador.fit(X_train, y_train)

prediccion = clasificador.predict(X_test)

print(prediccion)

print('Matriz de confusion:')
print(confusion_matrix(y_test,  prediccion))

print('Exactitud del modelo:')
print(accuracy_score(y_test, prediccion))