from Prod import Product


class Store:
    def __init__(self, location, owner):
         self.products = []
         self.location = location
         self.owner = owner

    def add_product(self, aProduct):
        print "Adding product {} to our inventory.".format(aProduct.itemName)
        self.products.append(aProduct)
        return self
    def remove_product(self, aProductName):
        for thisItem in self.products:
            if (thisItem.itemName == aProductName):
                print "Removing this product:", thisItem.DisplayInfo()
                self.products.remove(thisItem)
                return self
        print "Product '{}' not found in the inventory.".format(aProductName)
        return self
    def inventory(self):
        print "__" * 10, "Store Inventory", "__" * 10
        print "Location: {}    Owner: {}".format(self.location, self.owner)
        for num in self.products:
                print "   -", num
        print "__" * 8, " End Store Inventory", "__" * 8
        print " "
        return self

gum = Product(15, "Bazooka gum", 0, "Bazooka", 10, "for sale")
degree = Product(800000, "college Education", 0, "MIT", 700000)



Freddies = Store("Bellevue", "Fredwin J Meyer III")
Freddies.inventory()

Freddies.add_product(gum)
Freddies.add_product(degree)

Freddies.inventory()
Freddies.remove_product("Bazooka gum")
Freddies.inventory()
