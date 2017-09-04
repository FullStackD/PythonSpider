from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode("ascii", 'ignore')
dataFile = StringIO(data)
dictReader = csv.DictReader(dataFile)
print(dictReader.fieldnames)
# csvReader = csv.reader(dataFile)

for row in dictReader:
    # print("The album \"" + row[0] + "\" was released in " + str(row[1]))
    print(row)
