from math import sqrt

def solve_for_addition(sequence: list[int]) -> int:

    value = list()
    pattern = 0

    for index, number in enumerate(sequence):

        if index == 0:
            continue

        previous_number = sequence[index - 1]
        difference = number - previous_number

        value.append(difference)

    if len(set(value)) == 1:
        pattern = value[0]

    return pattern


def solve_for_multiplication(sequence: list[int]) -> int:

    value = list()
    pattern = 0

    for index, number in enumerate(sequence):

        if index == 0:
            continue

        previous_number = sequence[index - 1]
        difference = round(number / previous_number, 2)

        value.append(difference)

    if len(set(value)) == 1:
        pattern = value[0]

    return pattern


def solve_for_squares(sequence: list[int], range_lower_bound=1, range_upper_bound=11, exponent=2) -> int:

    powers_in_range = [x**exponent for x in range(range_lower_bound, range_upper_bound)]
    exponent_used = exponent

    for index, number in enumerate(sequence):

        if index == 0:
            continue

        if number not in powers_in_range:
            exponent_used = 0
            break

    return exponent_used


def solve_for_addition_results_pattern(sequence: list[int]) -> int:

    value = list()

    for index, number in enumerate(sequence):

        if index == 0:
            continue

        previous_number = sequence[index - 1]
        difference = number - previous_number

        value.append(difference)

    pattern = solve_for_addition(value)

    return pattern


def is_prime(number: int) -> bool:

    assessment = True

    for each in range(2, int(sqrt(number))+1):

        if number % each == 0:
            assessment = False
            break

    return assessment


def func_main():

    sequence = [4, 6, 9, 13, 18]
    result = solve_for_addition(sequence)

    print()

    if not result:
        print("Addition:\t\tNo pattern")
    else:
        print(f"Addition:\t\t{result} PATTERN FOUND")

    result = solve_for_multiplication(sequence)

    if not result:
        print("Multi:\t\t\tNo pattern")
    else:
        print(f"Multi:\t\t\t{result} PATTERN FOUND")

    exponent = 2
    lower = 1
    upper = 21
    result = solve_for_squares(sequence, range_lower_bound=lower, range_upper_bound=upper, exponent=exponent)

    if not result:
        print(f"Exponent {exponent}:\t\tNo pattern")
    else:
        print(f"Exponent {result}:\t\tPATTERN FOUND")

    exponent = 3
    lower = 1
    upper = 21
    result = solve_for_squares(sequence, range_lower_bound=lower, range_upper_bound=upper, exponent=exponent)

    if not result:
        print(f"Exponent {exponent}:\t\tNo pattern")
    else:
        print(f"Exponent {result}:\t\tPATTERN FOUND")

    result = solve_for_addition_results_pattern(sequence)

    if not result:
        print("Results add:\tNo pattern")
    else:
        print(f"Results add:\t{result} PATTERN FOUND")

    number = 97
    print(f"\nNumber \'{number}\' is prime: {is_prime(number)}")

    print()


if __name__ == "__main__":
    func_main()
