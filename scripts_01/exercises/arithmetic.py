from math import factorial

# maak een functie die twee integers vermenigvuldigd ZONDER de "*" operator te gebruiken
# voorbeeld multiply(3, 3) == 3 * 3
from sympy import isprime


def multiply(i1, i2):
    a_i1 = abs(i1)
    a_i2 = abs(i2)
    c = 0
    s = 0
    (v, t) = (a_i1, a_i2) if a_i1 < a_i2 else (a_i2, a_i1)
    while c < t:
        s += v
        c += 1
    return s if (i1 >= 0) == (i2 >= 0) else -s


for i in range(-10, 10):
    for j in range(-10, 10):
        if multiply(i, j) != i * j:
            print("multiply error: {i} * {j} != {mul}".format(i=i, j=j, mul=multiply(i, j)))


# maak een functie die de factorial van een getal uitrekent
# voorbeeld: factorial(5) == 5 * 4 * 3 * 2 * 1
# extra: gebruik geen loop maar recursie
def factorial_rec(i):
    if i == 0:
        return 1
    else:
        return fac_rec_help(i, 1)


def fac_rec_help(i, agg):
    if i != 1:
        return fac_rec_help(i - 1, agg * i)
    else:
        return agg


def factorial_loop(i):
    agg = 1
    while i > 0:
        agg *= i
        i -= 1
    return agg


for i in range(0, 10):
    if factorial_rec(i) != factorial(i):
        print("recursive factorial error: {i}! != {fac}".format(i=i, fac=factorial_rec(i)))
    if factorial_loop(i) != factorial(i):
        print("recursive factorial error: {i}! != {fac}".format(i=i, fac=factorial_loop(i)))


# maak een functie die checkt of twee integers deelbaar zijn door elkaar
# voorbeeld: divisable_by(4, 2) == True
# voorbeeld: divisable_by(5, 2) == False
def divisable_by(i1, i2):
    return i1 % i2 == 0


def divisable_by2(i1, i2):
    return i1 // i2 == i1 / i2


for i in range(-10, 10):
    for j in [x for x in range(-10, 10) if x != 0]:
        if divisable_by(i, j) != divisable_by2(i, j):
            print("divisisable function error for {i} divisable by {j}".format(i=i, j=j))


# maak een functie die alle delers van een integer print (de functie hoeft dus niets te returnen)
# voorbeeld: divisors(10) -> 1, 2, 5, 10
# voorbeeld: divisors(7) -> 1, 7
def divisors_of(i):
    print("divisors of " + str(i))
    for j in range(1, i // 2 + 1):
        if divisable_by(i, j):
            print(j)


divisors_of(100)


# maak een functie die aangeeft of een integer een priemgetal (deelbaar door 1 en zichzelf) is.
# voorbeeld: is_prime(7) == True
# voorbeeld: is_prime(10) == False
def is_prime(i):
    if i == 0 or i == 1:
        return False
    for j in range(2, i // 2 + 1):
        if divisable_by(i, j):
            return False
    return True


for i in range(0, 100):
    if isprime(i) != is_prime(i):
        print("is prime function error for " + str(i))