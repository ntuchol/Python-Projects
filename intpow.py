

def intpow(base, exponent):
    if exponent < 0:
      return 1 / intpow(base, -exponent)
    if exponent == 0:
        return 1
    else:
        return base * intpow(base, exponent - 1)
