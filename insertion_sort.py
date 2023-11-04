def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [64, 25, 12, 22, 11]
print("Dizi sıralanmadan önce:")
print(arr)

insertion_sort(arr)

print("Dizi sıralandıktan sonra:")
print(arr)
