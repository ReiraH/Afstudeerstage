import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

# number of points
n = 1000

# distance in meter or time period
Lx = 100

# angular frequency
omg = 2.0 * np.pi / Lx

# creating individual signals
x = np.linsoace(0, Lx, n)
y1 = 1.0 * np.cos(5.0 * omg * x)
y2 = 1.0 * np.sin(10.0 * omg * x)
y3 = 0.5 * np.sin(20.0 * omg * x)

# full signal
y = y1 + y2 + y3

#create all the neccessary frequencies
freqs = fftfreq(n)

# mask array to be used for power spectra and ignoring half the values.
mask = freqs > 0

# FFT and power spectra calculations
fft_vals = fft(y)

# true theoretical fft
fft_theo = 2.0 * np.abs(fft_vals / n)

plt.figure(1)
plt.title('Original Signal')
plt.plot(x, y, color='xkcd:salmon', label='original')
plt.legend()

plt.figure(2)