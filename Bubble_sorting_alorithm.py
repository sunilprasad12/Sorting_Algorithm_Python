# Bubble sort alorithm

def bubble(list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False  # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a


print(bubble([7, 2, 1, 9, 3, 6, 5, 8, 4]))