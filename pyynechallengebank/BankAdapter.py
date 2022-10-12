"""Adapter classes."""

from datetime import date
from typing import List
from bank1integration.Bank1AccountSource import Bank1AccountSource
from bank2integration.Bank2AccountSource import Bank2AccountSource


class Bank2Adapter():
    """Adapter for bank2 to get the account balance with the same method as the bank 1."""

    def __init__(self) -> None:
        """Class constructor."""
        self.bank2 = Bank2AccountSource()

    def getAccountBalance(self, accountId: int) -> float:
        """Balance method adapted.

        Args:
            accountId (int): the account id

        Returns:
            float: the account balance
        """
        return self.bank2.getBalance(accountNum=accountId).getBalance()

    def getAccountCurrency(self, accountId: int) -> str:
        """Balance method adapted.

        Args:
            accountId (int): the account id

        Returns:
            str: currency
        """
        return self.bank2.getBalance(accountNum=accountId).getCurrency()

    def getTransactions(self, accountId: int, fromDate: date, toDate: date):
        """Transaction method adapted.

        Args:
            accountId (int): account id
            fromDate (date): from date
            toDate (date): to date
        """
        return self.bank2.getTransactions(accountId, fromDate, toDate)
