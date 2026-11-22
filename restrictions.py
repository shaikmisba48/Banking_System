def _checkNegativeValue(s):#stopping the negative numbers input
        
        if s <= 0 :
            raise(ValueError("[FATAL]: The amount cannot be negative "))

def _emptyError(value,feild_name):#blocking entering noo values and causing the program to fail
           
            if value is None or str(value).strip()=="":
                raise(ValueError(f"{feild_name} cannot be empty"))        
        
def _checkingAccType(acc_ty):#user can write to sentence in upper or lower case but in that correct case we shouldnot through error
       acc_ty=acc_ty.upper()
       if acc_ty=="SAVINGS" or acc_ty=="CURRENT":
              return (acc_ty,"is your account type")
       else:
             raise(ValueError("invalid account type"))
def _datatypecheck(data_type):#setting restrictions like name can only have string and balance is int etc
       if not isinstance(data_type,str):
              raise(TypeError("INVALID DATA TYPE IT CAN ONLY BE A STRING"))       
def _balancedatatype(balance):
       if  not isinstance(balance,float):
              if isinstance(balance,int):
                     return

              else:
                     raise(ValueError("ONLY FLOAT AND INT DATATYPE IS ALLOWED"))       

def _Overdraft_limit(account_typ):
       if account_typ=="Savings":
              def debit(self,amount):
                     self.amount=amount
                     self.balance-=amount
                     if amount<=self.balance:
                            return f"{self.amount } is your debited amount and total balance is {self.balance}"
                     raise(ValueError("INSUFFICENT BALANCE"))
              
                     


