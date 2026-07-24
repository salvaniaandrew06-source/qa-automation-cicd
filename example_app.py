def add_to_cart(cart, item):
 cart.append(item)
 return cart


def calculate_total(prices):
 return sum(prices)

def apply_discount(total, discount_percent):
 return total - (total * discount_percent/100)

def apply_discount2(total, discount_percent):
 return total - (total * discount_percent/100)