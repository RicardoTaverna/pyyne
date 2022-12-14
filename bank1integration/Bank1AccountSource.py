"""Class to create an account."""

from datetime import date
from typing import List

from bank1integration.Bank1Transaction import Bank1Transaction


class Bank1AccountSource():
    """Class to create an account with data."""


    def getAccountBalance(self, accountId: int) -> float:
        """Return the account balance.

        Args:
            accountId (int): account id

        Returns:
            float: account balance
        """
        return 215.5
    
    def getAccountCurrency(self, accountId: int) -> str:
        """Return the account currency.

        Args:
            accountId (int): account id

        Returns:
            str: account currency
        """
        return "USD"

    def getTransactions(self, accountId: int, fromDate: date, toDate: date) -> List:
        """Return the account transactions.

        Args:
            accountId (int): account id
            fromDate (date): transaction initial date
            toDate (date): transaction final date

        Returns:
            List: list of transactions
        """
        arrList = []
        
        arrList.append(Bank1Transaction(100.0, Bank1Transaction.TYPE_CREDIT, "Check deposit"))
        arrList.append(Bank1Transaction(25.5, Bank1Transaction.TYPE_DEBIT, "Debit card purchase"))
        arrList.append(Bank1Transaction(225.0, Bank1Transaction.TYPE_DEBIT, "Rent payment"))

        return arrList
