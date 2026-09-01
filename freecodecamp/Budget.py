class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name
    def __str__(self):
        title = f"{self.name:*^30}\n"
        concept = ""
        for dic in self.ledger:
            note = dic['description'][:23]
            amount = f"{dic['amount']:.2f}"[:7]
            concept += f"{note:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance()}"
        return title + concept + total
    def deposit(self, amount: float, dscrp=''):
        self.ledger.append({"amount": amount, "description": dscrp})
        
    def withdraw(self, amount: float, dscrp=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": dscrp})
            return True
        return False

    def get_balance(self):
        return sum(dic['amount'] for dic in self.ledger)

    def transfer(self, amount: float, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False 

    def check_funds(self, amount: float):
        return amount <= self.get_balance()
def create_spend_chart(categories):
    title = 'Percentage spent by category\n'
    totals = []
    tall = 0
    num = len(categories)
    for cat in categories:
        total = 0
        for led in cat.ledger:
             total -= led['amount'] if led['amount'] < 0 else 0
        totals += [total]
        tall = max(tall, len(cat.name))
    utter = sum(totals)
    rows = [i for i in range(10,-1,-1)]
    colms = [i for i in range(num)]
    presents = []
    for c in colms:
        presents += [round((totals[c]/utter)*10)*10]
    concept = ""
    for r in rows:
        per = r*10
        concept += f"{per:>3}| "
        for c in colms:
            concept += "o  " if presents[c] >= per else "   "
        concept += '\n'
    btm = f"    {'-'*len(categories)*3}-\n"
    for l in range(tall):
        btm += "    "
        for c in colms:
            btm += f" {categories[c].name[l]} " if l < len(categories[c].name) else "   "
        btm += ' \n' if l != tall-1 else ' ' 
    return title + concept + btm
'''
food = Category('Food') 
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries') 
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
'''
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([food, entertainment, business]))      