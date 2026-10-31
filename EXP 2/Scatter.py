EXPERIMENT: SCATTER PLOT USING PYTHON
AIM
To create a scatter plot using Python's Matplotlib library to visualize the relationship between study hours and marks.

ALGORITHM
Start the program.

Import the Matplotlib library.

Define the study hours and corresponding marks.

Use the plt.scatter() function to create the scatter plot.

Add a title to the plot.

Label the X-axis and Y-axis.

Display the plot using plt.show().

Stop the program.

DESCRIPTION
A scatter plot is a data visualization technique used to show the relationship between two numerical variables. It represents each observation as an individual point on a graph.

Python's Matplotlib library provides the scatter() function to create scatter plots. In this program, study hours are represented on the X-axis and marks are represented on the Y-axis. The plotted points help us understand the relationship between study hours and marks.

PROGRAM

import matplotlib.pyplot as plt
hours = [1, 2, 3, 4, 5, 6]
marks = [45, 50, 58, 65, 72, 80]
plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

"""Program Explanation
The scatter() function displays observations as individual points. Study hours are placed on the
X-axis and marks on the Y-axis. The resulting pattern can be used to study the relationship between
the variables."""

PROGRAM EXPLANATION
import matplotlib.pyplot as plt – Imports the Matplotlib plotting module.

hours = [1, 2, 3, 4, 5, 6] – Stores the study hours.

marks = [45, 50, 58, 65, 72, 80] – Stores the corresponding marks.

plt.scatter(hours, marks) – Creates the scatter plot using individual points.

plt.title("Study Hours vs Marks") – Sets the title of the plot.

plt.xlabel("Study Hours") – Labels the X-axis.

plt.ylabel("Marks") – Labels the Y-axis.

plt.show() – Displays the scatter plot.

SAMPLE OUTPUT
Plaintext
A scatter plot titled "Study Hours vs Marks" is displayed.

X-axis: Study Hours
Y-axis: Marks

Study Hours    Marks
     1           45
     2           50
     3           58
     4           65
     5           72
     6           80
The scatter plot displays six points. The points show an increasing trend, indicating that higher study hours are associated with higher marks in this sample dataset.

RESULT
Thus, a scatter plot was successfully created using Python's Matplotlib library to visualize the relationship between study hours and marks.
