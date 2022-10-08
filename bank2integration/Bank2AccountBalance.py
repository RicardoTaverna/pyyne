"""Class who creates an account balance."""

class Bank2AccountBalance():
    """Class who creates an account balance."""

    def __init__(self, balance: float, currency: str) -> None:
        """Class constructor.

        Args:
            balance (float): account quantity
            currency (str): account currency
        """
        self.balance = balance
        self.currency = currency

    def getBalance(self) -> float:
        """Return the account balance.

        Returns:
            float: account quantity
        """
        return self.balance

    def getCurrency(self) -> str:
        """Return the account currency.

        Returns:
            str: account currency
        """
        return self.currency
