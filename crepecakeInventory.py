# A class works with the chain stores that sell crepe cakes in the DMV area
# contains 5 attributes: flavor, price, availableStore, size, and avePricePerSqInch
# contains 6 methods (including the constructor):
# __init__, addStore, getFlavor, getPrice, getSize, getAveragePricePerSqInch

import math

class CrepeCake:
    #the constructor initializes 5 attributes
    def __init__(self, flavor):
        self.cakeFlavor = flavor
        self.price = 0
        self.availableStore = []
        self.size = 0
        self.avePricePerSqInch = 0

    # addRegion is for adding each available store
    # It will append the input to the growing availableRegion
    def addStore(self, store):
        self.availableStore.append(store)

    # getFlavor returns the cake's flavor
    def getFlavor(self):
        return self.cakeFlavor

    # getPrice returns the cake's price
    def getPrice(self):
        return self.price

    # getSize returns the cake's diameter, measured in inches
    def getSize(self):
        return self.size

    # getAveragePricePerSqInch returns the cake's
    # average price per square inch
    def getAveragePricePerSqInch(self):
        area = (1/4)*math.pi*(self.getSize()**2)
        self.avePricePerSqInch = self.getPrice() / area
        return self.avePricePerSqInch

# main prints out a welcome message to user and then
# asks for the number of cakes (numCake). It then loops
# through the specified number of times (based on
# numCake), at each iteration asking for a cake flavor,
# using that flavor to create a cake object,then asking
# for the number of stores serving this cake (numRegions),
# then calling the summarizeAllRegions function
# (passing the cake object and numRegions as argument),
# and then calling the calculateAvePrice function
# (passing the cake object as argument). It will collect the
# return values from summarizeAllRegions and calculateAvePrice
# and output the list of stores and the price per square inch.
def main():
    print("Welcome to the our Crepe Cake Store's Inventory Database!")
    numCake = eval(input("Please enter the number of cake you would like to import: "))
    cakeList = []
    print()

    for i in range(numCake):
        flavor = input("Please enter the flavor of no." + str(i+1) + " cake: ")
        numRegions = eval(input("Please enter the number of stores that serve this cake: "))
        cake = CrepeCake(flavor)
        cakeList.append(cake)
        regions = summarizeAllRegions(cake, numRegions)
        print("The list of available store serving this cake is:")
        print(regions)
        print()
        averagePrice = round(calculateAvePrice(cake), 2)
        print("The price per square inch for this cake is: " + str(averagePrice) + " dollars per square inch")
        print()

    print("The current inventory cake list is:")
    for i in range(len(cakeList)):
        print(cakeList[i].getFlavor())

# summarizeAllRegions takes two parameters: a CrepeCake object
# and the number of available stores. It calculates for you how
# many of the Maryland stores and how many Virginia stores sell
# the cake of this flavor, and whether the Washington DC store
# sells it. It will return the full list of stores selling this cake.
def summarizeAllRegions(thisCake, regionNumber):
    numMaryland = 0
    numVirginia = 0
    whetherInDC = False
    marylandCounty = ["Calvert", "Charles", "Frederick", "Montgomery", "Prince George"]
    virginiaCounty = ["Alexandria", "Arlington", "Clarke", "Culpeper", "Fairfax", "Falls Church",
    "Fauquier", "Fredericksburg", "Loudoun", "Manassas", "Manassas Park", "Prince William",
    "Rappahannock", "Spotsylvania", "Stafford", "Warren"]
    for i in range(regionNumber):
        thisRegion = input("Please enter no. " + str(i+1) + " store that sells this cake: ")
        thisCake.addStore(thisRegion)
        if thisRegion in marylandCounty:
            numMaryland += 1
        elif thisRegion in virginiaCounty:
            numVirginia += 1

    if "Washington" in thisCake.availableStore:
        whetherInDC = True

    print("There are " + str(numMaryland) + " stores in Maryland serving " + thisCake.getFlavor() + " cake.")
    print("There are " + str(numVirginia) + " stores in Virginia serving " + thisCake.getFlavor() + " cake.")
    if whetherInDC == True:
        print("The Washington D.C. store is also serving this cake.")

    return thisCake.availableStore

# calculateAvePrice takes one parameter: a CrepeCake object.
# It collects the price and size (diamter) of the object.
# Then it returns the cake's price per square inch. But it
# does not calculate average price here, it will be making calls
# to CrepeCake's getAveragePricePerSqInch method to do the work.
def calculateAvePrice(thisCake):
    thisCake.price = eval(input("Please enter the price of this cake: "))
    thisCake.size = eval(input("Please enter the size (diameter) of this cake, in inches: "))
    avePrice = thisCake.getAveragePricePerSqInch()

    return avePrice

main()
