import matplotlib.pyplot as plotter
from math import *

g = 9.81
length = 2
T = 2 * pi * sqrt (length / g)
nrOfPeriods = 4
deltaT = 0.01
nrOfSteps = round ((nrOfPeriods * T) / deltaT)
alpha0 = 0.25 * pi


print (f'Nr of steps: {nrOfSteps}')
print (f'T should be {T}')

time = [deltaT * i for i in range (nrOfSteps)]
axis = [0 for t in time]
alphas = []

alpha = alpha0
v = 0
s = length * alpha

# Euler integration
for stepNr in range (nrOfSteps):
    alphas.append (alpha)
    a = -g * sin (alpha)
    v = v + a * deltaT
    s = s + v * deltaT
    alpha = s / length

    
phis = [alpha0 * cos (2 * pi * i * (deltaT / T)) for i in range (nrOfSteps)]

# Alternative:
#phis = [alpha0 * cos (sqrt (g / length)* i * deltaT) for i in range (nrOfSteps)]
    
figure = plotter.figure () 
subplot = figure.add_subplot (111) 
subplot.set_xlim (0, nrOfSteps * deltaT) 
subplot.set_ylim (-alpha0, alpha0)

subplot.plot (time, axis, color='black')
subplot.plot (time, alphas, color ='blue')
subplot.plot (time, phis, color ='green')

plotter.show ()


