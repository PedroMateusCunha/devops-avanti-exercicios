"""The binary_search function performs a binary search on an array arr between the
positions left_index and right_index, looking for the element search_element. If 
the element is found, the function returns the index of the first occurrenceof the
element. Otherwise, the function returns -1
"""
# It returns location of search_element in given array arr
# if present, else returns -1
def binary_search(arr: list, left_index: int, right_index: int, search_element: int):
    """The binary_search function performs a binary search on an array arr between the
    positions left_index and right_index, looking for the element search_element. If 
    the element is found, the function returns the index of the first occurrenceof the
    element. Otherwise, the function returns -1.

    Args:
        arr (list): The array to search in.
        left_index (int): The left bound of the array (inclusive).
        right_index (int): The right bound of the array (inclusive).
        search_element (int): The element to search for.

    Returns:
        _type_: _description_
    """
    # Base case: if left index is greater than right index, element is not present
    if left_index > right_index:
        return -1

    # Calculate the mid index
    mid = (left_index + right_index) // 2

    # If element is present at the middle itself
    if arr[mid] == search_element:
        return mid

    # If element is smaller than mid, then it can only be present in left subarray
    if arr[mid] > search_element:
        return binary_search(arr, left_index, mid - 1, search_element)

    # Else the element can only be present in right subarray
    return binary_search(arr, mid + 1, right_index, search_element)


# Main Function
if __name__ == "__main__":
    # User input array
    array = [int(search_element) for search_element in input("Enter the array with elements separated by commas: ").split(",")]

    # User input element to search for
    x = int(input("Enter the element you want to search for: "))

    # Function call
    result = binary_search(array, 0, len(array) - 1, x)

    # printing the output
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in array")
        