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


def drop_table():
        connect=sqlite3.connect("Bank_Accounts.db")
        cursor=connect.cursor()
        try:
                cursor.execute("""DROP TABLE IF EXISTS Transaction_history""")
                
                
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

""""Now building your tranction history """

def tranction_history(account,transaction_type,amount):#this func acts as both storing history and updating balance to the database.
        connect=sqlite3.connect("Bank_Accounts.db")
        connect.execute("PRAGMA foreign_keys = ON")
        cursor=connect.cursor()
        #creating the treansaction history table and entering or referencing the rows and columns into it.
        try:
               cursor.execute("""CREATE TABLE IF NOT EXISTS Transaction_history(
                                Transaction_ID INTEGER PRIMARY KEY ,
                                Account_Number NUMBER(8) 
                                        REFERENCES Bank_Accounts(Account_Number),
                                Type VARCHAR2(6) NOT NULL,
                                Amount INTEGER NOT NULL,
                                Balance_After NUMBER(8,2) NULL,
                                Time_stamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

                                CONSTRAINT type_dec CHECK(UPPER(Type) IN ('DEBIT','CREDIT'))
               )""")
               cursor.execute("""INSERT INTO Transaction_history(Account_Number,Type,Amount,Balance_After)
               VALUES(?,?,?,?)""",(account.account_no,transaction_type,amount,account.balance))
                #updating the balance into the database after the transaction.
               cursor.execute("""UPDATE Bank_accounts SET Balance=? WHERE Account_Number=?""",(account.balance,account.account_no))

               





               connect.commit()
        except sqlite3.Error:
            connect.rollback()
            raise
             
        
        finally:
               connect.close()

def get_transac_history(account_no):
       connect=sqlite3.connect("Bank_Accounts.db")
       cursor=connect.cursor()
       try:
              cursor.execute("""SELECT * FROM Transaction_history WHERE Account_Number = ?""",(account_no,))
              rows=cursor.fetchall()
              if not rows:
                     print("NO TRANSACTIONS FOUND")
              else:
                     for row in rows:
                      print(f"{row[2]}|Amount : {row[3]}|"
                            f"Balance After : {row[4]}|Time : {row[5]}")
              



              
       finally:
              connect.close()
              
              
               
       
       
          
     
     
    


