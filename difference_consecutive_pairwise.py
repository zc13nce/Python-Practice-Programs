# Python 3 program to implement
# the above approach

# Function to calculate the 
# differenece of consecutive pairwise
# elemenets in a set
def display_difference(s):

    # Printing difference between
    # consecutive elements in a aset
    itr1 = 0
    itr2 = 0
    while (1):
      itr2 += 1
      if (itr2 >= len(s)):
          break
      print((list(s)[itr2] - list(s)[itr1]), end = " ")
      itr1 += 1
  
# Driver code
if __name__ == "__main__":

    # Declaring the set
    s = set([8, 5, 4, 3, 15, 20])

    # Invoking the display_difference()
    # function
    display_difference(s)

    # This code is contributed by ukasp
    
