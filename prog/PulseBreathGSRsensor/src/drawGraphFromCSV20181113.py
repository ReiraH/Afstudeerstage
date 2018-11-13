import matplotlib.pyplot as plt
import csv

x = []
y = []
xa = 1
with open('all_sensors.csv','r') as csv_file:
    plots = csv.reader(csv_file, delimiter=',')
    header = next(plots)
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[3]))


plt.plot(x, y, color = 'blue')
plt.xlabel('x')
plt.ylabel('y')
plt.show()