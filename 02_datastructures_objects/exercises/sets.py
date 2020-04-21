# maak een functie die de intersection pakt van een lijst van sets (https://i.imgur.com/EgIZHSC.png)
# voorbeeld: list_intersection([{1,2,3}, {3,4,5}, {4,3,2}]) == {3}
def list_intersection(set_list):
    if len(set_list) == 0:
        return set()
    if len(set_list) == 1:
        return set_list[0]
    res = set_list[0] & set_list[1]
    for i in range(2, len(set_list)):
        res &= set_list[i]
    return res


# maak een functie die van een set een gesorteerde lijst maakt
# voorbeeld set_to_list({53,5,6,2,25,214}) == [2, 5, 6, 25, 53, 214]
def set_to_list(set):
    return sorted(list(set))
