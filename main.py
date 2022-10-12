"""Main file to run the project."""
from pyynechallengebank.BankController import BankController


def main():
    """Principal function who runs the project methods."""
    BankController().printBalances()
    BankController().printTransactions()


if __name__ == "__main__":
    main()
