# Weather_Graph_Generator
The program will read a csv file of weather data and generate a line graphn showing the highs and lows temperature each day.
> Currently the program only works with ct_weather.csv file


### Why does it only work with ct_weather.csv? 
1. This is my first project, so there are many examples of stinky codes, not following conventions, and no tests.
2. ct_weather.csv has some weird format and missing data that I had to designed my program uniquely for it.

### What so weird about ct_weather.csv?
In a normal csv file (especially one for weather data), there should be number or string values separated by commas.

Well, **ct_weather.csv** decided to make all its values into strings even the numbers.
![alt text][csv bad]

[csv bad]: https://github.com/Mintri1199/Weather_Graph_Generator/blob/master/bad_format.png

Along with it's format, it also have some missing data as expected from data sets.

# How to run this program

In terminal

``` git clone https://github.com/Mintri1199/Weather_Graph_Generator``` 

Then open the folder in Pycharm then run Make_Graph.py

**Make sure you config your Pycharm settings to include matplotlib in the project interpreter**

In your run console, input **ct_weather.csv** when asked for csv file name.
![alt text](https://github.com/Mintri1199/Weather_Graph_Generator/blob/master/Initial%20startup.png)


When you get to this screen in your run console

![alt text](https://github.com/Mintri1199/Weather_Graph_Generator/blob/master/Region_selection.png)

Simply enter a number that corresponded to a region of your interest and press enter. 
What will happen next is the program will generate a graph visualizing the highs and lows of temperature in the selected region.

![alt text](https://github.com/Mintri1199/Weather_Graph_Generator/blob/master/selected_graph.png)

