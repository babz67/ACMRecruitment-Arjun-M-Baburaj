k = [5,2,9,1,5,6]
print("The list before sorting is:", k)

# Looping from 2nd element to end as we assume first element is already sorted
for i in range(1, len(k)):
    key = k[i]        # The element to be put into right position
    j = i - 1         # The element just before the one to be sorted into correct position

    # Move elements of k, that are greater than key 1 index forward
    while j >= 0 and k[j] > key:
        k[j + 1] = k[j]
        j -= 1      #moving one step left to repeat until it find a smaller element or a same element

    # Insert the key at the correct position
    k[j + 1] = key



print("The list after sorting is:", k)
