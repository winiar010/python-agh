# Liczby pitagorejskie


def is_pythagorean_numbers(a, b, c):
    """Checking is numbers are pythagorean's"""

    if a*a + b*b == c*c:
        return 1
    elif a*a + c*c == b*b:
        return 1
    elif b*b + c*c == a*a:
        return 1
    else:
        return 0