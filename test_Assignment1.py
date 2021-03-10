import unittest
import Assignment1
from Assignment1 import Shop
from Assignment1 import ShoppingBasket

class Test_Shop(unittest.TestCase):
    def test_loadCSV(self):
        shop = Shop()
        self.assertEqual({"Jeans": ["Jeans", 95, 20], 
                          "Jacket": ["Jacket", 100, 10], 
                          "T-shirt": ["T-shirt", 25, 50], 
                          "Jumper": ["Jumper", 55, 15]}, shop.loadCSV("Inventory.csv"))


    def test_itemsInStock(self):
        
        shop = Shop()
        shop.addItemAndQty("Jeans", 95, 20)
        self.assertEqual(20, shop.itemsInStock("Jeans"))
        self.assertEqual(0, shop.itemsInStock("Jacket"))

class Test_ShoppingBasket(unittest.TestCase):
    
    def test_addItemAndQty(self):

        shop = Shop()
        shop.addItemAndQty("Jeans", 95, 20)
        shop.addItemAndQty("Jacket", 100, 10)
        shop.addItemAndQty("Jumper", 55, 20)
        shop.addItemAndQty("T-shirt", 25, 50)

        bag = ShoppingBasket(shop)
        self.assertEqual("2 items added to basket", bag.addItemAndQty("Jeans", 2))

    def test_totalCost(self):

        shop = Shop()
        shop.addItemAndQty("Jeans", 95, 20)
        shop.addItemAndQty("Jacket", 100, 10)
        shop.addItemAndQty("Jumper", 55, 20)
        shop.addItemAndQty("T-shirt", 25, 50)

        bag = ShoppingBasket(shop)
        bag.addItemAndQty("Jeans", 2)
        self.assertEqual(190, bag.totalCost())

    def test_itemsInStock(self):

        shop = Shop()
        shop.addItemAndQty("Jeans", 95, 20)
        shop.addItemAndQty("Jacket", 100, 10)
        shop.addItemAndQty("Jumper", 55, 20)
        shop.addItemAndQty("T-shirt", 25, 50)

        bag = ShoppingBasket(shop)
        bag.addItemAndQty("Jeans", 2)
        self.assertEqual(18, shop.inventory["Jeans"].quantity)


if __name__ == "__main__":
    unittest.main()