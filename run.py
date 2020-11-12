#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:50:23 2020

@author: isabellatobias
"""
#Graph for analysis of dispersion of values as a function of time

#The chart will contain two types of data: canceled orders and active orders at the end of a period of time

#Imports the required libraries

#Pandas for spreadsheet manipulation
#Matplotlib for displaying the graph
import pandas as pd
import matplotlib.pyplot as plt

#Open asset file
#The first column contains the date and the second contains the values
#Selects the first column
#Recognizes column data as date (DD / MM / YY)
#Selects the second column

data = pd.read_csv("01.csv")
data_ativos = data.iloc[:,0] 
data_ativos = [pd.to_datetime(d) for d in data_ativos]
venda_ativos = data.iloc[:,1]

#Open the file of canceled values
#Selects the first column
#Recognizes column data as date (DD / MM / YY)
#Selects the second column
data = pd.read_csv("02.csv")
data_cancelados = data.iloc[:,0] 
data_cancelados = [pd.to_datetime(d) for d in data_cancelados]
venda_cancelados = data.iloc[:,1]


#Figure size
#Plot the active data
#Plot the canceled data
plt.figure(figsize = (15,10))
plt.scatter(data_ativos,venda_ativos, color='b', label='Ativos')
plt.scatter(data_cancelados,venda_cancelados, color='r', label='Cancelados')

#Name the x axis
#Name the y-axis
#Position of the subtitles
#Place the title
#Place grid
plt.xlabel('Data')
plt.ylabel('Número de Vendas')
plt.legend(loc='best')
plt.title("Ciclo 1")
plt.grid(True)

#Displays the graph
plt.show()
