from math import isqrt
import numpy as np
import matplotlib.pyplot as plt

PRIME_AMT =100000
R_MAX = 10000
primes = []

def is_prime(n):
    if n < 0:
        pass

    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return False
        
    return True


def prime_bounds(b):
    for i in range(2,b):
        if is_prime(i):
            primes.append(i)
    print(primes)
    return primes

prime_bounds(PRIME_AMT)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(primes, primes, s=1)
ax.set_rmax(R_MAX)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Polar Spiral of Primes", va='bottom')
plt.savefig('polarspiral.png')



    
