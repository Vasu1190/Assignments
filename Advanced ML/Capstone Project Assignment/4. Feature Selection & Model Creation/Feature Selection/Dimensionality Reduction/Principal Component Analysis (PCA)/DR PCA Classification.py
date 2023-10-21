import pandas as pd
from sklearn.model_selection import train_test_split 
import time
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import chi2
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib.pyplot as plt


def pca(indep_X, n_components):
    pca = PCA(n_components=n_components)
    indep_X_pca = pca.fit_transform(indep_X)
    return indep_X_pca
    
def split_scalar(indep_X,dep_Y):
        X_train, X_test, y_train, y_test = train_test_split(indep_X, dep_Y, test_size = 0.25, random_state = 0)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)    
        return X_train, X_test, y_train, y_test
    
 
def cm_prediction(classifier,X_test):
     y_pred = classifier.predict(X_test)
        
        # Making the Confusion Matrix
     from sklearn.metrics import confusion_matrix
     cm = confusion_matrix(y_test, y_pred)
        
     from sklearn.metrics import accuracy_score 
     from sklearn.metrics import classification_report 
        #from sklearn.metrics import confusion_matrix
        #cm = confusion_matrix(y_test, y_pred)
        
     Accuracy=accuracy_score(y_test, y_pred )
        
     report=classification_report(y_test, y_pred)
     return  classifier,Accuracy,report,X_test,y_test,cm

def logistic(X_train,y_train,X_test):       
        # Fitting K-NN to the Training set
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm      
    
def svm_linear(X_train,y_train,X_test):
                
        from sklearn.svm import SVC
        classifier = SVC(kernel = 'linear', random_state = 0)
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm
    
def svm_NL(X_train,y_train,X_test):
                
        from sklearn.svm import SVC
        classifier = SVC(kernel = 'rbf', random_state = 0)
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm
   
def Navie(X_train,y_train,X_test):       
        # Fitting K-NN to the Training set
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB()
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm         
    
    
def knn(X_train,y_train,X_test):
           
        # Fitting K-NN to the Training set
        from sklearn.neighbors import KNeighborsClassifier
        classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm
def Decision(X_train,y_train,X_test):
        
        # Fitting K-NN to the Training set
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm      


def random(X_train,y_train,X_test):
        
        # Fitting K-NN to the Training set
        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
        classifier.fit(X_train, y_train)
        classifier,Accuracy,report,X_test,y_test,cm=cm_prediction(classifier,X_test)
        return  classifier,Accuracy,report,X_test,y_test,cm
    
def PCA_Classification(acclog,accsvml,accsvmnl,accknn,accnav,accdes,accrf): 
    
    kpcadataframe=pd.DataFrame(index=['PCA'],columns=['Logistic','SVMl','SVMnl',
                                                                                        'KNN','Navie','Decision','Random'])

    for number,idex in enumerate(kpcadataframe.index):
        
        kpcadataframe['Logistic'][idex]=acclog[number]       
        kpcadataframe['SVMl'][idex]=accsvml[number]
        kpcadataframe['SVMnl'][idex]=accsvmnl[number]
        kpcadataframe['KNN'][idex]=accknn[number]
        kpcadataframe['Navie'][idex]=accnav[number]
        kpcadataframe['Decision'][idex]=accdes[number]
        kpcadataframe['Random'][idex]=accrf[number]
    return kpcadataframe
    
    
dataset1=pd.read_csv("Social_Network_Ads.csv",index_col=None)
dataset1=pd.read_csv("prep.csv",index_col=None)

df2=dataset1

df2 = pd.get_dummies(df2, drop_first=True)

indep_X=df2.drop('classification_yes', axis=1)
dep_Y=df2['classification_yes']
df2

kernels = ['linear', 'poly', 'rbf', 'sigmoid']  
n_components = 10
kernel_results = {}  

for kernel in kernels:
    indep_X_pca = pca(indep_X, n_components)
    
    # Check if the length of indep_X_pca matches your original dataset
    if len(indep_X_pca) != len(dep_Y):
        print(f"Length mismatch for {kernel} kernel. Skipping.")
        continue

    acclog = []
    accsvml = []
    accsvmnl = []
    accknn = []
    accnav = []
    accdes = []
    accrf = []

    X_train, X_test, y_train, y_test = split_scalar(indep_X_pca, dep_Y)

    classifier, Accuracy, report, X_test, y_test, cm = logistic(X_train, y_train, X_test)
    acclog.append(Accuracy)

    classifier, Accuracy, report, X_test, y_test, cm = svm_linear(X_train, y_train, X_test)
    accsvml.append(Accuracy)

    classifier, Accuracy, report, X_test, y_test, cm = svm_NL(X_train, y_train, X_test)
    accsvmnl.append(Accuracy)

    classifier, Accuracy, report, X_test, y_test, cm = knn(X_train, y_train, X_test)
    accknn.append(Accuracy)

    classifier, Accuracy, report, X_test, y_test, cm = Navie(X_train, y_train, X_test)
    accnav.append(Accuracy)

    classifier, Accuracy, report, X_test, y_test, cm = Decision(X_train, y_train, X_test)
    accdes.append(Accuracy)

    classifier, Accuracy, report, X_test, y_test, cm = random(X_train, y_train, X_test)
    accrf.append(Accuracy)

    result = PCA_Classification(acclog, accsvml, accsvmnl, accknn, accnav, accdes, accrf)

    result
    
    #kernel_results[kernel] = result

# Access the results for each kernel from kernel_results dictionary
#print(kernel_results)
