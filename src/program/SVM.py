''' LO QUE PASA ES QUE AL COGER LOS VALORES DE LOS AUDIOS DEL DATA.CSV, EL STROKE SE GUARDA EN EL NOMBRE DE LA CARPETA CON EL NUMBERO Y NO CON EL
NOMBRE DE LA CLASE QUE QUEREMOS, ENTONCES LOS PLOTS NO LOS HACE BIEN.'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


data_file = '/home/naiaragarmendia/Documents/GitHub/AHSC/src/program/data.csv'

#Read data with pandas module
data = pd.read_csv(data_file)

#Plot first lines of our data
print(data.head())


#sns.relplot(x = "melbands_flatness_db.mean", y = "spectral_centroid.mean", hue = "stroke", data = data);
#plt.show()

data_modif = data.copy()

#Let's use sklearn's preprocessing tools for applying normalisation to features
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler() # el minmaxScales los scala y los normaliza
data_modif.iloc[:,:84] = min_max_scaler.fit_transform(data.iloc[:,:84].values)


# Checking if our data is balanced (if not, we should balance it to prevent our model to be baised)
print(data_modif.stroke.value_counts())


################################################################################################################

# categorizamos las 10 categorias en un valor numeral y las codificamos.
# Input values put in a matrix, there are 84 features
X = data_modif.iloc[:,:84].values
# Creating output values
data_modif.stroke = pd.Categorical(data_modif.stroke)  # convert to categorical data
y = np.array(data_modif.stroke.cat.codes)  # create label encoded outputs
# Print the first sample
print("Features of the first sample: ", X[0])
print("Class of the first sample: ", y[0])
print(len(X),len(y))

############################################################################################################3


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42) #posible error de calculo, no entendemos para que sirve el random_state

# Check sizes of input and output vectors
print("Size of train features matrix: ",X_train.shape, ", Size of train output vector: ",y_train.shape)
print("Size of test features matrix: ",X_test.shape, ", Size of test output vector: ",y_test.shape)


#################################################################################################################

from sklearn import svm
clf = svm.SVC(gamma = 1 / (X_train.shape[-1] * X_train.var()))
print(clf)

# Fit model with training data
clf.fit(X_train, y_train) # entrena el clasificador


# Predict classes of test samples
y_pred = clf.predict(X_test)

print(y_test == y_pred)

##################################################################################################################


# Data is balanced, so you can use accuracy as a measure:
print("accuracy: ", np.sum(y_test == y_pred)/len(y_test))


# Print the confusion matrix
#el plot de la matriz no funciona porq las size del plot no coincidem

classes = np.unique(data_modif.stroke)
conf_mat = pd.DataFrame(confusion_matrix(y_test, y_pred), columns = classes, index = classes)
conf_mat.index.name = 'Actual'
conf_mat.columns.name = 'Predicted'
plt.figure(figsize = (7, 5))
sns.set(font_scale = 1.2)
sns.heatmap(conf_mat, cmap = "Blues", annot_kws = {"size": 12}, annot = True);