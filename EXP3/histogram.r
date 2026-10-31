EXPERIMENT: HISTOGRAM USING R
AIM
To create a histogram using R programming to represent the frequency distribution of numerical data.

ALGORITHM
Start the program.

Define a dataset containing numerical values.

Use the hist() function to create the histogram.

Add a title to the histogram.

Label the X-axis and Y-axis.

Specify the colours of the bars.

Display the histogram.

Stop the program.

DESCRIPTION
A histogram is a data visualization technique used to represent the frequency distribution of numerical data. It groups data into intervals called bins, and the height of each bar indicates the frequency of observations within that interval.

R provides the built-in hist() function to create histograms. Histograms are useful for understanding the distribution, spread, and concentration of numerical data.

R SOURCE CODE
marks <- c(45, 50, 52, 55, 58, 60, 62, 65, 68,
           70, 72, 75, 78, 80, 82, 85, 88, 90)

hist(marks,
     breaks = 5,
     main = "Distribution of Marks",
     xlab = "Marks",
     ylab = "Frequency",
     col = "lightblue",
     border = "black")

SAMPLE OUTPUT
A histogram titled Distribution of Marks is displayed.

X-axis: Marks

Y-axis: Frequency

Number of intervals: Approximately 5, depending on how R selects the histogram breaks.

The bars represent the frequency of marks falling within each interval.

RESULT
Thus, a histogram was successfully created using R programming to represent the frequency distribution of marks.
