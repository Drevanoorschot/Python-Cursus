a = input("give me a number\n")
b = input("give me another number\n")

print("sum of inputs: {a} + {b} = {ab}".format(a=a, b=b, ab=int(a) + int(b)))

print("\nDid you know: input() functions are of type {t}\n".format(t=type(a)))
