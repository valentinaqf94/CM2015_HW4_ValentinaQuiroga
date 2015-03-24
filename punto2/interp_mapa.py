# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from __future__ import print_function 
import netCDF4
import numpy as np
import scipy as sp
from scipy import interpolate
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#para ver ambas imagenes CIERRE primero la que se genera al principio, la siguiente surgira despues de esta accion.

# <codecell>

nc = netCDF4.Dataset('air.mon.ltm.nc') #sube el archivo .nc a python

# <codecell>

nc.variables.keys() #muestra todas las variables del .nc

# <codecell>

airTemp = nc.variables['air'] #declara la variable de interes
#clim = nc.variables['climatology_bounds'] 

# <codecell>

airTemp.long_name #para ver el titulo que tiene en realidad, no el que esta guardado en la maquina

# <codecell>

airTemp.dimensions #dimensiones del arreglo

# <codecell>

airTemp.shape #forma del arreglo

# <codecell>

data = airTemp[0] #escogemos los datos de lat y lon
data.shape

# <codecell>

LON = nc.variables['lon'] #los guardamos en dichas variables para graficarlos 
LAT = nc.variables['lat']

# <codecell>

lonvals = LON[:]
latvals = LAT[:]

# <codecell>

plt.title (airTemp.long_name + ' (' + airTemp.units + ')') #grafica en contornos de los datos, los limites van dados por los mismos datos de la tabla
plt.xlabel(LON.long_name    + ' (' + LON.units    + ')')
plt.ylabel(LAT.long_name    + ' (' + LAT.units    + ')')
plt.contourf(lonvals, latvals, data,cmap=plt.get_cmap('Reds'))
plt.colorbar()
mapa = Basemap(lon_0=180)#dibuja el mapa con basemap 
mapa.drawcoastlines()
plt.show()

# <headingcell level=3>

# Interpolación Nearest Neighbors

# <codecell>


plt.title ('Interpolacion') #grafica en contornos de los datos, los limites van dados por los mismos datos de la tabla
#plt.imshow(data, cmap=plt.get_cmap('spectral'), interpolation ='nearest') 
plt.xlabel(LON.long_name    + ' (' + LON.units    + ')')
plt.ylabel(LAT.long_name    + ' (' + LAT.units    + ')')
plt.contourf(lonvals, latvals, data,cmap=plt.get_cmap('Reds'), interpolation = 'nearest')
plt.colorbar()
mapa = Basemap(lon_0=180)#dibuja el mapa con basemap 
mapa.drawcoastlines()
plt.show()




# <headingcell level=4>

# Vemos que el cambio de imagen interpolada a imagen normal se da en la mayor nitidez que tiene la imagen.

# <codecell>


