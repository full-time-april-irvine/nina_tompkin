class BankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = 0.006
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        if self.balance >= 0:
            print(f"Balance: ${round(self.balance,2)}")
        else:
            print(f"Balance: -${round(self.balance*-1,2)}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= (1+self.int_rate)
        return self