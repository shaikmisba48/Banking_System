import restrictions as r
import database 


class Bank_account: #accoubnt
    def __init__(self,name,account_no,balance,account_type):
        self.name=name
        self.account_no=account_no
        self.balance=balance
        self.account_type=account_type.upper()

        r._emptyError(name,"NAME")
        r._emptyError(account_no,"ACCOUNT NUMBER")
        r._emptyError(account_type,"ACCOUNT TYPE")
        r._checkingAccType(account_type)
        r._datatypecheck(name)
        r._datatypecheck(account_no)
        r._balancedatatype(balance)




    def credit(self,amount):
        r._checkNegativeValue(amount)
            
        self.amount=amount
        self.balance+=amount
        return f"amount of {self.amount} is credited and total balance is {self.balance}"

    
    def debit(self,withdraw):
        r._checkNegativeValue(withdraw)
        self.withdraw=withdraw
        self.balance-=withdraw
        return f"amount of {self.withdraw} is debited from your account and your balance is {self.balance}"

    
    def check_balance(self):
       return f"{self.balance} is your total balance"


    def display_acc_details(self):
        acc_det={
            "Name":self.name,
            "account Number":self.account_no,
            "balance":self.balance,
            "account type":self.account_type,
                 
                 
                 }
        return acc_det.items()
    
        
    

class Savings(Bank_account):
        _intrest = 0

        def debit(self,amount):
            r._checkNegativeValue(amount)
            if amount>self.balance:
                raise ValueError("INSUFFICENT BALANCE")
            return super().debit(amount)#uses parents existing subtraction
        
        def _updateInterest(self):
             if self.balance>50000:
                 self._intrest+=20//100
                 self._intrest+=self.balance
             elif self.balance>2000:
                 self._intrest+=0.8//100
                 self._intrest+=self.balance 
             elif self.balance>10000:
                 self._intrest+=4//100
                 self._intrest+=self.balance
             elif self.balance==0:
                self._intrest += self.balance
             else:
                 return  
                  
             
                  
               

                     
        

             
class Current(Bank_account):
    def debit(self,amount):
        r._checkNegativeValue(amount)
        if self.balance-amount<-150:
            raise(ValueError("CROSSED YOUR OVERDRAFT LIMIT"))
        return super().debit(amount)

#database.drop_table()

real_bal=database.balance_equalise(89776548)
acc1=Current("misba","8977889",78.0,"current")
acc2=Savings('nirmal','89776548',real_bal[0],'savings')

print("Starting balance :",acc2.balance)

acc2.debit(200)
database.tranction_history(acc2,'Debit',200)
print("After withdraw :",acc2.balance)


acc2.credit(500)
database.tranction_history(acc2,'Credit',500)
print("After deposit :",acc2.balance)

saved_balance=database.balance_equalise(89776548)
print("Balance saved in database :",saved_balance[0])



