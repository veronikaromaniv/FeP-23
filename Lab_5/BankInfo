from typing import List

class BankInfo:
    def __init__(self, bank_name: str, holder_name: str, accounts_number: List[str], credit_history: dict):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = accounts_number
        self.credit_history = credit_history

    def transaction_list(self, account_number: str) -> List[str]:
        if account_number in self.accounts_number:
            if account_number in self.credit_history:
                transactions = self.credit_history.get(account_number, [])
                return transactions
            else:
                return ["No credit history available for the given account number"]
        else:
            return ["No transactions available for the given account number"]
