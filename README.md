# turtlebars
A fun little python function to draw bar graphs with turtle graphics!

## Using graphs.py

While it provides little practical utility, it is capable of generating and storing bar graphs (SVG). Here's how to call it:

* Import graphs into your code with:
*  > import graphs.py
* Call the draw_bar() function in the following manner:
* > draw_graph(dataset,title_graph,scale,max_range)

1. dataset: as an array [[value,title],[value,title]...[value,title]]
2. title_graph: a string containing the title of the graph
3. scale: Specifies scale of marked values to be marked in graph
4. max_range: The maximum possible value of data

