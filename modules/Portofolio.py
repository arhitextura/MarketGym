

class Portofolio():
    '''
    TODO: Implement portoflio buy by amount or by cash
    '''
    def __init__(self) :
        self.portofolio = {}

    def __get__(self, obj, objtype=None):
        return obj.portofolio


    def addAsset(self, amount, symbol = "BTC"):
        if symbol not in self.portofolio:
            self.portofolio[symbol] = amount
        else:
            self.portofolio[symbol] += amount

    def sellAsset(self, amount,  symbol = "BTC"):
        if symbol not in self.portofolio:
            raise AssertionError(f"you dont have any {symbol} in portofolio")
        else:
            self.portofolio[symbol] -= amount

    def getPortofolio(self):
        return self.portofolio
    
    def reset(self):
        self.portofolio = {}