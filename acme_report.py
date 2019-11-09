import random
from acme import Product
def generate_products(iterations=30):
    products = []
    count = 0
    while count < 30:
        adjective = ['Awesome', 'Shiny', 'Impressive','Portable', 'Improved']
        noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        name = adjective[random.randint(0, len(adjective)-1)] + " " + noun[random.randint(0, len(noun)-1)]
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        prod = Product(name, price, weight, flammability)
        products.append(prod)
        count += 1
    return products

def inventory_report(products):
    names = []
    prices = []
    weights = []
    flammabilities = []
    for i in products:
        names.append(i.name)
        prices.append(i.price)
        weights.append(i.weight)
        flammabilities.append(i.flammability)
    print(f"ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print(f"Unique product names: {len(set(names))}")
    print(f'Average price: {sum(prices)/len(prices)}')
    print(f"Average weight: {sum(weights)/len(weights)}")
    print(f"Average flammability:{sum(flammabilities)/len(flammabilities)}")

if __name__ == '__main__':
    inventory_report(generate_products())
    