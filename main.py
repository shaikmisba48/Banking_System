import database as db
from bankAccount import Savings,Current


account_no=input("Enter your Account Number :")



details=db.get_account(account_no)#we use this as an object for our deposit and withdraw just rem like importing obj to here
if details[3].upper()=='SAVINGS':
    account=Savings(details[0],str(details[1]),details[2],details[3])


elif details[3].upper()=='CURRENT':    
    account=Current(details[0],str(details[1]),details[2],details[3])
else:
    raise(ValueError("INVALID ACCOUNT TYPE"))

#print(account.name)
#print(account.balance)





while True:
    print("1.Check balance\n"
      "2.Deposit\n"
      "3.Withdraw\n"
      "4.View transaction History\n"
      "5.Exit\n"
      )
    try:
        choice=int(input("Enter your choice in numbers:"))
    except ValueError:
        print("Please Enter a number from 1 to 5.")
        continue
    

    if choice==1:
        balance_db=db.balance_equalise(account_no)
        print(balance_db[0])


    elif choice==2:
        try:
            print("Enter the amount you want to deposit")
            amount=int(input())
            account.credit(amount)
        except ValueError as error:
            print(error)    
            continue
        
        db.tranction_history(account,"CREDIT",amount)
        print("SUCCESS !") 

        
    elif choice==3:
        try:
            print("enter the amount you want to Withdraw")
            amount=int(input())
            account.debit(amount)
        except ValueError as error:
            print(error)
            continue
       
        db.tranction_history(account,"DEBIT",amount)
        print("SUCCESS !") 


    elif choice==4:
        db.get_transac_history(account_no)#there is already print in the function
    elif choice==5:
        print("Exit") 
        break
    else:
        print("Enter a correct choice!")
