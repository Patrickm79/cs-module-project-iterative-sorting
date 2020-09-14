# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # Find smallest element
        for j in range(cur_index + 1, len(arr)): # start at next element
            if arr[j] < arr[smallest_index]: # if smaller,
                smallest_index = j # mark as smallest_index

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index] # swap

    return arr


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    
    # Your code here
    pass_num = 1 # Keep track of the pass number to not check the elements that have already bubbled up
    did_swap = True

    while (did_swap): # Only keep going while swaps are being made
        did_swap = False

        for i in range(len(arr) - pass_num): # Loop through all the elements minus the pass number
            if arr[i] > arr[i + 1]: # if the next element is larger,
                arr[i], arr[i + 1] = arr[i + 1], arr[i] # then swap
                did_swap = True # Make note if we did at least one swap

        pass_num += 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here

    # Loop through values, initalize buckets.
    # Place each value in bucket by incrementing that index then construct list from bucket
    # First pass solution: Loop through buckets, adding the appropriate number of values to our result list
    # Second pass: Overwrite data in the list passed in by looping through the buckets.

    # If no maximum is passed in, let's find the maximum

    if not maximum:
        maximum = 0
        for value in arr:
            if value > maximum:
                maximum = value

    buckets = [0] * (maximum + 1) # allocate appropriate number of buckets

    for value in arr:
        if value < 0: # make sure to guard against negative integers
            return "Error, negative numbers not allowed in Count Sort"
        buckets[value] += 1

    index = 0

    for value, occurences in enumerate(buckets): # bucket index is the value, the int in the bucket is the number of occurences
        for _ in range(occurences): 
            arr[index] = value # overwrite input list with value
            index += 1 # increment index

    return arr
