import csv

class CleanedPriceData:
    def __init__(self, csv_file):
        self.data_list = self.convert_csv_to_list(csv_file)
        self.price_map = {date:price for date, price in self.data_list}
        self.dates = [date for date, price in self.data_list]

    def convert_csv_to_list(self, csv_file):
        with open(csv_file) as csv_file:
            data_list = list(csv.reader(csv_file))
            # only need date and day's closing price
            data_list = [[data_list[i][0], float(data_list[i][4])] for i in range(len(data_list)-1, 0, -1)]
            return data_list

    def get_data_list(self):
        return self.data_list

    def get_price_map(self):
        return self.price_map

    def get_dates(self):
        return self.dates
