class ShoppingCart:
    def __init__(self):
        self.items = ["Apple", "Banana", "Milk"] 
        
    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

cart = ShoppingCart()

print(cart[1])      
cart[1] = "Mango"  
print(cart[1])      