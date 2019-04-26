import sort_helpers as sh

def bubble_sort(list):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(0, len(list) - 1):
            if list[i + 1] < list[i]:
                sh.swap(list, i, i + 1)
                swapped = True

list = sh.random_list(10, 1, 100)
print(list)
bubble_sort(list)
print(list)
