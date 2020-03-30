x = 0
y = 0
while x < 10:
    while y < 10:
        print("(" + str(x) + ", " + str(y) + ")")
        # print("({}, {})".format(x, y))

        # coord = "({}, {})"
        # print(coord.format(x, y))

        # coord = "({xx}, {yy})"
        # print(coord.format(xx=x, yy=y))
        y += 1
    y = 0
    x += 1
