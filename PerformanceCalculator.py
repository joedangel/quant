from CleanedPriceData import CleanedPriceData
from signals.RSICalculator import RSICalculator
from PurchaseDecider import PurchaseDecider

class PerformanceCalculator:

    def __init__(self, price_map, dates, calculator, purchase_decider):
        self.price_map = price_map
        self.dates = dates
        self.calculator = calculator
        self.purchase_decider = purchase_decider
        self.signal_date_map = self.calculator.compute()

        self.first_date_valid_signal = 14

    def update_action(self, value1, value2):
        self.own = self.purchase_decider.should_buy(value1, value2)

    def calculate_return(self):
        num_dollars = 1000
        num_shares = 0
        self.own = False
        last_date = None
        start_price = None
        num_days = -1

        for date in self.dates[self.first_date_valid_signal:num_days]:
            if start_price == None:
                start_price = self.price_map[date]
            if self.own:
                if num_shares == 0:
                    num_shares = num_dollars / self.price_map[date]
                    num_dollars = 0
            else:
                if num_dollars == 0:
                    num_dollars = num_shares * self.price_map[date]
                    num_shares = 0
            value1 = self.signal_date_map[date]
            # for rsi
            value2 = 30
            self.update_action(value1, value2)
            last_date = date

        print("signal - dollar val:", num_dollars)
        print("signal - share val:", num_shares * self.price_map[last_date])
        print("hold - dollar val:", self.price_map[last_date] / start_price * 1000)


cleaned_data = CleanedPriceData("sp500_prices_1978_2022.csv")
price_map = cleaned_data.get_price_map()
dates = cleaned_data.get_dates()

# RSI
rsi_calculator = RSICalculator(cleaned_data.get_data_list())
decider = PurchaseDecider()

sma_signal = PerformanceCalculator(price_map, dates, rsi_calculator, decider)
sma_signal.calculate_return()