# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Calentamiento Global

# <codecell>

import pylab as pyl
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d, splrep, splev
import scipy as sp
import csv
import pandas as pd
from scipy.interpolate import griddata
import datetime as DT
import matplotlib as plt


# <codecell>

#!wget https://raw.githubusercontent.com/valentinaqf94/CM2015_HW4_ValentinaQuiroga/master/punto1/temperaturas.csv

# <codecell>

reader = pd.read_csv('temperaturas.csv') #el archivo se abre y se convierte en un arreglo que despues pasa a ser un .dat
#print reader

# <markdowncell>

# Cree un script de python llamado interp_temperaturas.py que haga y grafique una interpolaci ́ on lineal, polin ́ omica y por splines (escoja polinomio y ́orden de los splines) para cada una de las ciudades anteriores. Cu ́al m ́etodo es mejor? Justifique estad ́ıstica- mente su escogencia.

# <codecell>

bogota = reader[reader.ciudad == "Bogota"]
cali = reader[reader.ciudad == "Cali"]
bucar = reader[reader.ciudad == "Bucaramanga"]
bquilla = reader[reader.ciudad == "Barranquilla"]
ipiales = reader[reader.ciudad == "Ipiales"]

# <headingcell level=1>

# Interpolaciones Lineales

# <codecell>

#interpolaciones lineales
bog_1 = bogota.interpolate()
cali_1 = cali.interpolate()
bquilla_1 = bquilla.interpolate()
ipiales_1 = ipiales.interpolate()
bucar_1 = bucar.interpolate()

# <codecell>

bog_1.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bog_lin.png', bbox_inches='tight')

# <codecell>

cali_1.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Cali_lin.png', bbox_inches='tight')

# <codecell>

bquilla_1.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bquilla_lin.png', bbox_inches='tight')

# <codecell>

bucar_1.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bucar_lin.png', bbox_inches='tight')

# <codecell>

ipiales_1.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Ipia_lin.png', bbox_inches='tight')

# <headingcell level=1>

# Interpolaciones Polinomicas

# <codecell>

#interpolaciones polinomicas
bog_2 = bogota.interpolate(method= 'polynomial', order=2)
cali_2 = cali.interpolate(method= 'polynomial', order=2)
bquilla_2 = bquilla.interpolate(method= 'polynomial', order=2)
ipiales_2 = ipiales.interpolate(method= 'polynomial', order=2)
bucar_2 = bucar.interpolate(method= 'polynomial', order=2)

# <codecell>

bog_2.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bog_Poli.png', bbox_inches='tight')

# <codecell>

bquilla_2.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bquilla_Poli.png', bbox_inches='tight')

# <codecell>

bucar_2.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bucar_Poli.png', bbox_inches='tight')

# <codecell>

cali_2.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Cali_Poli.png', bbox_inches='tight')

# <codecell>

ipiales_2.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Ipia_Poli.png', bbox_inches='tight')

# <headingcell level=1>

# Interpolacion por Splines

# <codecell>

bog_3 = bogota.interpolate(method='spline', order=3)
cali_3 = cali.interpolate(method='spline', order=3)
bquilla_3 = bquilla.interpolate(method='spline', order=3)
ipiales_3 = ipiales.interpolate(method='spline', order=3)
bucar_3 = bucar.interpolate(method='spline', order=3)

# <codecell>

bog_3.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bog_Spli.png', bbox_inches='tight')

# <codecell>

cali_3.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Cali_Spli.png', bbox_inches='tight')

# <codecell>

bucar_3.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bucar_Spli.png', bbox_inches='tight')

# <codecell>

bquilla_3.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Bquilla_Spli.png', bbox_inches='tight')

# <codecell>

ipiales_3.drop(['Unnamed: 0', 'ciudad', 'año' ], 1).plot()
pyl.savefig('Ipia_Spli.png', bbox_inches='tight')

# <codecell>

#mean(bogota),   std(bogota)

# <headingcell level=4>

# "Las temperaturas regularmente oscilan entre los 6 y 22 °C, con una media anual de 14 °C" segun Ideam, luego vemos que aun pertenece a un rango aceptable.

# <codecell>

#mean(cali), std(cali)

# <headingcell level=4>

# Cali temperatura promedio es  25 °C. Dentro del rango normal.

# <codecell>

#mean(bucar), std(bucar)

# <headingcell level=4>

# Bucaramanga temperatura promedio es  23 °C. Dentro del rango normal.

# <codecell>

#mean(bquilla), std(bquilla)

# <headingcell level=4>

# Barranquilla temperatura promedio es  27.4 °C. Dentro del rango normal.

# <codecell>

#mean(ipiales), std(ipiales)

# <headingcell level=4>

# Ipiales temperatura promedio es  11 °C. Dentro del rango normal.

# <markdowncell>

# Con base a los resultados obtenidos en las distintas interpolaciones, he llegado a la conclusión que, al menos 
# estadísticamente, los resultados no son concluyentes pues su tendencia al alza o a la baja depende ampliamente
# de la representación de interpolación escogida. Prueba de esto está en que, en las gráficas obtenidas en el script de R,
# se puede denotar una ligera tendencia al alza en la temperatura de todas las ciudades; mientras que en las anteriores 
# interpolaciones se tuvo tendencias crecientes (interpolación lineal), tendencias constantes o crecientes (polinómicas) e 
# incluso tendencias decrecientes (splines grado 3). Esto también puede deberse a que las temperaturas con las que trabajamos 
# de por sí ya son promedio, por lo tanto estamos añadiendo un factor de error muy grande pues se tratan de sistemas dinámicos, 
# no promediables por métodos convencionales. Además, tomando en cuenta los datos de temperatura promedio y desviación estándar,
# no se ve un aumento significativo en ninguno de los casos.

# <codecell>


