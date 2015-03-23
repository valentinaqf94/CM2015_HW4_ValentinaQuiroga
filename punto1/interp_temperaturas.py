# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Interpolacion!

# <codecell>

#pylab inline
import numpy as np
from scipy import interpolate
from scipy.interpolate import interp1d
import scipy as sp
import csv
import pandas as pd

# <codecell>

#!wget https://raw.githubusercontent.com/valentinaqf94/CM2015_HW4_ValentinaQuiroga/master/punto1/temperaturas.csv

# <codecell>

reader = pd.read_csv('temperaturas.csv.1') #el archivo se abre y se convierte en un arreglo que despues pasa a ser un .dat
print reader

# <markdowncell>

# Cree un script de python llamado interp_temperaturas.py que haga y grafique una interpolaci ́ on lineal, polin ́ omica y por splines (escoja polinomio y ́orden de los splines) para cada una de las ciudades anteriores. Cu ́al m ́etodo es mejor? Justifique estad ́ıstica- mente su escogencia.

# <codecell>

bogota = reader[reader.ciudad == "Bogota"]
cali = reader[reader.ciudad == "Cali"]
bucar = reader[reader.ciudad == "Bucaramanga"]
bquilla = reader[reader.ciudad == "Barranquilla"]
ipiales = reader[reader.ciudad == "Ipiales"]

# <codecell>

bogota1 = bogota.iloc[:,[3,5]]
cali1 = cali.iloc[:,[3,5]]
bquilla1 = bquilla.iloc[:,[3,5]]
ipiales1 = ipiales.iloc[:,[3,5]]
bucar1 = bucar.iloc[:,[3,5]]

# <codecell>

def cambiar_fechas(a):
    fechas = []
    for date in a:
        fecha = plt.datetime.datetime.strptime(date,"%Y/%m/%d")
        fechas.append(fecha)
    #dates = sort(dates)
    return fechas

# <codecell>

bog_temp=bogota1.iloc[:,1]
bog_fech = bogota1.iloc[:,0]
interBog = cambiar_fechas(bog_fech)
cali_temp=cali1.iloc[:,1]
cali_fech = cali1.iloc[:,0]
interCali = cambiar_fechas(cali_fech)

#print bog_fech

# <codecell>

plot(interBog,bog_temp)
xlabel("Fechas")
ylabel("Temperaturas")

    

# <codecell>

fechas = matplotlib.dates.date2num(fechas)
fit = polyfit(interBog,bog_temp,2)
fit_fn = poly1d(fit) # Poyfit para buscar la interpolacion mas fiel a la grafica

#plot(A,B,'r--',A, fit_fn(A), '--k')
#no se como convertir ese formato

# <codecell>

fcubic = interp1d(interBog,bog_temp,kind = "cubic")

# <codecell>


# <codecell>




# <headingcell level=1>


# <codecell>


# <codecell>


