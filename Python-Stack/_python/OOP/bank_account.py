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


acc1 = BankAccount()
acc2 = BankAccount()
acc1.deposit(100).deposit(200).deposit(13).withdraw(
    27
).yield_interest().display_account_info()
acc2.deposit(50).deposit(20).withdraw(10).withdraw(13).withdraw(12).withdraw(
    14
).yield_interest().display_account_info()
