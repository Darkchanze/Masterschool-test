def input_of_number():
    """Asks for user-input as long as no number is given"""
    while True:
        check_sum_prime = input("Enter a number:")
        if check_sum_prime.isnumeric():
            check_sum_prime = int(check_sum_prime)
            return check_sum_prime
        else:
            print('Input is invalid, only whole numbers and no letters')

def check_number_prime(check_if_prime):
    """Checking  if a number is Prime and return true or False"""
    number_is_prime = True
    smaller_numbers = 2
    while smaller_numbers < check_if_prime:
        if check_if_prime % smaller_numbers == 0:
            number_is_prime = False
        smaller_numbers += 1
    return number_is_prime


def is_sum_of_two_primes(check_sum_prime):
    """Checking which summation of 2 prime numbers will result in check_sum_prime"""
    set_of_used_numbers = set()
    list_of_prime_pairs = []
    if check_sum_prime % 2 == 1:
        return
    for check_if_first_prime in range(2, check_sum_prime):
        if check_number_prime(check_if_first_prime):
            # check_if_first_prime is prime
            check_if_second_prime = check_sum_prime - check_if_first_prime
            if check_if_second_prime >= 2:
                if check_number_prime(check_if_second_prime):
                    # Both numbers are Prime, now we Print them
                    if (check_if_second_prime not in set_of_used_numbers):  #Check if we already have that numbers in our list
                        list_of_prime_pairs.append((check_if_first_prime, check_if_second_prime)) #Numbers are new, so we add them in a touple to our list
                        set_of_used_numbers.add(check_if_first_prime)
    return list_of_prime_pairs


def main():
    number_user_input = input_of_number()
    list_of_prime_pairs = is_sum_of_two_primes(number_user_input)
    for pair in list_of_prime_pairs:
        print(f"The number {number_user_input} equals to the sum of {pair[0]} and {pair[1]}")


if __name__ == "__main__":
    main()