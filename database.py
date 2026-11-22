import sqlite3

def add_account(account):
        connect=sqlite3.connect("Bank_Accounts.db")
        cursor=connect.cursor()
        
        try:
            
    
            cursor.execute("""CREATE TABLE IF NOT EXISTS Bank_Accounts(
                            Name VARCHAR2(30) NOT NULL,
                            Account_Number NUMBER(8) PRIMARY KEY,
                            Balance NUMBER(8,2) NULL,
                            Account_Type VARCHAR2(7) NOT NULL

                            CONSTRAINT account_type_limitation CHECK(UPPER(Account_Type) IN ('SAVINGS','CURRENT'))); """)
         
         
         
                              
                                
            cursor.execute("""INSERT INTO Bank_Accounts(
                            Name,Account_Number,Balance,Account_Type
                            )  VALUES (?,?,?,?)""",(account.name,account.account_no,account.balance,account.account_type))

         
            connect.commit()
        finally:
            connect.close()

def update_balance(account):
        connect=sqlite3.connect("Bank_Accounts.db")
        cursor=connect.cursor()
        try:
                cursor.execute("""UPDATE Bank_accounts SET Balance=? WHERE Account_Number=?""",(account.balance,account.account_no))
                
                
                connect.commit()
        finally:
                connect.close()
def drop_table():
        connect=sqlite3.connect("Bank_Accounts.db")
        cursor=connect.cursor()
        try:
                cursor.execute("""DROP TABLE IF EXISTS Bank_Accounts""")
                
                
                connect.commit()
        finally:
                connect.close()
                """"why we are defining this is that because that account baalance is always resets to the entered balance rather than getting it from database """
def balance_equalise(account_no):
        connect=sqlite3.connect("Bank_Accounts.db")
        cursor=connect.cursor()
        try:
                cursor.execute("""SELECT Balance FROM Bank_Accounts WHERE Account_Number is ?""",(account_no,))
                row=cursor.fetchone()

                if  row is not None:
                        
                        return row
                else:
                        raise(ValueError("Invalid Account Number"))
               
               



               
        finally:
               connect.close()

       
          
     
     
    


