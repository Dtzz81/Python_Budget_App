#Complete the Category class in budget.py. 
#different budget categories like food, clothing,
#objects are created, passed in category name. 
#The class have an instance variable called ledger 
#that is a list. 

class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []
        self.budget = 0
#A deposit method that accepts an amount and description. 
#If no description is given, it should default to an empty string. 
#The method append an object to the ledger
#the form {"amount": amount, "description": description}.

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description":description})
        self.budget += amount
 
 #A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the budget of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else: 
            return False
        
#A withdraw method that is similar to the deposit method, 
#but the amount stored in the ledger as a negative number. 
#¡¡ If there are not enough funds, nothing should be added to the ledger.
#¡¡ This method  return True if the withdrawal took place,  False otherwise.
    
    def withdraw(self, amount: float, description=""):
        if self.check_funds(amount):
            
            self.ledger.append({"amount": - amount, "description":description})
            self.budget -= amount
            return True
        else:
            return False
        
        
#A get_budget method that returns the current budget 
#of the budget category based on the deposits and withdrawals 
    
    def set_balance(self, amount):
        self.budget = amount
    
    def get_balance(self):
        return self.budget


#A transfer method that accepts an amount 
#and another budget category as arguments. 
#add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
#add a deposit to the other budget category with the amount 
#and the description "Transfer from [Source Budget Category]". 
#This method should return True if the transfer took place, 
#and False otherwise.
    def transfer(self, amount, category_budget):
        if self.check_funds(amount) == True:
            self.withdraw(amount, f"Transfer to {category_budget.category_name}")
            category_budget.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False
        
        
# second part - how the print should look:
    def __str__(self):
        
        
        title_line = self.category_name.center(30, "*") + "\n"
    
        layout = title_line
        
        for i in self.ledger:
            
            all_items = f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
            layout += all_items
        
        category_total = f"Total: {format(self.get_balance(), '.2f')}"
       
        layout += category_total 
        return layout
   
    #third part - graph

def create_spend_chart(categories):
    category_names = []
    spent = []
    total_expenditure = []

    for category in categories: 
        total = 0
        for i in category.ledger:
            if i['amount'] < 0:
                total -= i['amount']
        spent.append(round(total, 2))
        category_names.append(category.category_name)

    for percents in spent:
        total_expenditure.append(round(percents/sum(spent), 2)*100)

    graph_layout = "Percentage spent by category\n"

    lines = range(100,-10,-10)
# from internet, similar to first project
# go through it again later!!

    for line_names in lines: 
        graph_layout += str(line_names).rjust(3) + "| "
        for percents in total_expenditure:
            if percents >= line_names:
                graph_layout += "o  "
            else:
                graph_layout += "   "
        graph_layout += "\n"
                                                
    graph_layout += "    ----" + ("---" * (len(category_names) - 1))
    graph_layout += "\n     "

    len_longest = 0
    
    for names in category_names:
        if len_longest < len(names):
            len_longest = len(names)

    for i in range(len_longest): 
        for names in category_names:
            if len(names) > i:
                graph_layout += names[i] + "  "
            else:
                graph_layout += "   "
        if i < len_longest - 1:
            graph_layout += "\n     "

    return graph_layout
