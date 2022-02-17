"""
Write a program to remove the item present at index 4 and 
add it to the 2nd position and at the end of the list.

Given:

list1 = [34, 54, 67, 89, 11, 43, 94]

Expected Output:

List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""

list1 = [34, 54, 67, 89, 11, 43, 94]
element = list1[4]
list1.pop(4)
list1.insert(2, element)
list1.append(element)

print(list1)
