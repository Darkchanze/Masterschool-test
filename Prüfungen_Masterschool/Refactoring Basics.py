def input_of_number():
    """Asks for user-input as long as no number is given"""
    while True:
        check_sum_prime = input("Enter a number:")
        if check_sum_prime.isnumeric():
            check_sum_prime = int(check_sum_prime)
            return check_sum_prime
        else:
            print('Input is invalid, only whole numbers and no letters')


def is_sum_of_two_primes(check_sum_prime):
    """Checking which summation of 2 prime numbers will result in check_sum_prime"""
    if check_sum_prime % 2 == 1:
        return False
    for check_if_first_prime in range(2, check_sum_prime):
        first_number_is_prime = True
        # Check if check_if_second_prime is Prime
        smaller_numbers = 2
        while smaller_numbers < check_if_first_prime:
            if check_if_first_prime % smaller_numbers == 0:
                first_number_is_prime = False
            smaller_numbers += 1
        if first_number_is_prime:
            # check_if_first_prime is prime
            # Check if check_if_second_prime is Prime
            check_if_second_prime = check_sum_prime - check_if_first_prime
            if check_if_second_prime >= 2:
                second_number_is_prime = True
                smaller_numbers = 2
                while smaller_numbers < check_if_second_prime:
                    if check_if_second_prime % smaller_numbers == 0:
                        second_number_is_prime = False
                    smaller_numbers += 1
                if second_number_is_prime:
                    # Both numbers are Prime, now we Print them.
                    print(f"The number {check_sum_prime} equals to the sum of {check_if_first_prime} and {check_if_second_prime}")
    return True


def main():
    is_sum_of_two_primes(input_of_number())


if __name__ == "__main__":
    main()
