def product_info(product_id, name, quantity, price):
    return (
        f"Product ID: {product_id}\n"
        f"Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )

if name == "main":
    product_id = "P102"
    name = "Keyboard"
    quantity = 5
    price = 799.50

    print("Product Details:\n")
    print(product_info(product_id, name, quantity, price))
