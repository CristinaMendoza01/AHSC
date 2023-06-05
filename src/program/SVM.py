import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
import csv

def SVM_classifier(best):
    data_file = 'FullData.csv'

    # Leer el archivo CSV
    data = pd.read_csv(data_file)

    # Plot first lines of our data
    print(data.head())

    sns.relplot(x="melbands_flatness_db.mean", y="spectral_centroid.mean", hue="clase", data=data)
    plt.show()

    data_modif = data.copy()

    # Let's use sklearn's preprocessing tools for applying normalisation to features
    from sklearn import preprocessing
    min_max_scaler = preprocessing.MinMaxScaler()
    data_modif.iloc[:, :96] = min_max_scaler.fit_transform(data.iloc[:, :96].values)

    # Checking if our data is balanced (if not, we should balance it to prevent our model to be biased)
    print(data_modif.clase.value_counts())

    ################################################################################################################

    # categorizamos las 10 categorias en un valor numeral y las codificamos.
    # Input values put in a matrix, there are 84 features
    X = data_modif.iloc[:, :96].values

    # Creating output values
    data_modif.clase = pd.Categorical(data_modif.clase)  # convert to categorical data
    y = np.array(data_modif.clase.cat.codes)  # create label encoded outputs
    # Print the first sample
    print("Features of the first sample: ", X[0])
    print("Class of the first sample: ", y[0])
    print(len(X), len(y))

    ############################################################################################################3

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=best, random_state=104)

    # Check sizes of input and output vectors
    print("Size of train features matrix: ", X_train.shape, ", Size of train output vector: ", y_train.shape)
    print("Size of test features matrix: ", X_test.shape, ", Size of test output vector: ", y_test.shape)

    #################################################################################################################

    from sklearn import svm
    clf = svm.SVC(gamma=1 / (X_train.shape[-1] * X_train.var()), probability=True)  # Set probability to True
    print(clf)

    # Fit model with training data
    clf.fit(X_train, y_train)

    # Predict classes of test samples
    y_pred = clf.predict(X_test)

    ##################################################################################################################
    accuracy = np.sum(y_test == y_pred) / len(y_test)

    # Data is balanced, so you can use accuracy as a measure:
    print(accuracy)

    # Print the confusion matrix
    # el plot de la matriz no funciona porq las

    classes = np.unique(data_modif.clase)
    conf_mat = pd.DataFrame(confusion_matrix(y_test, y_pred), columns=classes, index=classes)
    conf_mat.index.name = 'Actual'
    conf_mat.columns.name = 'Predicted'
    plt.figure(figsize=(7, 5))
    sns.set(font_scale=1.2)
    sns.heatmap(conf_mat, cmap="Blues", annot_kws={"size": 12}, annot=True)
    plt.show()

    # Guardar resultados en un archivo CSV
    results = [[y_test[i], y_pred[i], round(clf.predict_proba([X_test[i]])[0][y_pred[i]] * 100, 2)] for i in range(len(X_test))]
    with open('resultados.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(results)

    return accuracy, y_test, y_pred, clf

a = 0.1
accuracy, y_test, y_pred, clf = SVM_classifier(a)
