import sort_helpers as sh

def selection_sort(lst):
    length = len(lst)
    for i in range(0, length):
        min = i
        for j in range(i + 1, length):
            if lst[j] < lst[min]:
                min = j
        sh.swap(lst, i, min)

lst = sh.random_list(100, 1, 1000)
selection_sort(lst)
print(lst)
