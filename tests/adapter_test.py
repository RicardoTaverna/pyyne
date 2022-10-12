"""Class for testing bank2 adapter."""

import unittest
from bank1integration.Bank1AccountSource import Bank1AccountSource
from bank1integration.Bank1Transaction import Bank1Transaction
from bank2integration.Bank2AccountSource import Bank2AccountSource
from bank2integration.Bank2AccountTransaction import Bank2AccountTransaction
from pyynechallengebank.BankAdapter import BankAdapter


class TestBank2Adapter(unittest.TestCase):
    """Class for testing bank2 adapter."""

    def test_balance_bank1(self):
        """Test if the bank adapter using the same function name for bank1 will retrieve balance value."""
        accountId = 123
        bank1 = Bank1AccountSource()
        account = BankAdapter(bank=bank1)
        self.assertEqual(account.getAccountBalance(accountId), 215.5)

    def test_balance_bank2(self):
        """Test if the bank adapter using the same function name for bank2 will retrieve balance value."""
        accountId = 123
        bank2 = Bank2AccountSource()
        account = BankAdapter(bank=bank2)
        self.assertEqual(account.getAccountBalance(accountId), 512.5)

    def test_currency_bank1(self):
        """Test if the bank adapter using the same function name for bank1 will retrieve currency information."""
        accountId = 123
        bank1 = Bank1AccountSource()
        account = BankAdapter(bank=bank1)
        self.assertEqual(account.getAccountCurrency(accountId), "USD")

    def test_currency_bank2(self):
        """Test if the bank adapter using the same function name for bank2 will retrieve currency information."""
        accountId = 123
        bank2 = Bank1AccountSource()
        account = BankAdapter(bank=bank2)
        self.assertEqual(account.getAccountCurrency(accountId), "USD")

    def test_transaction_bank1(self):
        """Test if the bank adapter using the same function name for bank1 will retrieve transanction information."""
        accountId = 123
        fromDate = "2022-01-12"
        toDate = "2022-02-12"
        bank1 = Bank1AccountSource()
        accounts = BankAdapter(bank=bank1).getTransactions(accountId, fromDate, toDate)
        for account in accounts:
            self.assertIsInstance(account, Bank1Transaction)

    def test_transaction_bank2(self):
        """Test if the bank adapter using the same function name for bank2 will retrieve transanction information."""
        accountId = 123
        fromDate = "2022-01-12"
        toDate = "2022-02-12"
        bank2 = Bank2AccountSource()
        accounts = BankAdapter(bank=bank2).getTransactions(accountId, fromDate, toDate)
        for account in accounts:
            self.assertIsInstance(account, Bank2AccountTransaction)