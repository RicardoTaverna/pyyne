"""Created by Par Renyard on 5/12/21."""

from typing import Any
from bank1integration.Bank1AccountSource import Bank1AccountSource
from bank2integration.Bank2AccountSource import Bank2AccountSource
from pyynechallengebank.BankAdapter import Bank2BalanceAdapter


class BankController():
    """Controller that pulls information form multiple bank integrations and prints them to the console."""

    def printBalances(self):
        """Implement me to pull balance information from all available bank integrations and display them, one after the other."""
        print("============== ACCOUNT BALANCES ==============")
        accountId = 123
        accounts = [Bank1AccountSource(), Bank2BalanceAdapter()]
        for idx, account in enumerate(accounts):
            print(f"Bank{idx+1} - {account.getAccountBalance(accountId)} {account.getAccountCurrency(accountId)}")
        print("----------------------------------------------")

    def printTransactions(self):
        """Implement me to pull transactions from all available bank integrations and display them, one after the other."""
        accountId = 123
        fromDate = "2022-01-12"
        toDate = "2022-02-12"

        bankList = [Bank1AccountSource(), Bank2BalanceAdapter()]
        print("============ ACCOUNT TRANSACTIONS ============")
        for idx, banks in enumerate(bankList):
            print(f"------------------- bank {idx+1} -------------------")
            for _, bank in enumerate(banks.getTransactions(accountId, fromDate, toDate)):
                currency = banks.getAccountCurrency(accountId)

                gettype = self.__getType(bank_type=bank.getType())

                print(f"{bank.getAmount()} {currency} - {gettype} - {bank.getText()}")
            print("----------------------------------------------")

    def __getType(self, bank_type: Any):
        """Return the type Credit or Debit."""
        if bank_type == 1:
            gettype = "CREDIT"
        elif bank_type == 2:
            gettype = "DEBIT"
        else:
            gettype = bank_type

        return gettype
