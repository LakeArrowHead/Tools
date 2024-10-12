"""
This is a combinations calculator.
"""


def take_input():
    
    """
    Asks user for input.
    :rtype: tuple
    """

    n = int(input("Type 0 to quit. n = "))
    r = int(input("Type 0 to quit. r = "))
    
    if n == 0 or r == 0:
        return 'Quit'
    
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


def display_output(factorial, result, n, r):

    """
    Prints the factorial of n and the result of (n choose r).
    """

    print(f"{n}! = {factorial}")
    print(f"{n} choose {r} = {result}")
    

def main():

    """
    Main frunction.
    """

    input = take_input()
    while input != 'Quit':
        n = input[0]
        r = input[1]
        factorial = cal_factorial(n)
        result = cal_combinations(n, r)
        display_output(factorial, result, n, r)
        input = take_input()
    print('Quiting.')


if __name__ == "__main__":
    main()
