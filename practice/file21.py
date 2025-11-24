import csv
from classescont20 import FormatData

def Savedata(filename=" ", datalist= None):
    if datalist is None:
        datalist = []
        
    with open(filename, "w", newline="\n") as csvfile:
        Datawriter = csv.writer(
            csvfile,
            delimiter = ",",
            quotechar = '"',
            quoting = csv.QUOTE_NONNUMERIC)
        Datawriter.writerow(datalist)
        
    print("Data saved")
    
NewData = [FormatData("George", 65, True),
           FormatData("Sally", 47, False),
           FormatData("Doug", 52, True)]

Savedata("TestFile.csv", NewData)

NewDataLists = [item.to_list() for item in NewData]
Savedata("TestFile.csv", NewDataLists)

#reading data
import csv
from file21 import NewData
from file21 import Savedata
def Readdata(filename=""):
    output = []
    with open(filename, "r", newline="") as csvfile:
        Datareader = csv.reader(
            csvfile,
            delimiter=",",
            quotechar='"'
            )
        for item in Datareader:
            output.append(item)
    print("Data read!")
    return output

NewData = Readdata("TestFile.csv")  # read existing data
NewData.append(['Harry', 23, False])
Savedata("TestFile.csv", NewData)
