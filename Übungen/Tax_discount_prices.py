def get_prices_and_percent_from_user():

    input_line = input("Enter the prices: ")
    list_of_prices_str = input_line.split(",")
    list_of_prices_int = []
    for price in list_of_prices_str:
        list_of_prices_int.append(int(price))
    discount_percent = int(input("Enter the discount percent: "))
    discount_or_tax = int(input('Enter 0 for discount or 1 for tax'))
    return list_of_prices_int, discount_percent, discount_or_tax


def apply_discount_on_price(price, discount_percent):
    return price * (1-discount_percent/100)

def apply_tax_on_price(price, tax_percent):
    return price * (1+tax_percent/100)


def apply_discount_on_a_list_of_prices(price_list, discount_percent, discount_or_tax):
    list_of_discounted_prices = []
    if discount_or_tax == 0:
        for price in price_list:
            list_of_discounted_prices.append(apply_discount_on_price(price, discount_percent))
        return list_of_discounted_prices
    elif discount_or_tax == 1:
        for price in price_list:
            list_of_discounted_prices.append(apply_tax_on_price(price, discount_percent))
        return list_of_discounted_prices



def main():
    list_of_prices, discount_percent, discount_or_tax = get_prices_and_percent_from_user()
    list_of_discounted_prices = apply_discount_on_a_list_of_prices(list_of_prices, discount_percent, discount_or_tax)
    print(list_of_discounted_prices)


if __name__ == "__main__":
    main()