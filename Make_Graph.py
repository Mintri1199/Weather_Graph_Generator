# The final class for this project
from Process import Processing
from matplotlib import pyplot as p

# This class will use the formatted values from Processing to generate a line graph
class Visualizing(Processing):
    def __init__(self):
        super(). __init__()
   
    def LABELING(self):
        fig = p.figure(dpi=128,figsize=(10,6))
        title = 'Highs and Lows Weather Report in ' + self.locations[int(self.chose)]
        p.title(title, fontsize = 26)
        fig.autofmt_xdate()
        p.xlabel('', fontsize = 15)
        p.ylabel("Temperature(F)" , fontsize = 15)
        p.tick_params(axis='both', which="major", labelsize=15)

    def PLOTTING(self):

        p.plot(self.dates, self.final_highs , c = 'red' , alpha = 0.5)
        p.plot(self.dates,self.final_lows, c = 'blue', alpha = 0.5)
        p.fill_between(self.dates,self.final_highs,self.final_lows, facecolor = 'blue' , alpha = 0.1)

        for i in self.errorhighs:
            p.scatter(self.dates[i], self.final_highs[i] , c = 'red' )
        for i in self.errorlows:
            p.scatter(self.dates[i],self.final_lows[i], c = 'blue')
        p.show()
