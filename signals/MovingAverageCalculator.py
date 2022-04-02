class MovingAverageCalculator:

    def __init__(self, cleaned_data):
        self.cleaned_data = cleaned_data

    def get_moving_average(self, length):
        sma_map = {}
        for i in range(length, len(self.cleaned_data)):
            sma = sum(price for date,price in self.cleaned_data[i-length:i])/length
            sma_map[self.cleaned_data[i][0]] = sma
        return sma_map

