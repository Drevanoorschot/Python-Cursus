# maak een functie die een groet generereerd
# voorbeeld: greet("Dré") == "hallo Dré"
def greet(name):
    return "hallo " + name


def greet2(name):
    return "hallo {name}".format(name=name)


# maak een functie die kijkt of twee strings even lang zijn
# voorbeeld equal_length("woord", "woorden") == False
# voorbeeld equal_length("woord", "draad") == True
# tip: de len(string) functie geeft de lengte van een string
def equal_length(s1, s2):
    return len(s1) == len(s2)


def equal_length2(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 == l2:
        return True
    else:
        return False


name = "Dré"
surname = "van Oorschot"
str3 = "ABC"
print(greet(name))
print(greet2(name))

print(greet2(name + " " + surname))

print(equal_length(name, surname))
print(equal_length2(name, surname))

print(equal_length(name, str3))
print(equal_length2(name, str3))