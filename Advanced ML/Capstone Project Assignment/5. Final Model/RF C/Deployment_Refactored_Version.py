import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.model_selection import train_test_split

class MaterialClassifier:
    def __init__(self):
        # Load the dataset
        self.dataset = pd.read_csv('PP_Mtrls_and_their_Mchncl_Prprts.csv')

        # Drop unnecessary columns
        self.dataset.drop('Material', axis=1, inplace=True)
        columns_to_drop = ['Sy','mu']
        self.dataset = self.dataset.drop(columns=columns_to_drop)
        
        # Encode the 'Use' column
        self.dataset['Use'] = self.dataset['Use'].astype('object')
        self.dataset = pd.get_dummies(self.dataset, drop_first=True)

        # Label encode the target column
        label_encoder = LabelEncoder()
        self.dataset['Use_True'] = label_encoder.fit_transform(self.dataset['Use_True'])

        # Extract input features and target variable
        self.indep = self.dataset[['Su', 'E', 'G', 'Ro']]
        self.dep = self.dataset['Use_True']

        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.indep, self.dep, test_size=1/3, random_state=0)

        # Standardize the input data
        self.sc = StandardScaler()
        self.X_train = self.sc.fit_transform(self.X_train)
        self.X_test = self.sc.transform(self.X_test)

    def preprocess_data(self, input_data):
        # Standardize the input data
        ppinput = self.sc.transform([input_data])
        return ppinput, self.X_train, self.y_train

    def load_and_predict(self, ppinput):
        loaded_model = pickle.load(open("finalized_model_Random_Forest.sav", 'rb'))
        y = loaded_model.predict(ppinput)
        return y

    def predict(self, input_data):
        ppinput, X_train, y_train = self.preprocess_data(input_data)
        y = self.load_and_predict(ppinput)
        return y

if __name__ == "__main__":
    classifier = MaterialClassifier()
    su_input = float(input("Ultimate Tensile Strength (Su) in MPa:"))
    E_input = float(input("Elastic Modulus (E) in MPa:"))
    g_input = float(input("Shear Modulus (G) in MPa:"))
    ro_input = float(input("Density (Ro) in Kg/m3:"))

    input_data = [su_input, E_input, g_input, ro_input]
    y = classifier.predict(input_data)

    if y == 0:
        print("Future Prediction = [False]")
    else:
        print('Future Prediction = [True]')

