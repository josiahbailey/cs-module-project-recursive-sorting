# TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = [0] * elements

#     for item1, item2 in zip(arrA, arrB):
#         merged_arr.append(item1)
#         merged_arr.append(item2)

#     return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        Left = arr[:mid]
        Right = arr[mid:]
        index_left = 0
        index_right = 0
        index_other = 0

        merge_sort(Left)
        merge_sort(Right)

        while index_left < len(Left) and index_right < len(Right):
            if Left[index_left] < Right[index_right]:
                arr[index_other] = Left[index_left]
                index_left += 1
            else:
                arr[index_other] = Right[index_right]
                index_right += 1
            index_other += 1

        while index_left < len(Left):
            arr[index_other] = Left[index_left]
            index_left += 1
            index_other += 1

        while index_right < len(Right):
            arr[index_other] = Right[index_right]
            index_right += 1
            index_other += 1
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here
