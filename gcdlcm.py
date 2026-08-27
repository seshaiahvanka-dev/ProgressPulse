
import math

def gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a*b) // gcd
    return gcd, lcm

print("GCD and LCM of 12 and 18:", gcd_lcm(12, 18))
