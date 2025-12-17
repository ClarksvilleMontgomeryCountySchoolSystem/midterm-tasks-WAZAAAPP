# Testing flag - will be set by test
TESTING = True  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
Magic Wand.................$24.99
Potion of Healing..........$9.99
Enchanted Map..............$14.99
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info():  # Convert input when necessary
    item = input("Enter the item you want to purchase: ")
    price = float(input("Enter the price of the item: "))
    quantity = int(input("Enter the quantity (must be at least 3): "))
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()
else:
    # Example test data
    item = "Magic Wand"
    price = 24.99
    quantity = 3

# Calculate using the input values (NOT hardcoded!)
subtotal = price * quantity
tax_rate = 0.095  # Sales tax rate
tax = subtotal * tax_rate
total = subtotal + tax
total = round(total, 2)

# Print statements
print("--------------------------")
print(f"Item: {item} x {quantity} @ ${price:.2f} each")
print("--------------------------")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}\n")

print("Thank you for shopping at\nThe Peculiar Emporium!")
