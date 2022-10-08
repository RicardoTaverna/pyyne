"""Created by Par Renyard on 5/12/21."""

from bank1integration.Bank1AccountSource import Bank1AccountSource
from pyynechallengebank.BankAdapter import Bank2BalanceAdapter



class BankController():
    """Controller that pulls information form multiple bank integrations and prints them to the console."""

    @staticmethod
    def printBalances():
        """Implement me to pull balance information from all available bank integrations and display them, one after the other."""
        print("============ ACCOUNT BALANCES ============")
        accounts = [Bank1AccountSource(), Bank2BalanceAdapter()]
        for idx, account in enumerate(accounts):
            print(f"Bank{idx+1} - {account.getAccountBalance(123)}")
        print("------------------------------------------")

    @staticmethod
    def printTransactions():
        """Implement me to pull transactions from all available bank integrations and display them, one after the other."""
        
    
