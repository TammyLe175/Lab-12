
class Account:
    def __init__(self, name: str) -> None:
        """
        function to set up the account
        :param name: account name

        """
        balance = 0
        self.__account_name = name
        self.__account_balance = balance

    def deposit(self, amount: float) -> bool:
        """
        function deposit a amount of money, cannot be less than or equal to 0
        :param amount: ammount money deposit in account

        """

        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        :param amount: the amount of money to withdraw in the account
        :return: an action of withdraw an amount of money
        """
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        """

        :return: the current balance in the account
        """
        return self.__account_balance
    def get_name(self):
        """
        :return: the name of the account
        """
        return self.__account_name


