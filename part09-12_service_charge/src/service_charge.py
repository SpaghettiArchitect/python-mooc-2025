class BankAccount:
    def __init__(self, name: str, account: str, balance: float):
        self.__name = name
        self.__account = account
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= self.balance * 0.01


if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)
