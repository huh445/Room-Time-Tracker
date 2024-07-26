import csv

class ReadCSV:
    def __init__(self):
        self.csv = csv
    
    def read_csv(self):
        with open("ids.csv", mode="r") as f:
            reader = self.csv.reader(f)
            header = next(reader)
            rows = list(reader)
        
        return rows