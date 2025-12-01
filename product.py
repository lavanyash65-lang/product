import pytest
def product_details(id, name, quantity,price):
    result = (
        f"Employee Name: {id}\n "
        f"Employee ID: {name}\n "
        f"Department: {quantity}\n "
        f"Salary: {price}"
    )
    return result
if __name__ == "__main__":
    id = "E1001"
    name = "alice"
    quantity = 2
    price = 50000
    print(product_details(id, name, quantity, price))
