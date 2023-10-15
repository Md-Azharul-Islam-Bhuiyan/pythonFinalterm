from bank import Bank, Savings, Current
import random
class Admin:
    
    totalBalance = 0
    totalLoan = 0
    def __init__(self) -> None:
        self.user_accounts = []
    
    
    def createAccount(self, name, email, password, address, accType):
        accNumber = f'CB{random.randint(1,1000)}'
        if accType == 'savings':
            user_account = Savings(accNumber, name, email, password, address)
            print('Account has been created successfully')
        elif accType == 'current':
            user_account = Current(accNumber, name, email, password, address)
            print('Account has been created successfully')
        else:
            print('Invalid account type\n')
        
        self.user_accounts.append(user_account)
    
    def add_user_account(self, user_account):
        self.user_accounts.append(user_account)
    

    def deleteAccount(self, accNumber):
        for user in self.user_accounts:
            if user.accNumber == accNumber:
                 self.user_accounts.remove(user)
                 print(f'Account no. {accNumber} successfully deleted')
                 break
    

    def viewAllUser(self):
        if len(self.user_accounts) != 0:
            for user in self.user_accounts:
              print(f'Acc no:{user.accNumber} Name:{user.name} Account Type: {user.accType}')
        else:
            print('No User Found!')
    
    # def increase_total_balance(self):
    #     total = 0
    #     for user in self.user_accounts:
    #         total += user.balance
        
    #     return total
        
        # if totalBalance == 0 :
        #     Bank.bankcurpt = True

    # def total_balance(self):
    #     self.totalBalance =  self.increase_total_balance()
    #     print(f'\n Total Available balance: {self.totalBalance}')
    

    # def loan_amount(self) :
    #     total = 0
    #     for user in self.user_accounts:
    #         total += user.loan
    #     return total
        
    # def increase_total_loan(self, amount):
    #     self.totalLoan = self.loan_amount 
    #     self.totalLoan +=   
    
    # def total_loan_amount(self) :
    #     self.totalLoan = self.loan_amount()
    #     print(f'\n Total amount of Loan: {self.totalLoan}')


    
    def loanFeature(self, isAvail):
        if isAvail == 'False':
           Bank.allow_loan = False
           print(f'Loan feature off {isAvail}')
        elif isAvail == 'True' :
           Bank.allow_loan = True
           print(f'Loan feature on {isAvail}')


            