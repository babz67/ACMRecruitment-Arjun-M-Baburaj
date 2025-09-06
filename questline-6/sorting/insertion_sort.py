k = [5,2,9,1,5,6]
print("The list before sorting is:", k)

# Looping through the list from 1st index to end
for i in range(1, len(k)):
    key = k[i]        # The element to be put into right position
    j = i - 1

    # Move elements of k, that are greater than key to next position ahead of their current position
    while j >= 0 and k[j] > key:
        k[j + 1] = k[j]
        j -= 1

    # Insert the key at the correct position
    k[j + 1] = key



print("The list after sorting is:", k)
