# N-ta potęga


def power(x, n):
    """Calculation of power"""

    result = 1

    for _ in range(n):
        result *= x

    return result