EXPERIMENT: LINE GRAPH USING PYTHON
AIM
To create a line graph using Python's Matplotlib library to represent changes in values over a period of time.

ALGORITHM
Start the program.

Import the Matplotlib library.

Define the X-axis and Y-axis data.

Use the plt.plot() function to create the line graph.

Add a title to the graph.

Label the X-axis and Y-axis.

Display the graph using plt.show().

Stop the program.

DESCRIPTION
A line graph is a data visualization technique used to display changes in data over a continuous interval or period of time. It connects individual data points using straight lines to show trends and patterns.

Python's Matplotlib library provides the plot() function to create line graphs. In this program, monthly sales values are represented graphically to understand how sales change over time.

PROGRAM

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 90, 150, 170, 160]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

PROGRAM EXPLANATION
import matplotlib.pyplot as plt – Imports the Matplotlib plotting module.

months = [...] – Stores the month names for the X-axis.

sales = [...] – Stores the corresponding sales values for the Y-axis.

plt.plot(months, sales, marker="o") – Creates a line graph and displays circular markers at each data point.

plt.title("Monthly Sales") – Sets the title of the graph.

plt.xlabel("Months") – Labels the X-axis as Months.

plt.ylabel("Sales") – Labels the Y-axis as Sales.

plt.show() – Displays the line graph.

SAMPLE OUTPUT
Plaintext
A line graph titled "Monthly Sales" is displayed.

X-axis: Months
Y-axis: Sales

Jan - 100
Feb - 120
Mar - 90
Apr - 150
May - 170
Jun - 160
The graph shows that sales increase from January to February, decrease in March, rise until May, and decrease slightly in June.

RESULT
Thus, a line graph was successfully created using Python's Matplotlib library to represent changes in monthly sales.
