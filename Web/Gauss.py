import numpy
from numba import njit


#Алгоритм решения СЛАУ (кушает матрицу, выплевывает список(тип данных) решений
def gauss(a):
    for i in range(n):
        a[i] = a[i]/(a[i][i])
        for j in range(n):
            if i != j:
                a[j] = a[j]-a[i]*a[j][i]
    b = []
    for i in range(n):
        b.append(a[i][n])
    return(b)
