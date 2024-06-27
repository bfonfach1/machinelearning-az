#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 19:43:11 2019

@author: juangabriel
"""

# Plantilla de Pre Procesado

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt #para llamar una sublibreria es la libreria.la sublibreriaq se quiere
import pandas as pd #libreria para cargar datos 

#Importar el dataset
dataset = pd.read_csv('Data.csv') #pd es como llame a pandas


#--> la variable X representa las variables independientes y la variables Y las variables dependientes

X = dataset.iloc[:, :-1].values # la funcion iloc sirve para identificar los elementos de un dataset por posicion. El  desde:hasta, si no quiero la ultima es [ :-1].value
y = dataset.iloc[:, 3].values

#tratamiento de los NAs o valores que no estan en el data frame
from sklearn.preprocessing import Imputer  #imputer sirve para iputar los datos que faltan, usamos from ___- import solo la funcion que queremos de la libreria}
imputer = Imputer(missing_values = 'nan', strategy = 'mean', axis = 0) #axis=0 se le aplica a la columna 
