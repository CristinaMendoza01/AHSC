import csv

with open('../program/resultados.csv', 'r') as file:
    csv_reader = csv.reader(file)

    # 2nd col is Prediction (class) and 3rd col is Prob
    for row in csv_reader:
        print(row)