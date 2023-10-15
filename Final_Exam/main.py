from bank import Savings, Current
from Admin import Admin
import random

def main():
    admin = Admin()
    
    #Create User Account by User
    ac = f'CB{random.randint(1,1000)}'
    u1 = Savings(ac, 'Sakib', 'sakib@gmail.com', 's12', 'Dhaka')
    admin.add_user_account(u1)
    
    curr_User = None

    while True:
        
        print('----------User Type--------')
        print('1.Admin')
        print('2.User')
        print('3.Exit')
        Usertype = int(input('User type:'))
        if Usertype == 1:
            while True:
                
                    print('\n-----------Options----------\n')
                    print('1.Create Account')
                    print('2.Delete Account')
                    print('3.View All User')
                    print('4.Total Available Balance')
                    print('5.Total Loan Amount')
                    print('6.Toggle Loan Feature')
                    print('7.Exit')

                    ch = int(input('Enter your Options:'))
                    
                    if ch == 1:
                        nm = input('\nEnter Name:')
                        email = input('Enter Email:')
                        passw = input('Enter Password:')
                        addr = input('Enter Address:')
                        acType = input('Enter Account Type:(savings/current)?')
                        admin.createAccount(nm, email, passw, addr, acType)

                    elif ch == 2:
                        acNo = input('Enter Acc No:') 
                        admin.deleteAccount(acNo)
                    elif ch == 3:
                        admin.viewAllUser()
                    elif ch == 4:
                          print(f'\n Total Available balance: {admin.totalBalance}')
                        
                    elif ch == 5:
                        print(f'\n Total amount of Loan: {admin.totalLoan}')
                    elif ch == 6:
                        status = input('Enter status (True/False)?:')
                        admin.loanFeature(status)
                    elif ch == 7:
                        break
                    else:
                        print('Invalid Option choose right option')

        elif Usertype == 2:
            while True:
                if curr_User == None:
                    print('\nNo User Logged in!\n')
                    c = input('\nLogin or Register (L/R)?:')

                    if c == 'R':
                        accNumber = f'CB{random.randint(1,1000)}'
                        nm = input('\nEnter Name:')
                        email = input('Enter Email:')
                        passw = input('Enter Password:')
                        addr = input('Enter Address:')
                        acType = input('Enter Account Type:(savings/current)?')

                        if acType == 'savings':
                            curr_User = Savings(accNumber, nm, email, passw, addr)
                            admin.add_user_account(curr_User)
                            print('Account successfully created')
                        elif acType == 'current':
                            curr_User = Current(accNumber, nm, email, passw, addr)
                            admin.add_user_account(curr_User)
                            print('Account successfully created')
                        else :
                          print(f'Invalid account type {acType}')

                    else:
                        nu = input('Enter Account Number : ')
                        pas = input('Enter Password:')

                        for account in admin.user_accounts :
                            # print(account.accNumber)
                            f = False
                            if account.accNumber == nu:
                                if account.password == pas:
                                    curr_User = account
                                    f = True
                                    break
                                else:
                                    print('Wrong Password! Try Again!')
                            
                        if f == False:
                            print('\nYour given account number user not found!\n')               
        


                else:

                    if curr_User.accType == 'savings':
                        print(f'\nwelcome {curr_User.name}!\n')
                        print(f'\n---------{curr_User.accType} Account---------')
                        print('1. Deposite')
                        print('2. Withdraw')
                        print('3. Available Balance')
                        print('4. Loan')
                        print('5. Transfer Amount')
                        print('6. Transaction History')
                        print('7. Logout')
                        
                        op = int(input("Options:"))

                        if op == 1:
                            amount = int(input('Enter Amount: '))
                            curr_User.deposite(amount)
                            admin.totalBalance += amount
                        elif op == 2:
                            amount = int(input('Enter Amount: '))
                            if admin.totalBalance == 0:
                                  print('You can\'t withdraw money bankcrupted!!')
                            else: 
                                curr_User.withdraw(amount)
                                admin.totalBalance -= amount
                            # print(f'After withdraw: {admin.totalBalance}')
                        elif op == 3:
                            curr_User.checkBalance()
                        elif op == 4:
                            amount = int(input("Enter your loan amount:"))
                 
                            if admin.totalBalance >= amount and admin.totalBalance!=0:
                                
                                am = curr_User.takeLoan(amount)
                                admin.totalBalance -= am
                                admin.totalLoan += am
                                
                            else:
                                print('you can\'t take loan.')
                            # print(admin.totalBalance, admin.totalLoan)
                            
                        elif op == 5:
                            acountNo = input("Enter Another number:")
                            amount = int(input("Enter amount:"))
                            f = False
                            if admin.totalBalance > amount:
                                for user in admin.user_accounts:
                                    if user.accNumber == acountNo:
                                        curr_User.transfer_amount(user, amount)
                                        print(f'Amount {amount} has been successfully transfered!')
                                        f = True
                                        break
                                if f == False:
                                   print('Account not existed!')
                            else:
                               print('Insufficient Balance!!')

                        elif op == 6:
                            curr_User.checkTransactionHistory()
                        elif op == 7:
                            curr_User = None
                            break
                    
                    elif curr_User.accType == 'current':
                            print(f'\nwelcome {curr_User.name}!\n')
                            print(f'\n---------{curr_User.accType} Account---------')
                            print('1. Deposite')
                            print('2. Withdraw')
                            print('3. Available Balance')
                            print('4. Loan')
                            print('5. Transfer Amount')
                            print('6. Transaction History')
                            print('7. Logout')

                            
                            op = int(input("Options:"))

                            if op == 1:
                                amount = int(input('Enter Amount: '))
                                curr_User.deposite(amount)
                                admin.totalBalance += amount

                            elif op == 2:
                                amount = int(input('Enter Amount: '))

                                if admin.totalBalance == 0:

                                    print('You can\'t withdraw money bankcrupted!!')

                                else: 

                                    curr_User.withdraw(amount)
                                    admin.totalBalance -= amount
                                    

                            elif op == 3:
                                curr_User.checkBalance()
                            elif op == 4:
                                amount = int(input("Enter your loan amount:"))

                                if admin.totalBalance >= amount and admin.totalBalance!=0:
                                    am = curr_User.takeLoan(amount)
                                    admin.totalBalance -= am
                                    admin.totalLoan += am
                                    
                                else:
                                    print('you can\'t take loan.')

                            elif op == 5:
                                acountNo = input("Enter Another number:")
                                amount = int(input("Enter amount:"))
                                f = False
                                f = False
                                if admin.totalBalance > amount:
                                    for user in admin.user_accounts:
                                        if user.accNumber == acountNo:
                                            curr_User.transfer_amount(user, amount)
                                            print(f'Amount {amount} has been successfully transfered!')
                                            f = True
                                            break
                                    if f == False:
                                        print('Account not existed!')
                                else:        
                                  print('Insufficient Balance!!')
                            elif op == 6:
                                curr_User.checkTransactionHistory()  
                            elif op == 7:
                                curr_User = None
                                break                        
        
        elif Usertype == 3:
            break


if __name__ == '__main__':
    main()
    