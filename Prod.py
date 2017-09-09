class Product(object):
    def __init__(self, price, itemName, weight, brand, costs, status= "for sale"):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.costs = costs
        self.status = status

    def Sell(self):
        if (self.status.lower() == "sold"):
            raise Exception("Sold product that is already marked as 'sold'.")
        else:
            self.status = "sold"
        return self

        #takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def AddTax(self, taxDecimal ):
        return self.price + (self.price * taxDecimal)

    def Return(self, isBoxOpened, defectReason):
        if defectReason == "defective":
            self.price = 0
            self.status = "defective"
        elif not isBoxOpened:
            self.status = "for sale"
        else:
            self.price *= 0.8
            self.status = "box opened"
        return self

    def DisplayInfo(self):
        print "{}, Price ${}, Weight {}lbs, Brand {}, Cost ${}, Status: {}".format(self.itemName, self.price, self.weight, self.brand, self.costs, self.status)
        return self

    def __str__(self):
        return "{}, Price ${}, Weight {}lbs, Brand {}, Cost ${}, Status: {}".format(self.itemName, self.price, self.weight, self.brand, self.costs, self.status)
