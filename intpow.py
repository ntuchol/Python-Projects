

def intpow(base, exponent):
    """
    Calculates the power of an integer using recursion.

    Args:
        base: The base integer.
        exponent: The exponent integer.

    Returns:
        The result of base raised to the power of exponent.
    """

    if exponent < 0:
      return 1 / intpow(base, -exponent)
    if exponent == 0:
        return 1
    else:
        return base * intpow(base, exponent - 1)
