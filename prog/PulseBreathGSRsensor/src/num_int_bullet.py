import matplotlib.pyplot as plotter

duration = 200
deltaT = 0.1
nrOfSteps = int (duration / deltaT)

figure = plotter.figure () 

subplot = figure.add_subplot (111) 
subplot.set_xlim (0,30) 
subplot.set_ylim (0,600)

s0 = 0
v0 = 100
g = 9.81

time = [deltaT * i for i in range (nrOfSteps)]
analytic = [v0 * t - 0.5 * g * t**2 for t in time]

# Euler integration
euler = [s0]
v = [v0]
for stepNr in range (nrOfSteps - 1):
    v.append (v [-1] - g * deltaT)
    euler.append (euler [-1] + v [-1] * deltaT)

    
subplot.plot (time, analytic, color ='blue')
subplot.plot (time, euler, color ='red')

plotter.show ()
