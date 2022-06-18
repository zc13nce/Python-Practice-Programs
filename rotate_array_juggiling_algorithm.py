# Function to left rotate arr[] of size n by d
def leftRotate(arr, d, n):
    for i in range(gcd(d,n)):

        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

# UTILITY FUNCTIONS
# function to print an array
def printArray(arr, size):
    for i in range(size):
        print ("%d" % arr[i], end=" ")

# Function to get gcd of a and b
def gcd(a, b):
    if b == 0:
        return a;
    else:
        return gcd(b, a%b)

# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

# This code is contributed by Shreyanshi Arun

# Python program using the List
# slicing approach to rotate the array
def rotateList(arr, d,n):
    arr[:] = arr[d:n] + arr[0:d]
    return arr
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6,]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr)))

# this code is contributed by virusbuddah
# ^^^^_++++++
