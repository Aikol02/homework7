def binary_search(arr):
    a = len(arr)

    for num in range(a-1):
        for j in range(0, a - num - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


list_ = [1, 5, 7, 3, 8, 2, 9, 4, 6]
binary_search(list_)
print(f"binary search {list_}")


def bubble_sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]


list1 = [2, 5, 1, 7, 6, 9, 8, 3, 4]
bubble_sort(list1)
print(f"bubble sort {list1}")
