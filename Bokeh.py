from bokeh.plotting import figure, show

# Prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Create a new plot with a title and axis labels
p = figure(title="Simple Line Example", x_axis_label='x', y_axis_label='y')

# Add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Temp.", line_width=2)

# Show the results (opens in a web browser)
show(p)