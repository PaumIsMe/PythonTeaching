def remove_dups_evo(arr):
    i = 0
    starting_index = 0

    for item in arr:
        while i >= 0 and i < len(arr):
            while i + 1 < len(arr) and item == arr[i + 1]:
                del arr[i + 1]
            i += 1
        starting_index += 1
        i = starting_index
        

    return arr

def remove_dups_paum(arr):

    # Go through i by idx and not item, this way we won't be going through already-deleted items.
    for item_idx in range(len(arr)): 

        # We will be shrinking the arr every time, so we have to check if we're past the end before proceeding
        if item_idx < len(arr):

            # Now we grab the item as before. This is a little longer line-wise to get 'item' but prevents going through already-deleted items
            item = arr[item_idx]

            # We start testing to see duplicates starting with the next item, item_idx works here without needing to keep track of a starting_idx
            i = item_idx + 1

            # >= 0 check is not necessary here, i will always be >= 0
            while i < len(arr): 

                # This is the biggest difference. Instead of doing a while loop in here, we can just seperate the two cases -
                #   1. The element is the same, and we don't increment i & delete
                #   2. The element isn't the same, and we do increment i
                # This does fundimentally the same thing, but imo is a little easier to read

                if item == arr[i]:
                    arr.pop(i)
                else:
                    i += 1
    
    return arr

# We also use arr.pop() instead of del because del deletes the first element, which gets even more confusing.
# In the original code if we had [3, 2, 3], del arr[2] => del 3 is actually deleting the *first* instance of 3, i.e. the 3 at idx 0
# Fortunately, it still works out, but is more complicated that it needs to be, and than you intended most likely
# In short, if you know the index, *always* use pop

for i in range(30000):
    remove_dups_evo([4, 2, 6, 7, 23, 2, 4, 7, 7, 7, 7, 9, 7, 7, 4, 2, 6, 7, 23, 2, 4, 7, 7, 7, 7, 9, 7, 7, 4, 2, 6, 7, 23, 2, 4, 7, 7, 7, 7, 9, 7, 7, 4, 2, 6, 7, 23, 2, 4, 7, 7, 7, 7, 9, 7, 7, 4, 2, 6, 7, 23, 2, 4, 7, 7, 7, 7, 9, 7, 7, 4, 2, 6, 7, 23, 2, 4, 7, 7, 7, 7, 9, 7, 7])