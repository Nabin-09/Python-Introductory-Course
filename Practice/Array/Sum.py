def largest_Element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
arr = list(map(int, input("Enter the elements : ").split()))
largest = largest_Element(arr)
if largest is not None:
    print("The largest element is :",largest)