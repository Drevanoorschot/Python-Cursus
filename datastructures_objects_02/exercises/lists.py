def divisable_by(i1, i2):
    return i1 % i2 == 0


def is_prime(i):
    if i == 0 or i == 1:
        return False
    for j in range(2, i // 2 + 1):
        if divisable_by(i, j):
            return False
    return True


# maak een functie die een lijst van priem getallen maakt tot aan een bepaalde 'limit'
# voorbeeld: prime_list(13) == [2, 3, 5, 7, 11, 13]
def prime_list(limit):
    res = []
    for i in range(2, limit + 1):
        if is_prime(i):
            res.append(i)
    return res


# maak een functie die checkt of een item in een list voor komt.
# extra 1: maak geen gebruik van de 'in' keyword
# extra 2: maak de assumptie dat de lijst gesorteerd is (of sorteer de lijst eerst) en impelementeer binary search:
#   https://en.wikipedia.org/wiki/Binary_search_algorithm
# extra 3: Kun je binary search recursief maken?
# voorbeeld: contains([1,6,34,6,34,235,43,2], 2) == True
# voorbeeld: contains([1,6,34,6,34,235,43,2], 100) == False
def contains(list, item):
    list.sort()
    return bin_search(list, item)


def bin_search(list, item):
    print(list)
    if len(list) == 1:
        return list[0] == item
    if len(list) == 0:
        return False
    mid = len(list) // 2
    if item < list[mid]:
        return bin_search(list[:mid], item)
    elif item > list[mid]:
        return bin_search(list[mid:], item)
    else:
        return True


# maak een eigen sorteer algorithme voor een lijst.
# een vrij simpel algorithme is bubble sort:
# https://www.youtube.com/watch?v=xli_FI7CuzA
# een iets complexer algorithme (maar een stuk sneller dan bubble sort), is merge sort:
# https://www.youtube.com/watch?v=4VqmGXwpLqc
# voorbeeld: sort([1, 5, 2, 8]) == [1, 2, 5, 8]
def bubble_sort(list):
    n = len(list)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            print(list)
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves
        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    print(arr)
