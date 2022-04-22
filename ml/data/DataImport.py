import csv

class DataImport:
    def __init__(self):
        self.csv = '/Users/joedangelewicz/git/quant/ml/data/FB_price_pe_ps_pfcf_data.csv'
        self.createData()

    def createData(self):
        self.output = []
        with open(self.csv) as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            for line in csv_file:
                line = line[:len(line)-2]
                lst = line.split(',')
                self.output.append(lst)

    def getPrices(self):
        return [float(row[1]) for row in self.output]

    def getMetrics(self):
        return [[float(x) for x in row[2:5]] for row in self.output]
