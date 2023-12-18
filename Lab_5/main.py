from fastapi import FastAPI, Request, HTTPException
from BankInfo import BankInfo
from BankCustomer import BankCustomer, PersonalInfo
from Credit_Cart import GoldenCreditCard, CorporateCreditCard
from cryptography.fernet import Fernet

app = FastAPI()

encryption_key = Fernet.generate_key()


golden_card = GoldenCreditCard(
    client="John Doe",
    account_number="1234567890123456",
    credit_limit=5000.0,
    grace_period=30,
    cvv="123",
    encryption_key=encryption_key
)


corporate_card = CorporateCreditCard(
    client="Jane Doe",
    account_number="9876543210987654",
    credit_limit=7000.0,
    grace_period=45,
    cvv="456",
    encryption_key=encryption_key
)

golden_card_details = golden_card.give_details()
corporate_card_details = corporate_card.give_details()

bank_info = BankInfo(
    bank_name="My Bank",
    holder_name="John Doe",
    accounts_number=["1234567890123456", "9876543210987654"],
    credit_history={
        'golden_card': {
            'account_number': golden_card_details['account_number'],
            'credit_limit': golden_card_details['credit_limit'],
            'grace_period': golden_card_details['grace_period'],
        },
        'corporate_card': {
            'account_number': corporate_card_details['account_number'],
            'credit_limit': corporate_card_details['credit_limit'],
            'grace_period': corporate_card_details['grace_period'],
        },
    }
)


personal_info = PersonalInfo()


bank_customer = BankCustomer(
    personal_info=personal_info,
    bank_details=bank_info
)


@app.get("/")
async def read_root():
    return {"message": "Hello, welcome to the FastAPI application!"}


@app.post("/enhanced_credit_card")
async def get_enhanced_credit_card():
    return {"enhanced_credit_card_details": golden_card.give_details()}


@app.post("/bank_customer")
async def get_bank_customer():
    return {"bank_customer_details": bank_customer.give_details()}


#python -m uvicorn main:app --reload
#http://127.0.0.1:8000/docs
