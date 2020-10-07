valid_commands = ["select", "insert", "quit"]
valid_coins = [50, 25, 10, 5]

class Product:
    def __init__(self, name = "", price = 35, recipe = [""]):
        self.name = name
        self.price = price
        self.recipe = recipe
        if self.recipe[0] != 'cup':
            self.recipe.insert(0, 'cup')
        if self.recipe[-1] != 'water':
            self.recipe.append('water')
    
    def getPrice(self):
        return self.price
    
    def make(self):
        print(f"Making {self.name}:")
        for ing in self.recipe:
            print(f"\tDispensing {ing}")

class CashBox:
    def __init__(self, credit = 0, totalReceived = 0):
        self.credit = credit
        self.totalReceived = totalReceived
        pass

    def depost(self, amount = 0):
        pass

    def returnCoins(self):
        pass

    def haveYou(self, amount):
        return self.credit >= amount
    
    def deduct(self, amount):
        pass
    
    def total(self):
        # int
        pass

class Selector:
    def __init__(self):
        self.cash = CashBox()
        black = Product("black", recipe=['coffee'])
        white = Product('white', recipe=['coffee', 'creamer'])
        sweet = Product('sweet', recipe=['coffee', 'sugar'])
        white_sweet = Product('white & sweet', recipe=['coffee', 'sugar', 'creamer'])
        bouillon = Product('bouillon', 25, ['bouillonPowder'])
        self.products = [black, white, sweet, white_sweet, bouillon]
    
    def select(self, choiceIndex = 0):
        pass

class CoffeeMachine:
    def __init__(self):
        self.cash = CashBox()
        self.select = Selector()
    
    def one_action(self):
        pass
    
    def totalCash(self):
        pass


# def main():
#     m = CoffeeMachine()
#     while m.one_action():
#         pass
#     total = m.totalCash()
#     print(f"Total cash: ${total/100:.2f}")