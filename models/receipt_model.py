class Item:
    def __init__(self, shortDescription, price):
        self.shortDescription = shortDescription
        self.price = price


class Receipt:
    def __init__(self, retailer, purchaseDate, purchaseTime, total, items):
        self.retailer = retailer
        self.purchaseDate = purchaseDate
        self.purchaseTime = purchaseTime
        self.total = total
        self.items = [Item(**item) for item in items]
