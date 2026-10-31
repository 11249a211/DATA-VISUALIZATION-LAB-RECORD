Experiment: Bar Graph in R
Aim
To create a bar graph using R programming to represent and compare values across different categories.

Algorithm
Start the program.

Define the categories and their corresponding values.

Use the barplot() function to create the bar graph.

Add a title and labels to the X-axis and Y-axis.

Set the colors of the bars.

Display the bar graph.

Stop the program.

Description
A bar graph is a data visualization technique used to compare values among different categories. Each bar represents a category, and its height indicates the corresponding value.

In R, the barplot() function is used to create bar graphs. The main parameter specifies the title, xlab and ylab specify the axis labels, and col sets the bar colors.

Program

# Define the data
technologies <- c("Python", "Java", "R", "Tableau", "SQL")
marks <- c(85, 78, 82, 90, 88)

# Create the bar graph
barplot(marks,
        names.arg = technologies,
        main = "Marks in Different Technologies",
        xlab = "Technologies",
        ylab = "Marks",
        col = "lightblue",
        border = "black")

Sample Output
A bar graph titled Marks in Different Technologies is displayed.

X-axis: Technologies

Y-axis: Marks

Five bars represent Python, Java, R, Tableau, and SQL.

Tableau has the highest value of 90.

Result
Thus, a bar graph was successfully created using R to compare values across different categories.
