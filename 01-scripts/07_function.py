def largest_of_three(x, y, z):
    if x >= y and x >= z:
        return "first"
    elif y >= x and y >= z:
        return "second"
    else:
        return "third"


a = 1
b = 5
c = 6

d = 6
e = 1
f = 9

print(largest_of_three(a, b, c) + " is largest")
print(largest_of_three(d, e, f) + " is largest")
print(largest_of_three(b, a, e) + " is largest")
