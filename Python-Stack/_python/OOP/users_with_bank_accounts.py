class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"your balance is ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
    def __init__(self, name, email_address):
        self.name = name
        self.accounts = {}
        self.email = email_address

    def add_account(self, account_name, int_rate=0.02, balance=0):
        self.accounts[account_name] = BankAccount(int_rate, balance)
        return self

    def make_deposit(self, account_name, amount):

        (
            self.accounts[account_name].deposit(amount)
            if account_name in self.accounts
            else print("Account not found")
        )

    def make_withdrawal(self, account_name, amount):
        (
            self.accounts[account_name].withdraw(amount)
            if account_name in self.accounts
            else print("Account not found")
        )

    def display_user_balance(self, account_name):
        if account_name in self.accounts:
            print(
                f"User: {self.name}, Account: {account_name}, Balance: {self.accounts[account_name].balance}"
            )

    def transfer_money(self, from_account, other_user, to_account, amount):
        if from_account in self.accounts and to_account in other_user.accounts:
            self.accounts[from_account].withdraw(amount)
            other_user.accounts[to_account].deposit(amount)
        else:
            print("Account not found")
