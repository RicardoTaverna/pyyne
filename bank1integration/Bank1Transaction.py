"""Class to create transactions."""

class Bank1Transaction():
    """Class to create transactions for the bank 1."""

    TYPE_CREDIT = 1
    TYPE_DEBIT = 2


    def __init__(self, amount: float, type: int, text: str) -> None:
        """Class constructor.

        Args:
            amount (float): transaction quantity
            type (int): transaction type (1, 2)
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

    def getType(self) -> int:
        """Return the type of the transaction.

        Returns:
            int: transaction type (1, 2)
        """
        return self.type
    
    def getText(self) -> str:
        """Return the description of the transaction.

        Returns:
            str: transaction description
        """
        return self.text