# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#%pylab inline
import numpy as np
import urllib2
import urllib
import Image
from mpl_toolkits.basemap import Basemap
import csv
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# <codecell>

url = 'http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt' #libreria para descargar archivos de url
urllib.urlretrieve(url, "catalogo.txt")
f = urllib.urlopen(url)
data = f.read()
with open("catalogo.txt", "wb") as code: #reconstruye el archivo linea por linea
    code.write(data)

# <codecell>

lst = map(str, open('catalogo.txt').readlines()) #convierte las lineas en una lista
todo = np.asarray(lst) #convierte a arreglo

# <codecell>

##solo queremos operar con la segunda columna, se crea un arreglo de dos dimensiones con el indice y el numero buscado
A = np.zeros((len(todo),2))
B = np.zeros(len(todo))
C = np.zeros(len(todo))
for i in range(1, len(todo)):
    a = todo[i].split(' ') #separa las lineas del arreglo por espacios
    a[:] = [x for x in a if x != ''] #escoge todo lo que no sea espacio
    A[i,0] = i
    A[i,1] = a[1]
    B[i] = a[2]
    C[i] = a[3]
A = A[1:,:] #define el nuuevo arreglo

# <codecell>

A_sorted = A[A[:, 1].argsort()] #ordena de menor a mayor el arreglo
A_i = A_sorted[925-300:925,:] #selecciona los ultimos 300 que ya sabemos que son los mayores
index = A_i[:,0]
ratio = A_i[:,1]
lon = []
lat = []
for el in index:
    lon.append(B[int(el)])
    lat.append(C[int(el)])

# <codecell>

EL_QUE_VA_PA_CSV = np.column_stack((index,ratio,lon,lat))

# <codecell>

fileout = open("hfile.csv", "w")
fileout.write('No,m2s_ratio,lonm,latm\n') 
for i in range(300):
    fileout.write('%f,%f,%f,%f\n'%(index[i],ratio[i],lon[i],lat[i]))
fileout.close()

# <codecell>

#for el in lat: #la lista para basemap
    #print el
#type(flux)
#values = ','.join(str(v) for v in flux)
#values.split()
#values[::-1]

# <codecell>

#for el in top_300:
    #print el

# <codecell>

a = lat
b = lon
c=np.column_stack((a,b)) 
d = c.tolist()

# <codecell>

son_todos=[] #vuelve a llenar en el arreglo inicial que tiene todos los datos
for j in range(len(todo)):
    b = todo[j].split(' ')
    b[:] = [x for x in b if x != '']
    son_todos.append(b)  


# <codecell>

#for j in son_todos:
    #print j

# <codecell>

with open("top_basemap.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(d)

# <codecell>

csvfile = "top_300.csv" #guarda como archivo csv
with open(csvfile, "w") as output:
    writer = csv.writer(output, delimiter=' ', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for val in son_todos:
        writer.writerow([val])    
with open("top_basemap.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(d)

# <codecell>

#!ls

# <codecell>

#!head hfile.csv

# <codecell>


# <codecell>


