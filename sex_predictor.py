import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import pickle


filename = 'finalized_model1.sav'
loaded_model = pickle.load(open(filename, 'rb'))


dados = pd.read_csv('newsample.csv')

#dados['sex'] = dados['sex'].str.upper()
dados1 = dados.drop(['cp','index', 'slope'], axis = 1)
#dados1['sex'] = dados1['sex'].astype('str')

#le = preprocessing.LabelEncoder()
#dados1['sex'] = le.fit_transform(dados1['sex'])

dados1['age'] = dados1['age'].astype('int')

dados1 = dados1.dropna()

#y_test=dados1['sex']
#X_test = dados1.drop('sex', axis = 1)
X_test = dados1

prev = loaded_model.predict(X_test)

prediction2 = pd.DataFrame(prev, columns=['sex'])
prediction2.loc[prediction2["sex"] == 1] = 'M'
prediction2.loc[prediction2["sex"] == 0] = 'F'
#prediction2.head()
prediction2 = prediction2.to_csv('newsample_PREDICTIONS_{Alfredo_Ricardo_de_Faria_Passos}.csv', index=False)