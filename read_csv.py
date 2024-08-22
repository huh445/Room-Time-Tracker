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
    
    def save_csv(self, recorded_time):
        with  open("times.csv", mode="a", newline="\n") as f:
            writer = self.csv.DictWriter(f, fieldnames=["name", "room", "times"])
            writer.writerow(recorded_time)