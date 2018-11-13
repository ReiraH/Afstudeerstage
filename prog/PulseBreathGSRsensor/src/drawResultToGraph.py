import test1.py
import matplotlib.pyplot as plotter

duration = 60 #in seconds
deltaTime = 0.001
nrOfSteps = int (duration / deltaTime)


figure = plotter.figure () 

subplot = figure.add_subplot (111) 
subplot.set_xlim (0,3600) # in seocnds
subplot.set_ylim (0,4100) # max values in arduino

time = [deltaT * i for i in range (nrOfSteps)]

subplot.plot (time, grafiekloop, color ='blue')

plotter.show ()