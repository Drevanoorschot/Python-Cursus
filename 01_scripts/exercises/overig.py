# maak een functie die vertelt of een integer even of oneven is
# voorbeeld odd_or_even(7) == "odd"
# voorbeeld odd_or_even(4) == "even"
# tip: google modulo operator en hoe je hem kan gebruiken in Python
def odd_or_even(i):
    return "even" if i % 2 == 0 else "odd"


def odd_or_even2(j):
    if j % 2 == 0:
        return "even"
    else:
        return "odd"


def odd_or_even3(k):
    counter = 0
    even = True
    while counter != k:
        even = False if even else True
        counter += 1
    return "even" if even else "odd"


for l in range(1, 10):
    print("is {} even or odd?".format(l))
    print("sol 1: {}".format(odd_or_even(l)))
    print("sol 2: {}".format(odd_or_even2(l)))
    print("sol 3: {}\n".format(odd_or_even3(l)))

print(odd_or_even(10000000))
print(odd_or_even2(10000000))
print(odd_or_even3(100000000))
