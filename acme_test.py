import unittest
import random
from acme import Product
from acme import BoxingGlove
from acme_report import generate_products
from acme_report import inventory_report

class AcmeProductTests(unittest.TestCase):
    '''Making sure Acme products are the tops'''
    def test_default_product_price(self):
        '''Test default product price being 10.'''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        '''Test default weight product being 20'''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)
    
    def test_methods(self, price=random.randint(5, 100), weight=random.randint(5, 100), flammability=random.uniform(0.0, 2.5)):
        '''I had trouble with this one. I don't know how to assert the value of a print statement.'''
        prod = Product('Test product', price=price, weight=weight, flammability=flammability)
        stealability = price/weight
        if stealability < 0.5:
            self.assertEqual("Not so stealable...")
        if (stealability >= 0.5) & (stealability <= 1):
            print("Kinda stealable.")
        else:
            print("Very stealable!")
            
if __name__ == '__main__':
    unittest.main()