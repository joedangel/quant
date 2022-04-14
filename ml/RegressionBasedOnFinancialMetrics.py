from sklearn import linear_model
from data.DataImport import DataImport

class RegressionBaseOnFinancialMetrics:
    def __init__(self):
        data = DataImport()
        self.X = data.getMetrics()
        self.y = data.getPrices()

    def calculate(self):
        self.reg = linear_model.LinearRegression()
        self.reg.fit(self.X, self.y)

    def coefs(self):
        return (self.reg.coef_, self.reg.intercept_)

    def score(self):
        return self.reg.score(self.X, self.y)

model = RegressionBaseOnFinancialMetrics()
model.calculate()
print("coefs:", model.coefs())
print("score:", model.score())