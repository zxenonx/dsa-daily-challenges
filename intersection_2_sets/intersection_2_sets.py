"""
Find the intersection (common) of two sets and remove those elements from the first set

See: Python Set

Given:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

Expected Output:

Intersection is  {57, 83, 29}
First Set after removing common element  {65, 42, 78, 23}
"""
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print(f"Intersection is {first_set.intersection(second_set)}")
print(f"First set after removing common elements {first_set.difference(first_set.intersection(second_set))}")
