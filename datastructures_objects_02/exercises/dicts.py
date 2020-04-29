# maak een functie die een dictionary van kwadraten generereert tot de 'limit'
# voorbeeld: squares(5) == {1:1, 2:4, 3:9, 4:16, 5:25}
def squares(limit):
    res = {}
    for i in range(1, limit + 1):
        res.update({i: i ** 2})
    return res


auto = {
    "merk": "Ford",
    "type": "Fiesta",
    "deuren": 3,
    "motor": {
        "cylinders": 6,
    },
    "kleuren": {"blauw", "geel", "grijs"}
}


# maak een functie die een motor dict genereert zoals het voorbeeld hierboven
# voorbeeld: create_motor(cylinders=8) == {"motor": {"cylinders": 8}}
def create_motor(cylinders):
    if type(cylinders) != int:
        raise TypeError("argument 'cylinders' must be of type int")
    return {"motor": {"cylinders": cylinders}}


# maak een functie die een kleuren dict genereert zoals het voorbeeld hierboven
# voorbeeld: create_motor(kleuren={"rood", "geel"}) == {"rood", "geel"}}
def create_kleuren(kleuren):
    if type(kleuren) != set:
        raise TypeError("argument 'kleuren' must be of type set")
    for kleur in kleuren:
        if type(kleur) != str:
            raise TypeError("argument 'kleuren' contains {i} that is of type {t} and should be str".format(
                i=kleur,
                t=type(kleur)
            ))
    return {"kleuren": kleuren}


# maak een functie die een auto dict genereert zoals het voorbeeld hierboven
# voorbeeld:
# input: create_car(name="Ferrari",
#                   type="Enzo",
#                   deuren=2,
#                   motor=create_motor(8),
#                   kleuren=create_kleuren({"rood"})
# output: {
#     "merk": "Ferrari",
#     "type": "Enzo",
#     "deuren": 2,
#     "motor": {
#         "cylinders": 8,
#     },
#     "kleuren": {"rood"}
# }
def create_car(name: str, type: str, deuren: int, motor: dict, kleuren: dict):
    return {
        "name": name,
        "type": type,
        "deuren": deuren,
        "motor": motor,
        "kleuren": kleuren
    }
