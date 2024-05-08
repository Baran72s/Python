def bubble_sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if ascending:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Beispiel Liste zum Sortieren
unsorted_list = [64, 34, 25, 12, 22, 11, 90]

# Sortierung in aufsteigender Reihenfolge
sorted_list_ascending = bubble_sort(unsorted_list.copy(), ascending=True)
print("Sortierte Liste (aufsteigend):", sorted_list_ascending)

# Sortierung in absteigender Reihenfolge
sorted_list_descending = bubble_sort(unsorted_list.copy(), ascending=False)
print("Sortierte Liste (absteigend):", sorted_list_descending)
input()