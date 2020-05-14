## Problema inicial anaconda y vs code.. parece surgía de bash como terminal, pase a cmd.

# GeorgeMKhoury commented on 2 Feb
# For anyone else who runs into this issue and finds this thread: Not an issue with numpy, but rather with VS code. You need to tell VS Code to activate the appropriate conda environment in settings: Python>Terminal:Activate Environment. Note that if you install anaconda with default settings, this does not work properly if your terminal is git bash, but it works fine if you use cmd (and the integrated terminal).


import os #para navegar por los directorios del sistema.
import fnmatch # Unix filename pattern matching, va a servir para wildcards *.txt y derivar regex
import pandas as pd
import numpy as np
import csv

path = os.getcwd() #Directorio actual
print(path)

with open('GEMCSVSAMPLE\G505261_200210T081343.CSV') as csvfile:
    readCSV = csv.reader(csvfile)
    print(readCSV)












### Referencias copiadas.


for path,dirs,files in os.walk('.'): 
    for f in fnmatch.filter(files,'*.csv'): #lista los archivos que cumplan con la condición.
        fullname = os.path.abspath(os.path.join(path,f))
        text = open(fullname).read()
        print(fullname)
        print('testing')
        print(text)

# print(os.getcwd())
# f = open(fullname) 
# text = fj.read()
# print(text) 
# fj.close() 



