EXPERIMENT: PIE CHART USING PYTHON
AIM
To create a pie chart using Python's Matplotlib library to represent the percentage contribution of different technologies.

ALGORITHM
Start the program.

Import the Matplotlib library.

Define labels for different technologies.

Define the corresponding values for each technology.

Use the plt.pie() function to create the pie chart.

Display percentage values using the autopct parameter.

Add a title to the pie chart.

Display the chart using plt.show().

Stop the program.

DESCRIPTION
A pie chart is a circular statistical graph divided into sectors to represent the proportions of different categories in a dataset. Each sector represents a category, and its size is proportional to the corresponding value.

Python's Matplotlib library provides the pie() function to create pie charts. In this program, the percentage contributions of Python, Java, R, and Tableau are represented using a pie chart. The autopct parameter displays the percentage of each sector.

PROGRAM

import matplotlib.pyplot as plt
labels = ["Python", "Java", "R", "Tableau"]
values = [35, 25, 20, 20]
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("Technology Usage")
plt.show()
"""Program Explanation
The pie() function divides a circle into sectors according to the supplied values. The labels identify
the sectors and autopct displays the percentage contribution."""


PROGRAM EXPLANATION
import matplotlib.pyplot as plt – Imports the Matplotlib plotting module.

labels = ["Python", "Java", "R", "Tableau"] – Defines the labels for the four technologies.

values = [35, 25, 20, 20] – Specifies the values for each technology.

plt.pie(values, labels=labels, autopct="%1.1f%%") – Creates the pie chart, displays the category labels, and shows percentages to one decimal place.

plt.title("Technology Usage") – Sets the title of the chart.

plt.show() – Displays the pie chart.

SAMPLE OUTPUT
Plaintext
A pie chart titled "Technology Usage" is displayed.

Python  : 35.0%
Java    : 25.0%
R       : 20.0%
Tableau : 20.0%
The pie chart contains four sectors representing the technologies. Python occupies 35%, Java occupies 25%, and R and Tableau each occupy 20%.

RESULT
Thus, a pie chart was successfully created using Python's Matplotlib library to represent the percentage contribution of different technologies.
