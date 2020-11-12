import numpy
import flask
import csv

def gauss(filename):
    a = list()
    with open(filename, "r") as file:
        reader = csv.reader(file, delimiter = ';')
        for row in reader:
            a.append(row)
            
    lr = len(a[0])
    lc = len(a)
    
    for i in range(lc):
        for j in range(lr):
            a[i][j] = int(a[i][j])

    for i in range(lc):
        for j in range(lc):
            a[i][j] = a[i][j]/(a[i][i])
    for i in range(lc):
        for j in range(lc):
            if i != j:
                for k in range(lr):
                    a[j][i] = a[i][j]-a[j][j]*a[j][i]
    o = [0] * lc
    for k in range(0, lc):
      o[k] = a[lc-1][k]
    return(o)

