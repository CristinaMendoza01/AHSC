import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
import csv
from sklearn import preprocessing

def SVM_classifier(best):
    data_file = 'clases_filtrados.csv'

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


    # Merging after downsampling

    # Checking the balance again
    data_modif.clase.value_counts()

    ################################################################################################################

    # categorizamos las 10 categorias en un valor numeral y las codificamos.
    # Input values put in a matrix, there are 84 features
    X = data_modif.iloc[:, :96].values

    # Creating output values
    data_modif.clase = pd.Categorical(data_modif.clase)  # convert to categorical data
    y = np.array(data_modif.clase.cat.codes)  # create label encoded outputs

    for i in range(len(y)):
       print('label:', y[i], "classe: ", data_modif.clase[i])


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



def classify_new_sounds(new_sounds, clf, min_max_scaler):
    normalized_sounds = new_sounds.copy()

    # Aplica la normalización a los nuevos datos
    normalized_sounds.iloc[:, :95] = min_max_scaler.fit_transform(new_sounds.iloc[:, :95].values)

    # Clasifica los nuevos datos utilizando el modelo SVM
    predictions = clf.predict(normalized_sounds)

    horror_sounds = pd.read_csv("horrorSounds.csv")

    # Crear una lista de resultados que contenga el id, las tres categorías con las probabilidades más altas
    results = []
    for i in range(len(new_data)):
        sound_id = horror_sounds.iloc[i, -1]  # Obtener el id de cada sonido de la última columna del archivo de entrada
        probabilities = clf.predict_proba(normalized_sounds.iloc[i:i + 1])[0]  # Obtener las probabilidades de todas las categorías para el sonido
        top_classes = np.argsort(probabilities)[-5:][::-1]  # Obtener los índices de las tres categorías con las probabilidades más altas
        top_probabilities = probabilities[top_classes]  # Obtener las probabilidades correspondientes a las tres categorías

        result_row = [sound_id]  # Agregar el id del sonido al resultado

        # Agregar las tres categorías y sus respectivas probabilidades al resultado
        for class_index, probability in zip(top_classes, top_probabilities):
            #predicted_class = predictions[i]  # Obtener la clase predicha para el sonido
            result_row.extend([class_index, probability])

        results.append(result_row)

    # Crear un nuevo DataFrame con los resultados
    columns = ['sound_id', 'category_1', 'prob_1', 'category_2', 'prob_2', 'category_3', 'prob_3', 'category_4', 'prob_4', 'category_5', 'prob_5']
    results_df = pd.DataFrame(results, columns=columns)

    # Guardar los resultados en un nuevo archivo CSV
    results_csv_file = 'results.csv'  # Nombre del nuevo archivo CSV
    results_df.to_csv(results_csv_file, index=False)

    return predictions



# Supongamos que tienes nuevos sonidos en la matriz 'new_sounds'
new_data_file = 'horrorsounds-id.csv'

# Leer el archivo CSV
new_data = pd.read_csv(new_data_file)
min_max_scaler = preprocessing.MinMaxScaler()

# Clasifica los nuevos sonidos utilizando el modelo SVM entrenado
predictions = classify_new_sounds(new_data, clf, min_max_scaler)

# Imprime las predicciones de clase
print(predictions)







