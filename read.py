# This is the first class of the project
import csv
# Access the file and marked the file so it will help when searching specific data at a specific location
class Read():
    def __init__(self,):
        print("Welcome\nThis is a program that render a line graph of the max and min temperature "
              +"of the given weather csv file")
        self.track = 1 # The key for the dictionary
        self.locations = {} # Dictionary of locations in the csv file
        self.file = input("Please type the csv file name: ")
        self.frmt = self.file.lower().lstrip()

    # checking if the user enter the filename wrong
    def filename_checking(self):
        while True:
            try:
                if self.frmt == 'quit':
                    break

                with open(self.frmt) as f:
                    break
            except:
                self.file = str(input('Please type the file name again\nType quit to end'))
                self.frmt = self.file.lower().lstrip()
    
    # Since ct_weather.csv file have multiple locations, this function will access, count, store 
    # the locations, and then display them to the user so they could choose
    def access(self):
        if self.frmt != 'quit':
            with open(self.frmt) as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    if row[1] in self.locations.values():
                        pass
                    else:
                        self.locations[self.track] =str(row[1])
                        self.track +=1
                for key, value in self.locations.items():
                    print(str(key) + '   '+ value)
        else:
            pass

