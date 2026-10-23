import pandas as pd 
 
# Paso 1. Cargar y limpiar los datos
df = pd.read_csv('titanic.csv')
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis = 1, inplace = True)
df['Embarked'] = df['Embarked'].fillna('S')
df.drop('Embarked', axis = 1, inplace = True)
 
edad_1 = df[df['Pclass'] == 1]['Age'].median()
edad_2 = df[df['Pclass'] == 2]['Age'].median()
edad_3 = df[df['Pclass'] == 3]['Age'].median()
 
def rellenar_edad(fila):
    if pd.isnull(fila['Age']):
        if fila['Pclass'] == 1:
            return edad_1
        if fila['Pclass'] == 2:
            return edad_2
        return edad_3
    return fila['Age']
 
df['Age'] = df.apply(rellenar_edad, axis = 1)
 
def rellenar_sexo(sexo):
    if sexo == 'male':
        return 1
    return 0
 
df['Sex'] = df['Sex'].apply(rellenar_sexo)
 
# Paso 2. Creando un modelo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
 
X = df.drop('Survived', axis = 1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)
 
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
 
clasificador = KNeighborsClassifier(n_neighbors = 5)
clasificador.fit(X_train, y_train)
 
y_pred = clasificador.predict(X_test)
print('Porcentaje de resultados predichos correctamente:', accuracy_score(y_test, y_pred) * 100)
print('Matriz de confusión:')
print(confusion_matrix(y_test, y_pred))