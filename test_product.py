from product import product_details
def test_product_details():
    expected_output = (
        "product ID: E1001\n "
        "product name: alice\n "
        "quantity: 2\n "
        "price: 50000"
    )
    assert product_details("E1001", "alice", 2, 55000) == expected_output
        