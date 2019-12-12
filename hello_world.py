#!/usr/bin/env python3 # Указание на интерпритатор
# -*- coding: utf-8 -*- # Кодировка

import math # Импортирование модуля "math" из стандартной библиотеки
import numpy # Подключение библиотеки "numpy"
import matplotlib.pyplot as mpp #Подключение модуля pyplot из библиотеки "matplotlib", называем его mpp


if __name__=='__main__': # Код в этой программе будет выполнен, если программа программа является самостоятельной
    arguments = numpy.r_[0:200:0.1] # Силами numpy мы создаем список от 0 до 200 с шагом 0,1
    mpp.plot(arguments, [math.sin(a) * math.sin(a/20.0) for a in arguments] # Создание зависимости sin(a)*sin(a/20) для всех значений списка 
    )
    mpp.show() # Отображение графика
