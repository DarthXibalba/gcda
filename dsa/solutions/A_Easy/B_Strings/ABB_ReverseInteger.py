def reverse_integer(x: int) -> int:
    multiplier = 1
    if x < 0:
        multiplier = -1
    
    y = 0
    x *= multiplier

    while (x > 0):
        y *= 10
        y += x % 10
        x = x // 10
    
    return y * multiplier
