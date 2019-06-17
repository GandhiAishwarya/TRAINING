import matplotlib
from matplotlib import pyplot as plt
import csv

year=[]
inches=[]
with open('sealevel.csv') as file:
    plots= csv.reader(file, delimiter=',')
    next(plots)
    for row in plots:
        year.append(int(row[0]))
        inches.append(float(row[1]))
         
plt.plot(year, inches)
plt.title("Sealevel analyis")
plt.xlabel("Year")
plt.ylabel("Sea Level in Inches")
plt.show()