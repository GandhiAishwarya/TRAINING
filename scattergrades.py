import matplotlib
from matplotlib import pyplot as plt

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(grades_range, boys_grades, marker='o', color='green',label='Boys_Grades')
plt.scatter(grades_range, girls_grades, marker='x', color='red', label='Girls_Grades')

plt.xlabel("Grades_Range")
plt.ylabel("Grades of boys and girls")
plt.title("Performance")


plt.legend()
plt.show()

