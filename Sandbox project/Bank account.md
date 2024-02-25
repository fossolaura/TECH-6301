# Final Project

# BANK ACCOUNT

## DESCRIPTION

This project allows you to apply the knowledge gained from all Python modules covered in the learning platform. The knowledge from each module is essential for implementing certain functionalities in this project.

In this project, you will simulate bank account operations using object-oriented programming (OOP). You should create a class called BankAccount, specializing in all banking operations, including:

- Creating an account.
- Depositing money.
- Withdrawing money.
- Checking the balance.
- Getting the account type.
- Getting the account number.
- Getting the holder name.
- Keeping a transaction history.

## OBJECTIVE

* By the end of this project, you will be able to
* Create a class for the bank account operation;
* Implement multiple functions that are each specialized in only one account operation; and
* Test your bank account class by applying multiple operations.

## THE CODE

``` python
import uuid

class BankAccount(object):

    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.id = str(uuid.uuid4())
        self.filename = f"{self.id}_{self.accountType}_{self.name}.txt"
        
        with open(self.filename, 'w') as file:
            file.write(f"Account created: {self.name}, {self.accountType}, Balance: {self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        with open(self.filename, 'a') as file:
            file.write(f"Deposit: {amount}, New Balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            with open(self.filename, 'a') as file:
                file.write(f"Withdraw: {amount}, New Balance: {self.balance}\n")

    def get_balance(self):
        return self.balance

    def get_user_id(self):
        return self.id

    def get_username(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(self.filename, 'r') as file:
            return file.read()
```
## TESTING THE CODE

### Test 1: CHEQUING - Creating An Account and Performing Transactions.
```PYTHON
account1 = BankAccount("Ken Doll", "chequing")
account1.deposit(10000)
account1.withdraw(50)
print("Transaction history for Ken Doll:")
print(account1.get_transaction_history())
```
### Test 2: Creating An Account and Performing Transactions w/ Insufficient funds.
```PYTHON
account2 = BankAccount("Barbie", "savings", 500000)
account2.deposit(200000)
account2.withdraw(800000)  
print("Transaction history for Barbie:")
print(account2.get_transaction_history())
```
### Test 3: SAVINGS - Creating An Account and Performing Transactions.
```PYTHON
account3 = BankAccount("Captain America", "savings", 20000)
account3.deposit(250)
account3.withdraw(500)
account3.deposit(100)
account3.withdraw(50)
print("Transaction history for Captain America:")
print(account3.get_transaction_history())
```
### Test 4: Creating Multiple Accounts and Performing Transactions
```PYTHON
account4 = BankAccount("SpiderMan", "chequing", 100)
account4.deposit(200)
account4.withdraw(150)
account5 = BankAccount("Justice League LLC", "savings", 300)
account5.withdraw(100)
account5.deposit(400)
print("Transaction history for SpiderMan:")
print(account4.get_transaction_history())
print("Transaction history for Justice League LLC:")
print(account5.get_transaction_history())
```
END
