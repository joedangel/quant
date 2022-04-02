class PurchaseDecider:

    def __init__(self):
        pass

    def should_buy(self, a, b):
        if a > b:
            return True
        return False