def print_catalogue(price1, price2, price3, contact):
    # Discounts in decimal fractions
    combo_discount = 0.10
    gift_discount = 0.25

    # Expressions & arithmetics
    combo12 = (price1 + price2) * (1 - combo_discount)
    combo23 = (price2 + price3) * (1 - combo_discount)
    combo13 = (price1 + price3) * (1 - combo_discount)
    gift = (price1 + price2 + price3) * (1 - gift_discount)

    # Function body & print statements
    print("Output:\n")
    print("Online Store")
    print("----------------------------")
    print("Product(S)\t\t\tPrice")
    print("Item 1\t\t\t\t", price1)
    print("Item 2\t\t\t\t", price2)
    print("Item 3\t\t\t\t", price3)
    print("Combo 1 (Item 1 + 2)\t\t", combo12)
    print("Combo 2 (Item 2 + 3)\t\t", combo23)
    print("Combo 3 (Item 1 + 3)\t\t", combo13)
    print("Combo 4 (Item1 + Item2 + Item3)\t", gift)
    print("\n____________________________")
    print("For delivery Contact:", contact)

# Calling the function
print_catalogue(200.0, 400.0, 600.0, "98764678899")
