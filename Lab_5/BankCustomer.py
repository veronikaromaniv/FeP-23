from dataclasses import dataclass
from schemas.BankInfo import BankInfo

@dataclass
class PersonalInfo:
    pass

@dataclass
class BankCustomer:
    personal_info: PersonalInfo
    bank_details: BankInfo

    def give_details(self) -> dict:
        selected_account_number = self.bank_details.accounts_number[0] if self.bank_details.accounts_number else None

        bank_details_info = {
            "bank_name": self.bank_details.bank_name,
            "holder_name": self.bank_details.holder_name,
            "accounts_number": self.bank_details.accounts_number,
            "credit_history": self.bank_details.credit_history,
        }

        personal_info = {
            "personal_info": self.personal_info.__dict__,
            "bank_details": bank_details_info,
        }

        return personal_info
