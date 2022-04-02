from signals.BaseCalculator import BaseCalculator

class RSICalculator(BaseCalculator):

    def __init__(self, cleaned_data):
        # cleaned_data = x by 2 array; date, price
        self.cleaned_data = cleaned_data

    def daily_return(self, day1_price, day2_price):
        return (day2_price - day1_price) / day1_price

    def total_positive_return(self, days):
        return sum(self.daily_return(days[day][1], days[day+1][1]) if self.daily_return(days[day][1], days[day+1][1]) >= 0 else 0 for day in range(len(days)-1))

    def total_negative_return(self, days):
        total = sum(abs(self.daily_return(days[day][1], days[day+1][1])) if self.daily_return(days[day][1], days[day+1][1]) < 0 else 0 for day in range(len(days)-1))
        # avoid dividing by 0
        if total == 0:
            return 0.001
        return total

    def compute(self):
        days_in_window = 14
        rsi_map = {}
        length = len(self.cleaned_data)
        for i in range(days_in_window, length):
            total_positive = self.total_positive_return(self.cleaned_data[i-days_in_window:i])
            total_negative = self.total_negative_return(self.cleaned_data[i-days_in_window:i])
            rsi = 100 - (100 / (1 + total_positive / total_negative))
            rsi_map[self.cleaned_data[i][0]] = rsi
        return rsi_map
