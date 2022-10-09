"""Class for testing bank2 adapter."""

import unittest

from pyynechallengebank.BankAdapter import Bank2BalanceAdapter

class TestBank2Adapter(unittest.TestCase):
    """Class for testing bank2 adapter."""

    def test_balance(self):
        """Test if the bank2 adapter using the same function name for bank1 will retrieve bank2 balance information."""
        accountId = 123
        account = Bank2BalanceAdapter()
        self.assertEqual(account.getAccountBalance(accountId), 512.5)

    def test_currency(self):
        """Test if the bank2 adapter using the same function name for bank1 will retrieve bank2 currency information."""
        accountId = 123
        account = Bank2BalanceAdapter()
        self.assertEqual(account.getAccountCurrency(accountId), "USD")
