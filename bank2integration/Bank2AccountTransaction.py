"""Class to create a transaction."""
from enum import Enum


class TRANSACTION_TYPES(Enum):
    """Transaction types enum."""

    DEBIT = "DEBIT"
    CREDIT = "CREDIT"


class Bank2AccountTransaction():
    """Class to create a transaction."""

    def __init__(self, amount: float, type: str, text: str) -> None:
        """Class constructor.

        Args:
            amount (float): transaction quantity
            type (str): transaction type
            text (str): transaction description
        """
        self.amount = amount
        self.type = type
        self.text = text
    
    def getAmount(self) -> float:
        """Return the amount of the transaction.

        Returns:
            float: transaction quantity
        """
        return self.amount
    
    def getType(self) -> str:
        """Return the type of the transaction.

        Returns:
            type (TRANSACTION_TYPES): transaction type
        """
        return self.type
    
    def getText(self) -> str:
        """Return the description of the transaction.

        Returns:
            str: transaction description
        """
        return self.text
