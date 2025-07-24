

## yahi main bhulti hu sabse jyada
# Bubble Sort Implementation in Python
# Bubble Sort is a simple sorting algorithm that repeatedly steps through 
# the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the
# list is repeated until the list is sorted. The algorithm gets its name 
# from the way larger elements "bubble" to the top of the list.
# Bubble Sort is not a very efficient algorithm, especially for large lists, 
# but it is simple to understand and implement. It has a time complexity of O(n^2) in the average and worst case.    

n=int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    a=int(input("Enter element: "))
    arr.append(a)
print("Unsorted array:", arr)

def bubble_sort(arr):
    n=len(arr)
    for i  in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

