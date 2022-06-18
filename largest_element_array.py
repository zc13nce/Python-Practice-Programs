# Python3 program to find maximum 
# in arr[] of size n

# python function to find maximum
# in arr[] of size n
def largest(arr,n):

    #Initialize maximum element
    max = arr[0]

    # traverse array elemetns from second
    # and compare elevery element with
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

# Driver Code
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print("Largest in given array is",Ans)

# This code is contributed by Smitha Dinesh Semwal
