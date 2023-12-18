from cryptography.fernet import Fernet
import hashlib


def golden_credit_card(cls):
    class GoldenCreditCard(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.credit_limit *= 2
            self.grace_period += 60
            self.encryption_key = kwargs.get("encryption_key")

    return GoldenCreditCard

def corporate_credit_card(cls):
    class CorporateCreditCard(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.credit_limit *= 1.5
            self.grace_period += 30
            self.encryption_key = kwargs.get("encryption_key")

    return CorporateCreditCard



class CreditCard:
    def __init__(self, client: str, account_number: str, credit_limit: float, grace_period: int, cvv: str, encryption_key: bytes):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self.encryption_key = encryption_key
        self.cvv = self.encrypt(cvv, encryption_key)


    def give_details(self) -> dict:
        return {
            "client": self.client,
            "account_number": self.account_number,
            "credit_limit": self.credit_limit,
            "grace_period": self.grace_period,
            "cvv": self.decrypt(self.cvv, self.encryption_key),
        }

    def encrypt(self, value: str, encryption_key: bytes) -> bytes:
        cipher = Fernet(encryption_key)
        encrypted_value = cipher.encrypt(value.encode())
        return encrypted_value

    def decrypt(self, encrypted_value: bytes, encryption_key: bytes) -> str:
        cipher = Fernet(encryption_key)
        decrypted_value = cipher.decrypt(encrypted_value)
        return decrypted_value.decode()

@golden_credit_card
class GoldenCreditCard(CreditCard):
    pass

@corporate_credit_card
class CorporateCreditCard(CreditCard):
    pass



