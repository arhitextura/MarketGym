from modules.Portofolio import Portofolio


class MarketGym(object):
    def __init__(self, dataset):
        self._dataset = dataset
        self.counter = 0
        self.done = False
        self._cash = 1000
        self._portofolio = Portofolio()

    @property
    def portofolio(self):
        value = self._portofolio.getPortofolio()
        return value

    @property
    def cash(self):
        return self._cash

    def init(self):
        pass

    def step(self, action=None):
        reward = self._cash - 1000
        if(self.counter + 1 < len(self._dataset)):
            self.counter += 1
        else:
            self.done = True
        return (self.cash, reward)

    def reset(self):
        '''
        Description
        -----------
        Resets the counter to 0 
        '''
        self.counter = 0

    def state(self):
        return self._dataset[self.counter]

    def setInitialCash(self, amount):
        self._cash = amount

    def buyAmount(self, amount):
        currentAssetValue = self._dataset[self.counter]
        self._cash = self._cash - (currentAssetValue * amount)
        self._portofolio.addAsset(amount=amount)

    def buyWithCash(self, cash):
        currentAssetValue = self._dataset[self.counter]

    def sellAmount(self, amount):
        currentAssetValue = self._dataset[self.counter]
        self._portofolio.sellAsset(amount=amount)
        self._cash = self._cash + (currentAssetValue * amount)


data = [1, 2, 3, 4, 5, 4, 3, 2, 1]
market_test = MarketGym(data)
market_test.buyAmount(1)

print(market_test.step())
print(market_test.step())

print(market_test.cash)
print(market_test.portofolio)
market_test.sellAmount(1)
print(market_test.cash)
