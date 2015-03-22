# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#%pylab inline
import matplotlib.pyplot as plt
import Image
from mpl_toolkits.basemap import Basemap
import numpy as np

#from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# <codecell>

array = np.genfromtxt("hfile.csv",delimiter=",") #sube el csv
LAT = array[:,2] #elige las columnas de interes
LON = array[:,3]
#z = array[:,1]

# <codecell>

plt.figure(figsize=(40,35)) #tama;o de la imagen
map = Basemap(projection='robin', lat_0=0, lon_0=120, #ubicacion del mapa mundi centrado en dichas lat y lon
    resolution = 'l', area_thresh = 1000.0) 
plt.title(u"Ubicacion ríos más caudalosos",fontsize=36)
map.drawcoastlines()
map.drawcountries()
map.bluemarble()
map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
#aqui se generan los datos x,y para graficar con plot
x,y = map(LAT, LON)
map.scatter(x, y, color='red')
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
#show()
plt.savefig('myfig.png')

# <codecell>


# <codecell>


#!ls

# <codecell>


# <codecell>


# <codecell>


