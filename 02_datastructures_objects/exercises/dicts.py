# maak een functie die een dictionary van kwadraten generereert tot de 'limit'
# voorbeeld: squares(5) == {1:1, 2:4, 3:9, 4:16, 5:25}
def squares(limit):
    pass


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
    pass


# maak een functie die een kleuren dict genereert zoals het voorbeeld hierboven
# voorbeeld: create_motor(kleuren={"rood", "geel"}) == {"rood", "geel"}}
def create_kleuren(cylinders):
    pass


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
def create_car(name, type, deuren, motor, kleuren):
    pass
