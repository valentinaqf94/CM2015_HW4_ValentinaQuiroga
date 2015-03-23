# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#Hallando el espectro de frecuencias del archivo de voz que entra por parametro, de nuevo ENVIA UN AVISO CUANDO COMPILA PERO NO COMPROMETE SU DESEMPENIO.
from scipy.fftpack import fft, fftfreq
import scikits.audiolab as audio
import matplotlib.pyplot as plt
import numpy as np

# <codecell>

input_signal, sampling_rate, enc = audio.wavread("minombre.wav") #entra por parametro el archivo grabado en script de C
print (input_signal[0:10]), sampling_rate, enc 

# <codecell>

time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate)) #establece el conteo del tiempo

# <codecell>

n = len(time_array) #puntos por medicion
f = 200.0 #  frecuencia Hz
dt = 1 / (f * n/32 ) #32 datos por frecuencia

# <codecell>

signalFFT = fft(input_signal)/n
#ignalPSD = np.abs(signalFFT) ** 2
fftFreq = fftfreq(n, dt)
#i = fftfreq>0
np.shape(fftFreq)
np.shape(signalFFT)

# <codecell>

fig = plt.figure()
graf = plt.plot(fftFreq,abs(signalFFT))
plt.xlim(-70000,70000)
plt.title("Grafica FFT de Voz", fontsize=20)
plt.xlabel("Frecuencia (1/s)", fontsize=15)
plt.ylabel("Amplitud", fontsize=15)
plt.savefig("mi_voz_fft.png")

# <headingcell level=3>

# Para hallar el armónico más grande, se recurrió a la funcion de numpy llamada argmax() la cual retorna el indice del mayor valor de un 
# arreglo, en este caso del arreglo de las amplitudes. Acto seguido, dado que los arreglos que guardan las amplitudes y frecuencias respetan en mismo orden, se halló el índice
# que correspondía a dicha amplitud pero en el arreglo de la frecuencia, encontrando así que el armónico más grande está en (0.00095, 24225).

# <codecell>

a = max(abs(signalFFT)) #maximo de amplitud de la grafica anterior
print a

# <codecell>

b = np.argmax(signalFFT) #indice del maximo valor amplitud para hallar la frecuencia correspondiente

# <codecell>

abs((fftFreq[b])) #valor de la frecuencia que corresponde con el armonico mas grande, es simetrico en el eje x por lo que tomamos su valor absoluto solo por conveniencia

# <codecell>

#!ls 

# <codecell>


# <codecell>


