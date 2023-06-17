import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def evaluar_svm(csv_file):
    df = pd.read_csv(csv_file, header=None)

    y_true = df.iloc[:, 0]
    y_pred = df.iloc[:, 1]

    y_true = y_true.astype(int)
    y_pred = y_pred.astype(int)

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')

    # Calcular la matriz de confusión
    cm = confusion_matrix(y_true, y_pred)

    # Obtener los valores de TP, FP, TN y FN
    tp = np.diag(cm)
    fp = np.sum(cm, axis=0) - tp
    fn = np.sum(cm, axis=1) - tp
    tn = np.sum(cm) - (tp + fp + fn)

    print("\nQuantitative evaluation:\n")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-Score:", f1)
    print("\nTrue Positives (TP):\n", tp, "\n")
    print("False Positives (FP):\n", fp, "\n")
    print("True Negatives (TN):\n", tn, "\n")
    print("False Negatives (FN):", fn)

##############################################
evaluar_svm("resultados.csv")
