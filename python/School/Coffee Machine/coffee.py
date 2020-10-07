valid_commands = ["select", "insert"]
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
    def __init__(self, totalReceived = 0):
        self.credit = 0
        self.totalReceived = totalReceived

    def deposit(self, amount = 0):
        self.credit += amount
        print(f"Depositing {amount} cents. You have {self.credit} cents credit.")

    def returnCoins(self):
        print(f"Returning {self.credit} cents")
        self.credit = 0

    def haveYou(self, amount):
        return self.credit >= amount
    
    def deduct(self, amount):
        self.credit -= amount
        self.totalReceived += amount
    
    def total(self):
        return self.totalReceived

class Selector:
    def __init__(self, cashbox):
        self.cash = cashbox
        black = Product("black", recipe=['coffee'])
        white = Product('white', recipe=['coffee', 'creamer'])
        sweet = Product('sweet', recipe=['coffee', 'sugar'])
        white_sweet = Product('white & sweet', recipe=['coffee', 'sugar', 'creamer'])
        bouillon = Product('bouillon', 25, ['bouillonPowder'])
        self.products = [black, white, sweet, white_sweet, bouillon]
        self.product_string = ""
        for i in range(len(self.products)):
            self.product_string += (f"{i+1}={self.products[i].name}, ")
    
    def select(self, choiceIndex = 0):
        if self.cash.haveYou(self.products[choiceIndex].price):
            self.products[choiceIndex].make()
            self.cash.deduct(self.products[choiceIndex].price)
            self.cash.returnCoins()
            return
        else:
            print(f"Sorry. Not enough money deposited.")
            return

class CoffeeMachine:
    def __init__(self):
        self.cash = CashBox()
        self.selector = Selector(self.cash)
    
    def one_action(self):
        print(f"PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print(self.selector.product_string)
        print(f"Sample commands: insert 25, select 1")
        user_input = input("Your command: ").strip().lower()
        if user_input == 'quit':
            return False
        user_input = user_input.split(' ')
        try:
            user_input[1] = int(user_input[1])
        except:
            print("Invalid command.")
            return True
        if user_input[0] == 'insert':
            if user_input[1] not in valid_coins:
                print("INVALID AMOUNT")
                print("We only take half-dollars, quarters, dimes, and nickels.")
                return True
            self.cash.deposit(user_input[1])
        elif user_input[0] == 'select':
            self.selector.select(user_input[1])
        else:
            print("Invalid command.")
        return True
    
    def totalCash(self):
        return self.cash.totalReceived

def main():
    m = CoffeeMachine()
    while m.one_action():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}")

if __name__ == "__main__":
    main()