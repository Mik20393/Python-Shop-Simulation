import csv

#Class to hold name,price and quantity information for an item
class ItemAndQty:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


#__repr__ function to return ItemAndQty object as a string
    def __repr__(self):
         return str({"Item Name": self.name, "Price": self.price, "Quantity": self.quantity})


#function to return the total cost of a number of items       
    def cost(self):
        return self.price * self.quantity


#Shop class containing a dictionary of ItemAndQty objects 
class Shop:
    def __init__(self):
        self.inventory = {}


#Function to create new items in the inventory or update the quantity of items already in stock
    def addItemAndQty(self, name, price, quantity):
        if name not in self.inventory.keys():
            self.inventory[name] = ItemAndQty(name, price, quantity)
        else:
            self.inventory[name].quantity += quantity
        

#Function to load items into the inventory from a csv file
    def loadCSV(self, fileName):
        
        with open(fileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile)
            next(csvReader, None)
            for row in csvReader:
                
                self.addItemAndQty((str(row[0])), (float(row[1])), (int(row[2])))

        return self.inventory


#Function that returns item name, price and quantity given the item name
    def itemAndQtyByName(self, name):
        
        #Check item exists in shop inventory
        if name in self.inventory.keys():
            
            #Return item name, price and quantity
            return self.inventory[name]
        
        else:
            return None


#Fucntion that returns quantity of items avilable in the Shop given the item name
    def itemsInStock(self, name):
        
        #Check item exists in shop by calling the itemAndQtyByName function
        if self.itemAndQtyByName(name):
            
            #Return quantity of item if it exists
            return self.inventory[name].quantity
        
        else:
            return 0
        

#Shopping basket class that adds item objects to a dictionary 
class ShoppingBasket:
    def __init__(self, Shop):
        self.Shop = Shop
        self.basket = {} 


#Function to add items to the shopping basket 
    def addItemAndQty(self, name, quantityRequest):
    
    #Check the item exists in the shop
        if name in self.Shop.inventory.keys():
            
            price = self.Shop.inventory[name].price
            quantityAvailable = self.Shop.inventory[name].quantity
            
            #Check the quantity asked for is available
            if quantityAvailable  >= quantityRequest:
                
                #Create new ItemAndQty object and add to basket
                self.basket[name] = ItemAndQty(name, price, quantityRequest)

                #Reduce the quantity in the shop by the quantity requested
                quantityAvailable -= quantityRequest
                self.Shop.inventory[name] = ItemAndQty(name, price, quantityAvailable)

                #Return number of items added to basket
                return (str(quantityRequest) + " items added to basket")

            else:
                print("Only " + str(quantityAvailable) + " in stock")    


        else:
            return None


#Function to return the total price of all items in basket
    def totalCost(self):
        
        #Loop through items in the basket
        for i in self.basket.keys():
            
            #Local variables for name price and quantity of item
            name = self.basket[i].name
            price = self.basket[i].price
            quantity = self.basket[i].quantity
            
            #Create ItemAndQty objects and call the cost function from class
            total = 0
            total += ItemAndQty(name, price, quantity).cost()
            
            return ("Total cost of items " + str(total))
                        

#Function to clear the contents of the basket dictionary
    def empty(self):
        self.basket.clear()
              

if __name__ == "__main__":
   
    print("Answer for q1, q2 and q3")
    print("========================")
    item = ItemAndQty("Jeans", 95.0, 12)
    print(item)
    print(item.cost())
    print("=========================")

    print("Answer for q4, q5, and q6")
    print("=========================")
    shop = Shop()
    shop.addItemAndQty(item.name, item.price, item.quantity)
    print(shop.inventory) 
    shop.loadCSV("Inventory.csv")
    print(shop.inventory)
    print("========================")

    print("Anwer for q7")
    print("=========================")
    print(shop.itemAndQtyByName("Jeans"))
    print(shop.itemAndQtyByName("Socks"))
    print("=========================")

    print("Answer for q8")
    print("=========================")
    print(shop.itemsInStock("Jacket"))
    print(shop.itemsInStock("Socks"))
    print("=========================")

    print("Answer to q9 and 10")
    print("=========================")
    shopping = ShoppingBasket(shop)
    print("Inventory before")
    print(shop.inventory)
    print("=========================")
    print(shopping.addItemAndQty("Jeans", 2))
    print(shopping.basket)
    print("=========================")
    print("Inventory after")
    print(shop.inventory)
    
    print("Answer to q 11 and 12")
    print("=========================")
    print(shopping.totalCost())
    shopping.empty()
    print(shopping.basket)
    
    
    
   
    
    
    
    
   
    
   
