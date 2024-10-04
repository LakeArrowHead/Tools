"""
This is a combinations calculator.
"""


def take_input():
    
    """
    Asks user for input.
    :rtype: tuple
    """

    n = int(input("n = "))
    r = int(input("r = "))
    
    return (n, r)


def cal_factorial(n):

    """
    Calculates n!
    :rtype: int
    """

    if n == 1 or n == 0:
        return 1
    
    return n * cal_factorial(n - 1)


def cal_combinations(n, r):

    """
    Calculates n! / (r! * (n - r)!)
    rtype: int
    """

    result = int(cal_factorial(n) / ((cal_factorial(r)) * cal_factorial(n-r)))

    return result


def display_output(factorial, result):

    """
    Prints the factorial of n and the result of (n choose r).
    """

    print(f"n! = {factorial}")
    print(f"n choose r = {result}")
    

def main():

    """
    Main frunction.
    """

    input = take_input()
    factorial = cal_factorial(input[0])
    result = cal_combinations(input[0], input[1])
    display_output(factorial, result)


if __name__ == "__main__":
    main()