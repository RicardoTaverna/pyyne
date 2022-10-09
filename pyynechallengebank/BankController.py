"""Created by Par Renyard on 5/12/21."""

from bank1integration.Bank1AccountSource import Bank1AccountSource
from bank2integration.Bank2AccountSource import Bank2AccountSource
from pyynechallengebank.BankAdapter import Bank2BalanceAdapter



class BankController():
    """Controller that pulls information form multiple bank integrations and prints them to the console."""

    @staticmethod
    def printBalances():
        """Implement me to pull balance information from all available bank integrations and display them, one after the other."""
        print("============ ACCOUNT BALANCES ============")
        accountId = 123
        accounts = [Bank1AccountSource(), Bank2BalanceAdapter()]
        for idx, account in enumerate(accounts):
            print(f"Bank{idx+1} - {account.getAccountBalance(accountId)} {account.getAccountCurrency(accountId)}")
        print("------------------------------------------")

    @staticmethod
    def printTransactions():
        """Implement me to pull transactions from all available bank integrations and display them, one after the other."""
        accountId = 123
        fromDate = "2022-01-12"
        toDate = "2022-02-12"

        bankList = [Bank1AccountSource(), Bank2AccountSource()]
        print("============ ACCOUNT TRANSACTIONS ============")
        for banks in bankList:
            for _, bank in enumerate(banks.getTransactions(accountId, fromDate, toDate)):
                print(f"{bank.getAmount()} - {bank.getType()} - {bank.getText()}")
