from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import pandas as pd
import pathlib

# Lee el archivo CSV
df = pd.read_csv(pathlib.Path('data/traffic.csv'))
df=df.rename(columns={'Traffic Situation':'TrafficSituation'})
df=df.drop(["Time","Day of the week","Total"],axis=1)
df["TrafficSituation"]=df["TrafficSituation"].map({'low':1,'normal':2,'heavy':3,'high':4})
#df=df['Time'] = pd.to_datetime(df['Time']).dt.hour * 60 + pd.to_datetime(df['Time']).dt.minute
#df['Time'] = df['Time'] / 60.0

# Define las columnas que serán características (X) y la columna objetivo (y)
y = df.pop('TrafficSituation')
X = df


# Divide los datos en conjuntos de entrenamiento y prueba
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
X,y  = df.iloc[:,:-1],df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state = 1, test_size = 0.2)

print('Training model...')
#clf = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=0)
#clf.fit(X_train, y_train)
model1 = RandomForestClassifier(n_estimators=10, max_depth=2, random_state=0)
model1.fit(X_train,y_train)

print('Saving model...')
dump(model1, pathlib.Path('model/traffic-v1.joblib'))
