"""Adapter classes."""

from bank2integration.Bank2AccountSource import Bank2AccountSource

class Bank2BalanceAdapter():
    """Adapter for bank2 to get the account balance with the same method as the bank 1."""

    def __init__(self) -> None:
        """Class constructor."""
        self.bank2 = Bank2AccountSource()

    def getAccountBalance(self, accountId: int) -> float:
        """Method to be adated.

        Args:
            accountId (int): the account id

        Returns:
            float: the account balance
        """
        return self.bank2.getBalance(accountNum=accountId).getBalance()
