#linearsearch 

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

data = [34, 78, 12, 9, 89, 50, 41]
search_item_1 = 89
result_1 = linear_search(data, search_item_1)
print("Example 1 - Target 89 found at index:", result_1)
search_item_2 = 34
result_2 = linear_search(data, search_item_2)
print("Example 2 - Target 34 found at index:", result_2)
search_item_3 = 100
result_3 = linear_search(data, search_item_3)
print("Example 3 - Target 100 found at index:", result_3)