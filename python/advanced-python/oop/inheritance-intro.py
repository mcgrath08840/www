class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        # format needs to be first then % replace.
        return "%.{}f".format(self.places) % self.number




class Currency(Decimal):  # Inherit from Decimal
    def __init__(self, symbol, number, places):
        super().__init__(number, places)  #Call super class and feed variables to it.
        self.symbol = symbol

    def __repr__(self):
        # Use super().__repr__() to call super class display after symbol.
        return "{}{}".format(self.symbol, super().__repr__())




print(Currency('$', 15.6789, 3))
