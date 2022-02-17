"""
Write a program to iterate a given list and count the occurrence of each element 
and create a dictionary to show the count of each element.

Given:

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

Expected Output:

Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""
import timeit

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occurrence_dict = {}
starttime = timeit.default_timer()
print("The start time is :", starttime)

# faster than collections.Counter
for element in sample_list:
    if element in occurrence_dict:
        occurrence_dict[element] += 1
    else:
        occurrence_dict[element] = 1

print("The time difference is :", timeit.default_timer() - starttime)

print(occurrence_dict)
