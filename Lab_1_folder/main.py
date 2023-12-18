import json
from collections import namedtuple

# Define namedtuples for Operator and Customer
Operator = namedtuple("Operator", ["ID", "talking_charge", "message_cost", "network_charge", "discount_rate"])
Customer = namedtuple("Customer", ["id", "name", "age", "limiting_amount", "operator_ptr", "bill"])

class Bill:
    def __init__(self, limiting_amount):
        self.limiting_amount = limiting_amount
        self.current_debt = 0.0

    def check(self, amount):
        return self.current_debt + amount <= self.limiting_amount

    def add(self, amount):
        self.current_debt += amount

    def pay(self, amount):
        self.current_debt -= amount

    def change_the_limit(self, amount):
        self.limiting_amount = amount

def print_customers_and_operators(customers, operators):
    print("Customers:")
    for customer in customers:
        print(
            f"ID: {customer.id}, Name: {customer.name}, Age: {customer.age}, Limit: {customer.limiting_amount}")

    print("\nOperators:")
    for oper in operators:
        print(f"ID: {oper.ID}, Talking Charge: {oper.talking_charge}, Message Cost: {oper.message_cost}, "
              f"Network Charge: {oper.network_charge}, Discount Rate: {oper.discount_rate}")
    print()



class CustomerClass:
    def __init__(self, id, name, age, limiting_amount, operator_ptr, bill):
        self.id = id
        self.name = name
        self.age = age
        self.limiting_amount = limiting_amount
        self.operator_ptr = operator_ptr
        self.bill = bill

    def talk(self, minutes, other):
        cost = minutes * self.operator_ptr.talking_charge
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} was talking with {other.name} during {minutes} minutes for {cost} dollars.")
        else:
            print("The call could not be made: there are not enough funds in the account.")

    def message(self, quantity, other):
        cost = quantity * self.operator_ptr.message_cost
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} sent {quantity} messages to {other.name} for {cost} dollars.")
        else:
            print("Failed to send messages: insufficient funds in account.")

    def connection(self, amount):
        cost = amount * self.operator_ptr.network_charge
        if self.bill.check(cost):
            self.bill.add(cost)
            print(f"{self.name} used the Internet for {amount} MB for {cost} dollars.")
        else:
            print("Could not connect to the Internet: insufficient funds in the account.")

    def set_limiting_amount(self, amount):
        self.limiting_amount = amount

def main():
    with open("file.json") as input_file:
        data = json.load(input_file)

    # Create lists of customers and operators using list comprehension
    customers = [
        CustomerClass(customer_data["id"], customer_data["name"], customer_data["age"],
                      customer_data["limit"], None, None)
        for customer_data in data["customers"]
    ]

    operators = [
        Operator(operator_data["id"], operator_data["talkingCharge"], operator_data["messageCost"],
                 operator_data["networkCharge"], operator_data["discountRate"])
        for operator_data in data["operators"]
    ]

    print_customers_and_operators(customers, operators)

    # Perform operations if at least two customers are available
    if len(customers) >= 2:
        customer1, customer2 = customers[:2]

        # Set operator pointers for customers
        customer1.operator_ptr = operators[0]
        customer1.bill = Bill(customer1.limiting_amount)

        customer2.operator_ptr = operators[1]
        customer2.bill = Bill(customer2.limiting_amount)

        # Customer 1 activities
        customer1.talk(15, customer2)  # Customer1 talks with customer2 for 15 minutes
        customer1.message(8, customer2)  # Customer1 sends 8 messages to customer2
        customer1.connection(500)  # Customer1 uses 500 MB of internet
        customer1.bill.pay(70)  # Customer1 pays a part of the bill, e.g., $70
        customer1.operator_ptr = customer1.operator_ptr._replace(
            talking_charge=0.12)  # Customer1's talking charge is adjusted
        customer1.set_limiting_amount(300)  # Customer1 increases the account limit to $300

        # Customer 2 activities
        customer2.talk(8, customer1)  # Customer2 talks with customer1 for 8 minutes
        customer2.message(5, customer1)  # Customer2 sends 5 messages to customer1
        customer2.connection(150)  # Customer2 uses 150 MB of internet
        customer2.bill.pay(20)  # Customer2 pays a part of the bill, e.g., $20
        customer2.operator_ptr = customer2.operator_ptr._replace(
            talking_charge=0.2)  # Customer2's talking charge is adjusted
        customer2.set_limiting_amount(250)  # Customer2 decreases the account limit to $250

    else:
        print("Error: At least two customers are expected in the JSON data.")

if __name__ == "__main__":
    main()
