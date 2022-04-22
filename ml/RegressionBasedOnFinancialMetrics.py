from sklearn import linear_model
from sklearn.neural_network import MLPRegressor
from data.DataImport import DataImport

class RegressionBaseOnFinancialMetrics:
    def __init__(self):
        data = DataImport()
        self.X = data.getMetrics()
        self.y = data.getPrices()

    def calculateLinearRegression(self):
        self.reg = linear_model.LinearRegression()
        self.reg.fit(self.X, self.y)

    def coefsLinearRegression(self):
        return (self.reg.coef_, self.reg.intercept_)

    def scoreLinearRegression(self):
        return self.reg.score(self.X, self.y)

    def predictLinearRegression(self):
        return self.reg.predict([self.X[0]])

    def calculateNeuralNetwork(self):
        self.nn = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5), random_state=1)
        self.nn.fit(self.X, self.y)

    def coefsNeuralNetwork(self):
        return self.nn.coefs_

    def scoreNeuralNetwork(self):
        return self.nn.score(self.X, self.y)

    def predictNeuralNetwork(self):
        return self.nn.predict([self.X[0]])

model = RegressionBaseOnFinancialMetrics()
model.calculateLinearRegression()
print("LinearRegression:")
print("coefs:", model.coefsLinearRegression())
print("score:", model.scoreLinearRegression())
print("predict:", model.predictLinearRegression())
model.calculateNeuralNetwork()
print("NeuralNetwork:")
print("coefs:", model.coefsNeuralNetwork())
print("score:", model.scoreNeuralNetwork())
print("predict:", model.predictNeuralNetwork())
