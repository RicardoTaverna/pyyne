"""Class to create a transaction."""

from datetime import date
from typing import List
from bank2integration.Bank2AccountBalance import Bank2AccountBalance
from bank2integration.Bank2AccountTransaction import Bank2AccountTransaction, TRANSACTION_TYPES


class Bank2AccountSource():
    """Class to create a transaction."""

    @staticmethod
    def getBalance(accountNum: int) -> Bank2AccountBalance:
        """Return the account balance.

        Args:
            accountNum (int): account number

        Returns:
            Bank2AccountBalance: Bank2AccountBalance object
        """
        return Bank2AccountBalance(512.5, "USD")

    @staticmethod
    def getTransactions(accountNum: int, fromDate: date, toDate: date) -> List:
        """Return the account transactions.

        Args:
            accountNum (int): account number
            fromDate (date): transaction initial date
            toDate (date): transaction final date

        Returns:
            List: list of Bank2AccountTransaction objects.
        """
        arrList = []
        arrList.append(Bank2AccountTransaction(125.0, TRANSACTION_TYPES.DEBIT.value, "Amazon.com"))
        arrList.append(Bank2AccountTransaction(500.0, TRANSACTION_TYPES.DEBIT.value, "Car insurance"))
        arrList.append(Bank2AccountTransaction(800.0, TRANSACTION_TYPES.CREDIT.value, "Salary"))
        return arrList
