#importing the Libraies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder


dataset=pd.read_csv('PP_Mtrls_and_their_Mchncl_Prprts.csv')
dataset.head()


dataset.drop('Material', axis=1, inplace=True)


columns_to_drop = ['Sy','mu']
dataset = dataset.drop(columns=columns_to_drop)
dataset.head()


dataset['Use'] = dataset['Use'].astype('object')
dataset.info()


dataset=pd.get_dummies(dataset,drop_first=True)
dataset.head()


label_encoder = LabelEncoder()

# Fit and transform the target column
dataset['Use_True'] = label_encoder.fit_transform(dataset['Use_True'])
dataset


indep=dataset[['Su','E','G','Ro']]
dep=dataset["Use_True"]




su_input=float(input("Ultimate Tensile Strength (Su) in MPa:"))
E_input=float(input("Elastic Modulus (E) in MPa:"))
g_input=float(input("Shear Modulus (G) in MPa:"))
ro_input=float(input("Density (Ro) in Kg/m3:"))




Future_Prediction=grid.predict([[su_input,E_input,g_input,ro_input]])
y=("Future_Prediction={}".format(Future_Prediction))
if (y==0):
    print("Future_Prediction=[False]")
else:
    print('Future_Prediction=[True]')
    
    
    
    
    Ultimate Tensile Strength (Su) in MPa:1000
Elastic Modulus (E) in MPa:119876
Shear Modulus (G) in MPa:67543
Density (Ro) in Kg/m3:8912
    
    
    
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder


dataset=pd.read_csv('PP_Mtrls_and_their_Mchncl_Prprts.csv')



dataset.drop('Material', axis=1, inplace=True)


columns_to_drop = ['Sy','mu']
dataset = dataset.drop(columns=columns_to_drop)



dataset['Use'] = dataset['Use'].astype('object')


dataset=pd.get_dummies(dataset,drop_first=True)

label_encoder = LabelEncoder()

# Fit and transform the target column
dataset['Use_True'] = label_encoder.fit_transform(dataset['Use_True'])
dataset

indep=dataset[['Su','E','G','Ro']]
dep=dataset["Use_True"]

#split into training set and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(indep, dep, test_size = 1/3, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

su_input=float(input("Ultimate Tensile Strength (Su) in MPa:"))
E_input=float(input("Elastic Modulus (E) in MPa:"))
g_input=float(input("Shear Modulus (G) in MPa:"))
ro_input=float(input("Density (Ro) in Kg/m3:"))

ppinput=sc.transform([[su_input,E_input,g_input,ro_input]])
ppinput

import pickle
loaded_model=pickle.load(open("finalized_model_Random_Forest.sav",'rb'))
y=loaded_model.predict(ppinput)
if (y==0):
    print("Future_Prediction=[False]")
else:
    print('Future_Prediction=[True]')