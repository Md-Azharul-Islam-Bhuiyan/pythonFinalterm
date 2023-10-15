from abc import ABC, abstractmethod
from datetime import datetime

class  Bank(ABC):
    allow_loan = True
    
    def __init__(self, accNumber, name, email, password, address, accType) -> None:
        self.accNumber = accNumber
        self.name = name 
        self.email = email
        self.password = password
        self.address = address
        self.accType = accType
        self.balance = 0
        self.countloan = 0
        self.loan = 0
        self.tHistory = []


    def deposite(self, amount):
        if amount >= 0 :
            self.balance += amount
            self.tHistory.append(f'Deposite: {amount} Date: {datetime.now()}')
            print(f'Acc no. {self.accNumber} deposited {amount} Tk.')
        else:
            print(f'Invalid amount {amount}')
    
    def withdraw(self, amount):
        
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            self.tHistory.append(f'Withdraw: {amount} Date: {datetime.now()}')
            print(f'From Account No {self.accNumber} you withdraw {amount} Tk')
            
        else:
            print(f'Withdrawal amount exceeded')
            
        

    
    @abstractmethod
    def checkBalance(self):
        pass

    @abstractmethod
    def checkTransactionHistory(self):
        pass

class Savings(Bank):
    def __init__(self,accNumber, name, email, password, address) -> None:
        super().__init__(accNumber, name, email, password, address, 'savings')

    
    

    def checkBalance(self):
        print('\n-------------------Balance-------------------------------\n')
        print(f'Your {self.accType} Acc No {self.accNumber} total balance is {self.balance}')
    
    def checkTransactionHistory(self):
        print('\n-------------------Transaction History-------------------\n')
        for history in self.tHistory:
            print(history)
    
    def takeLoan(self, amount):
        f = False
        if self.allow_loan == True:
            if self.countloan < 2 :
                self.countloan += 1
                self.loan += amount
                f = True
                self.tHistory.append(f'AccNo:{self.accNumber} take Loan: {amount} Date: {datetime.now()}')
                print(f'Your loan request successfully completed.\nAcc no. {self.accNumber} Total Loan: {self.loan} ')
                
            else:
                print('Your are not eligible to grab it.Your are already take 2 times')
                
        
        else:
            print('This Features currently Unavailable from the Authority')
        
        if f == True:
           return amount
        else:
          return 0
            
    

    def transfer_amount(self, tUser, amount):
        if  amount < self.balance:
            self.balance -= amount
            tUser.balance += amount
            self.tHistory.append(f'AccNo:{self.accNumber} transfer: {amount} Tk to  account no {tUser.accNumber} Date: {datetime.now()}')
        else:
            print('Insufficient balance!!. You can\'t transfer.')


class Current(Bank):
    def __init__(self,accNumber, name, email, password, address) -> None:
        super().__init__(accNumber, name, email, password, address, 'current')

    
    

    def checkBalance(self):
        print('\n-------------------Balance-------------------------------\n')
        print(f'Your {self.accType} Acc No {self.accNumber} total balance is {self.balance}')
    
    def checkTransactionHistory(self):
        print('\n-------------------Transaction History-------------------\n')
        for history in self.tHistory:
            print(history)
    
    def takeLoan(self, amount):
        f = False
        if self.allow_loan == True :
            if self.countloan < 2 :
                self.countloan += 1
                self.loan += amount
                f = True
                self.tHistory.append(f'AccNo:{self.accNumber} take Loan: {amount} Date: {datetime.now()}')
                print(f'Your loan request successfully completed.\nAcc no. {self.accNumber} Total Loan: {self.loan} ')
                
            else:
                print('Your are not eligible to grab it.Your are already take 2 times')
                
        
        else:
            print('This Features currently Unavailable from the Authority')
        

        if f == True:
            return amount
        else :
            return 0
            

    def transfer_amount(self, tUser, amount):
        if amount < self.balance:
            self.balance -= amount
            tUser.balance += amount
            self.tHistory.append(f'AccNo:{self.accNumber} transfer: {amount} Tk to  account no {tUser.accNumber} Date: {datetime.now()}')
        else:
            print('Insufficient balance!! You can\'t transfer.')
    



        
    
    



        