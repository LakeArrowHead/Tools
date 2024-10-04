"""
This is a combinations calculator.
"""

def cal_factorial(n):

    """
    Calculates n!
    :rtype: int
    """

    if n == 1:
        return n
    
    return n * cal_factorial(n - 1)


def cal_combinations ():

    """
    Calculates n!/(r! * (n - r)!)
    rtype: int
    """

    n = int(input("n = "))
    r = int(input("r = "))

    result = cal_factorial(n) / ((cal_factorial(r)) * cal_factorial(n-r))
    print(result)

    return result


def main():
    cal_combinations()


if __name__ == "__main__":
    main()