"""Class for testing bank2 adapter."""

import unittest
from bank2integration.Bank2AccountTransaction import Bank2AccountTransaction
from pyynechallengebank.BankAdapter import Bank2Adapter


class TestBank2Adapter(unittest.TestCase):
    """Class for testing bank2 adapter."""

    def test_balance(self):
        """Test if the bank2 adapter using the same function name for bank1 will retrieve bank2 balance information."""
        accountId = 123
        account = Bank2Adapter()
        self.assertEqual(account.getAccountBalance(accountId), 512.5)

    def test_currency(self):
        """Test if the bank2 adapter using the same function name for bank1 will retrieve bank2 currency information."""
        accountId = 123
        account = Bank2Adapter()
        self.assertEqual(account.getAccountCurrency(accountId), "USD")

    def test_transaction(self):
        """Test if the bank2 adapter using the same function name for bank1 will retrieve bank2 transanction information."""
        accountId = 123
        fromDate = "2022-01-12"
        toDate = "2022-02-12"
        accounts = Bank2Adapter().getTransactions(accountId, fromDate, toDate)
        for account in accounts:
            self.assertIsInstance(account, Bank2AccountTransaction)
