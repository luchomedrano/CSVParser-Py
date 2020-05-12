import os
import fnmatch

path = os.getcwd() #Directorio actual
for path,dirs,files in os.walk('.'): 
    for f in fnmatch.filter(files,'*.csv'): #lista los archivos que cumplan con la condición.
        fullname = os.path.abspath(os.path.join(path,f))
        text = open(fullname).read()
        print(fullname)
        print(text)

# print(os.getcwd())
# f = open(fullname) 
# text = fj.read()
# print(text) 
# fj.close() 
