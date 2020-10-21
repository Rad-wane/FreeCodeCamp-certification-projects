# -*- coding: utf-8 -*-
"""
Dev. by : AIT OUHANI Radwane

FreeCodeCamp 3rd project.

Prupose : 
The Category class to instantiate objects based on different budget categories
 like food, clothing, and entertainment. When objects are created, they are passed in the 
 name of the category. The class have an instance variable called 
 ledger that is a list. The class also contain the following methods:

     * A deposit method that accepts an amount and description. If no description is
         given, it should default to an empty string. 
     * A withdraw method that is similar to the deposit method, but the amount passed 
         in should be stored in the ledger as a negative number. If there are not enough funds,
         nothing should be added to the ledger. 
     * A get_balance method that returns the current balance of the budget category based 
         on the deposits and withdrawals that have occurred.
     * A transfer method that accepts an amount and another budget category as arguments.
         The method should add a withdrawal with the amount and the description "Transfer to
         [Destination Budget Category]". The method should then add a deposit to the other
         budget category with the amount and the description "Transfer from [Source Budget 
         Category]". If there are not enough funds, nothing should be added to either ledgers.
         This method should return True if the transfer took place, and False otherwise.
     * A check_funds method that accepts an amount as an argument. It returns False if
         the amount is less than the balance of the budget category and returns True otherwise.
         This method should be used by both the withdraw method and transfer method.



When the budget object is printed, here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96


Besides the Category class,  a function called create_spend_chart that takes a list of
categories as an argument. It should return a bar chart.

The chart show the percentage spent in each category passed in to the 
function. The percentage spent is calculated only with withdrawals and 
not with deposits.This function is to set up to four categories.

When the function is called, here is an example of the output:

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
"""

class Category:
    def __init__(self,budget_categories):
        self.budget_categories=budget_categories
        self.ledger=[]
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self,amount, description=""):
        if self.check_funds(amount)==True:
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self,amount, a_budg_cat):
        if self.check_funds(amount)==True:
            self.withdraw(amount, "Transfer to "+ a_budg_cat.budget_categories)
            a_budg_cat.deposit(amount,"Transfer from "+ self.budget_categories)
            return True
        else: 
            return False
    def check_funds(self,amount):
        if self.get_balance()<amount:
            return False
        else:
            return True
        
    def __str__(self):
        output = self.budget_categories.center(30,"*")+"\n"
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
        output += f"Total: {format(self.get_balance(), '.2f')}"
        return output


        
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)
list_cat=[food,clothing,auto]
def create_spend_chart(list_cat):
    if len(list_cat)>4: return False
    def round_down (a,b):
        return a-a%b
    
    
    
    #Calculating %
    spent=[]
    percent =[]
    for cat in list_cat:
        total=0
        for item in cat.ledger:
            if item['amount']<0:
                total+=item['amount']
        spent.append(round(total, 2))
        
    for i in spent:
        tmp = (i/sum(spent))*100
        r_tmp=round_down(tmp, 10)
        percent.append(r_tmp)
       
    ##creating the output 
        #Creating the bars
    output="Percentage spent by category\n"
    label = range(100,-1,-10)
    n=0
    for i in label:
        add = n*" o " +"\n"
        if i  in percent:
            n+=1
            add = n*" o " +"\n"
            output+= str(i).rjust(3) +"|" +add
        else:
            output+= str(i).rjust(3) +"|" +add
        
        
        #creating the line
    for i in range(len(output.split("\n"))-1):
        nb_line=len(output.split("\n")[i])
    output+=(nb_line+1)*"-"    
        #Category name 
    output+="\n     "
    cnt=0
    name=[]
    for cat in list_cat:
        name.append(cat.budget_categories)
    len_name=[]
    for i in range(len(list_cat)):
        len_name.append(len(name[i]))
    max_len=max(len_name)
    
    for i in range(max_len):
      for nm in name:
        if len(nm)>i:
          output+=nm[i]+"  "
        else:
          output+="   "
      if i<max_len-1:
        output+="\n     "
    
    
    
                      
    print(output)
    return output
        
create_spend_chart(list_cat)      
        
        
        
        
        
        
        