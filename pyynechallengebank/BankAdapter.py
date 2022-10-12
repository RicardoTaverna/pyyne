"""Adapter classes."""

from datetime import date
from typing import List
from bank1integration.Bank1AccountSource import Bank1AccountSource
from bank2integration.Bank2AccountSource import Bank2AccountSource


class BankAdapter():
    """Adapter for bank2 and bank1 to get the account details without access originals methods."""

    def __init__(self, bank) -> None:
        """Class constructor."""
        self.bank = bank

    def getAccountBalance(self, accountId: int) -> float:
        """Balance method adapted.

        Args:
            accountId (int): the account id

        Returns:
            float: the account balance
        """
        if isinstance(self.bank, Bank2AccountSource):
            return self.bank.getBalance(accountNum=accountId).getBalance()
        return self.bank.getAccountBalance(accountId)

    def getAccountCurrency(self, accountId: int) -> str:
        """Balance method adapted.

        Args:
            accountId (int): the account id

        Returns:
            str: currency
        """
        if isinstance(self.bank, Bank2AccountSource):
            return self.bank.getBalance(accountNum=accountId).getCurrency()
        return self.bank.getAccountCurrency(accountId)

    def getTransactions(self, accountId: int, fromDate: date, toDate: date):
        """Transaction method adapted.

        Args:
            accountId (int): account id
            fromDate (date): from date
            toDate (date): to date
        """
        return self.bank.getTransactions(accountId, fromDate, toDate)
