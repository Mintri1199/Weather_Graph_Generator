# This is the second class of the project
from read import Read
import csv
from datetime import datetime

# This class will allow the user to choose the desired location and retrieve data from that location only

class Processing(Read):
    def __init__(self):
        self.errorhighs = [] # Both error lists will get the index of missing data so it will be graph later
        self.errorlows = []
        self.chose =''
        self.revise_choice = ''
        self.highs = [] # Both highs and lows lists will contain raw data from the csv file
        self.lows = []
        self.dates = []
        self.final_highs = [] # Both final lists will contain formatted raw data to be use when graphing
        self.final_lows = []
        super().__init__()

    # Take user input to select a specific locations of the file while also allowing them to quit
    def Choosing(self):
        self.chose = input("Please enter the number associated with the location you want to see:")
        self.revise_choice = self.chose
        while True:
            try:
                if str(self.revise_choice.lower().lstrip()) == 'quit':
                    break
                if int(self.revise_choice) <=21:
                    if int(self.revise_choice) <=0:
                        print("What you've entered was not found on the list!")
                        self.revise_choice = input("Please enter the number again\nEnter quit to end:")
                    break
                else:
                    break
            except ValueError:
                print("What you've entered was not a number!")
                self.revise_choice = input("Please enter the number again\nEnter quit to end:")
        self.chose = self.revise_choice

    # Get raw data from selected location
    def get_data(self):
        with open(self.file) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if str(row[1])== self.locations[int(self.chose)]:
                    date = datetime.strptime(row[2],'%Y-%m-%d')
                    self.dates.append(date)

                    high = row[4]
                    self.highs.append(high)

                    low = row[5]
                    self.lows.append(low)

                    
    def formatting_numbers(self):
        x = 0
        y = 0
        # Because the ct_weather csv file has strings instead of numerical values and missing data
        # This function will convert these strings to int and store the indexes of missing data
        for i, item in enumerate(self.highs):
            try:
                x_revise = self.highs[x]
                self.final_highs.append(int(x_revise))
                x +=1
            except ValueError:
                self.final_highs.append(0)
                self.errorhighs.append(i)
                x += 1

        for i, item in enumerate(self.lows):
            try:
                y_revise = self.lows[y]
                self.final_lows.append(int(y_revise))
                y += 1
            except ValueError:
                self.final_lows.append(0)
                self.errorlows.append(i)
                y += 1


