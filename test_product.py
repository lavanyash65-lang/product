from product import product_info

def test_product_info():
    expected_output = (
        "Product ID: P102\n"
        "Name: Keyboard\n"
        "Quantity: 5\n"
        "Price: 799.5"
    )

    assert product_info("P102", "Keyboard", 5, 799.5) == expected_output
