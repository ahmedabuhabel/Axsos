class User:
    def __init__(self, name, email_address):
        self.name = name
        self.account_balance = 0
        self.email = email_address

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


user = User("Yash", "Yash@123")
user2 = User("Ahmad", "Ahmad@123")
user.make_deposit(100).transfer_money(user2, 500)

user2.display_user_balance()
