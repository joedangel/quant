from signals.MovingAverageCalculator import MovingAverageCalculator
from CleanedPriceData import CleanedPriceData

class SMATradingSignal:

    def __init__(self, price_map, dates, short_sma, long_sma, long_length):
        self.price_map = price_map
        self.dates = dates
        self.short_sma = short_sma
        self.long_sma = long_sma
        self.long_length = long_length

        ## TEST -------------

        # sma_long_test = sum(self.price_map[date] for date in self.dates[long_length:long_length + long_length])/long_length
        # sma_act_long = self.long_sma[self.dates[long_length+long_length]]

        # print("short: {} act : {}".format(sma_long_test, sma_act_long))

        # print(self.short_sma["04/23/98"])
        # print(self.long_sma["04/23/98"])

        ## END TEST ----------

    def update_action(self, date):
        short_sma = self.short_sma[date]
        long_sma = self.long_sma[date]
        # print(short_sma, long_sma)
        if short_sma < long_sma:
            self.own = False
        else:
            self.own = True

    def calculate_return(self):
        num_dollars = 1000
        num_shares = 0
        self.own = False
        last_date = None
        start_price = None
        num_days = -1

        for date in self.dates[self.long_length:num_days]:
            if start_price == None:
                start_price = self.price_map[date]
            if self.own:
                if num_shares == 0:
                    num_shares = num_dollars / self.price_map[date]
                    num_dollars = 0
                    # print("{} bought: {}".format(date, num_shares))
            else:
                if num_dollars == 0:
                    num_dollars = num_shares * self.price_map[date]
                    num_shares = 0
                    # print("{} sold: {}".format(date, num_dollars))
            self.update_action(date)
            last_date = date

        print("d: {}".format(num_dollars))
        print("s: {} p: {} *: {}".format(num_shares, self.price_map[last_date], num_shares * self.price_map[last_date] ))
        print("e ret: {}".format(self.price_map[last_date] /start_price))

test_data = [(5, 10), (100, 2000)]

for short, long_ in test_data:
    cleaned_data = CleanedPriceData("sp500_prices_1978_2022.csv")
    price_map = cleaned_data.get_price_map()
    dates = cleaned_data.get_dates()
    sma_calculator = MovingAverageCalculator(cleaned_data.get_data_list())
    short_sma = sma_calculator.get_moving_average(short)
    long_sma = sma_calculator.get_moving_average(long_)

    sma_signal = SMATradingSignal(price_map, dates, short_sma, long_sma, long_)
    sma_signal.calculate_return()