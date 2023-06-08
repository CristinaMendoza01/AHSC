import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
import csv

def SVM_classifier(best):
    data_file = 'fulldata.csv'

    # Leer el archivo CSV
    data = pd.read_csv(data_file)

    # Plot first lines of our data
    # print(data.head())

    sns.relplot(x="melbands_flatness_db.mean", y="spectral_centroid.mean", hue="clase", data=data)
    plt.show()

    data_modif = data.copy()

    # Let's use sklearn's preprocessing tools for applying normalisation to features
    from sklearn import preprocessing
    min_max_scaler = preprocessing.MinMaxScaler()
    data_modif.iloc[:, :96] = min_max_scaler.fit_transform(data.iloc[:, :96].values)

    # Selecciona todas las columnas excepto la última
    #cols = data_modif.columns[:-1]

    # Crea un nuevo DataFrame con las columnas seleccionadas
    #data_sel = data_modif[cols]
    #print(type(data_sel))


    #print(data_sel)

    #pca = PCA(n_components=2)
    #reduced_data = pd.DataFrame(pca.fit_transform(data_sel))

    #print(type(reduced_data))

    # Checking if our data is balanced (if not, we should balance it to prevent our model to be biased)
    print(data_modif.clase.value_counts())

    # Here we didn't pick the lowest number, 108 for frog, wind, screaming, which is too small.
    # Instead, we choose the 480 of "gunshot"
    min_number = data_modif.clase.value_counts()['gunshot']
    door_data = data_modif[data_modif.clase == 'door_window'].sample(n=min_number, random_state=42)
    guitar_data = data_modif[data_modif.clase == 'guitar'].sample(n=min_number)
    bowed_data = data_modif[data_modif.clase == 'bowedStringInstruments'].sample(n=min_number)
    bird_data = data_modif[data_modif.clase == 'bird'].sample(n=min_number)
    respiratory_data = data_modif[data_modif.clase == 'RespiratorySounds'].sample(n=min_number)
    alarm_data = data_modif[data_modif.clase == 'Alarm'].sample(n=min_number)
    laughter_data = data_modif[data_modif.clase == 'laughter'].sample(n=min_number)
    rain_data = data_modif[data_modif.clase == 'rain'].sample(n=min_number)
    interf_data = data_modif[data_modif.clase == 'interferences'].sample(n=min_number)
    bell_data = data_modif[data_modif.clase == 'bell'].sample(n=min_number)
    keyboard_data = data_modif[data_modif.clase == 'keyboardInstruments'].sample(n=min_number)
    household_data = data_modif[data_modif.clase == 'household_appliances'].sample(n=min_number)
    hits_data = data_modif[data_modif.clase == 'hits_footsteps'].sample(n=min_number)
    insect_data = data_modif[data_modif.clase == 'Insect'].sample(n=min_number)
    fire_data = data_modif[data_modif.clase == 'fire'].sample(n=min_number)
    gunshot_data = data_modif[data_modif.clase == 'gunshot'].sample(n=min_number)
    wind_data = data_modif[data_modif.clase == 'wind']
    screaming_data = data_modif[data_modif.clase == 'Screaming']
    frog_data = data_modif[data_modif.clase == 'frog']
    explosion_data = data_modif[data_modif.clase == 'explosion'].sample(n=min_number)
    telephone_data = data_modif[data_modif.clase == 'telephone'].sample(n=min_number)
    tools_data = data_modif[data_modif.clase == 'tools'].sample(n=min_number)
    motor_vehicle_data = data_modif[data_modif.clase == 'motor vehicle'].sample(n=min_number)

    # Merging after downsampling
    data_modif = pd.concat(
        [door_data, explosion_data, telephone_data, guitar_data, tools_data,bowed_data, bird_data, motor_vehicle_data,respiratory_data, alarm_data, laughter_data, rain_data, interf_data, bell_data, keyboard_data, household_data, hits_data, insect_data, fire_data, gunshot_data, wind_data, screaming_data, frog_data])

    # Checking the balance again
    data_modif.clase.value_counts()

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

a = 0.2
accuracy, y_test, y_pred, clf = SVM_classifier(a)
