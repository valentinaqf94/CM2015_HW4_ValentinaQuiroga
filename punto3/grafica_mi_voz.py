# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>
#este script grafica la voz proveniente de la entrada por parametro desde C. ESDE NOTAR QUE PESE A QUE SACA UN WARNING AL EJECUTAR, FUNCIONA PERFECTAMENTE. DICHO AVISO PUEDE PROVENIR DE LAS CONDICIONES DE AUDIOLAB PERO NO COMPROMETE SU FUNCIONAMIENTO.

import scikits.audiolab as audio
from scipy.fftpack import fft, fftfreq
import wave as wv
import matplotlib.pyplot as plt
import numpy as np

# <codecell>

input_signal, sampling_rate, enc = audio.wavread("minombre.wav") #entra por parametro el archivo grabado en script de C
print (input_signal[0:10]), sampling_rate, enc 

# <codecell>

time_array = np.arange(0, len(input_signal)/float(sampling_rate), 1/float(sampling_rate)) #establece el conteo del tiempo

# <codecell>

fig = plt.figure() #grafica la voz
plt.plot(time_array[0:100000], input_signal[0:100000])
plt.title("Grafica Amplitud vs tiempo", fontsize=20)
plt.xlabel("Tiempo (s)", fontsize=15)
plt.xlim(0.0,2.1)
plt.ylim(-0.20,0.20)
plt.ylabel("Amplitud", fontsize=15)
plt.savefig("mi_voz.png")

# <codecell>


