from pyynechallengebank.BankController import BankController


def main():
    BankController().printBalances()
    BankController().printTransactions()

if __name__ == "__main__":
    main()