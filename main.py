import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('titanic_min.csv')
#pobieranie wybranych kolumn
df2 = pd.read_csv('titanic_min.csv', usecols = ['PassengerId', 'Survived', 'Age', 'Sex'], index_col = 'PassengerId')

# print(df2.head())

# sortowanie
# print(df2.sort_values('Age', ascending = False).head())
#count - liczy ile jest wierszy
# print(df2['Sex'].value_counts())
# print(df2['Survived'].value_counts())

#unikalna wartosc
print(df2.nunique())

#tworzymy filtr
filtr = df['Survived']==1
survivers = df[filtr] #nakładam filtr na calosc danych
print(survivers)
filtr2 = df['Age']>=18
olders = df[filtr2]
print(olders)
#histogram na kolumnie Age
survivers.hist(column='Age')
plt.show()
survivers.hist(column='Pclass')
plt.show()