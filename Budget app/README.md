## Budget app

Dev. by : **Radwane Ait Ouhani**.

Context : **'Scientific Computing with python'** certification project on **FreeCodeCamp**.


### The idea :
 
The `Category` class to instantiate objects based on different budget categories
like food, clothing, and entertainment. When objects are created, they are passed in the 
name of the category. The class have an instance variable called `ledger` that is a `list`. The 
class also contain the following methods:

* A `deposit` method that accepts an amount and description. If no description is given, it should default to an empty string. 
* A `withdraw` method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. 
* A `get_balance` method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
* A `transfer` method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to
[Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget 
 Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
* A `check_funds` method that accepts an amount as an argument. It returns `False` if the amount is less than the balance of the budget category and returns `True` otherwise. 
This method should be used by both the withdraw method and transfer method.


### Exanmpe :

When the `budget` object is printed, here is an example of the output:
```
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
```

### An other idea :

Besides the `Category` class,  a function called `create_spend_chart` that takes a list of
categories as an argument. It should return a bar chart.

The chart show the percentage spent in each category passed in to the 
function. The percentage spent is calculated only with withdrawals and 
not with deposits.This function is to set up to four categories.

When the function is called, here is an example of the output:
```
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
```
