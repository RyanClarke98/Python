
def divisible(numerator: int, denominator: int)->bool:
    return numerator % denominator == 0

print(divisible(30,4)) # This will turn true when it is possible to divide the numerator by the denmonitor without a remainder
                       # The function returns with false as there is remainder of .5 