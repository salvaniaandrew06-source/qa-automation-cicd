import pytest
from example_app import add_to_cart, calculate_total, apply_discount, apply_discount2

def test_add_to_cart():
 cart=[]
 updated_cart=add_to_cart(cart, "laptop")
 assert "laptop" in updated_cart

def test_calculate_total():
 prices=[100,200,300]
 total=calculate_total(prices)
 assert total == 600

def test_apply_discount():
 total=1000
 discounted=apply_discount(total,10)
 assert discounted == 900

def test_apply_discount2():
 total=1000
 discounted=apply_discount2(total,10)
 assert discounted == 900