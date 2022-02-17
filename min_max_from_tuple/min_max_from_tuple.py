"""
Remove duplicates from a list and create a tuple and find the minimum and maximum number

Given:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

Expected Outcome:

unique items [87, 45, 41, 65, 99]
tuple (87, 45, 41, 65, 99)
min: 41
max: 99
"""
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

print(list(set(sample_list)))
print(tuple(set(sample_list)))
print(max(set(sample_list)))
print(min(set(sample_list)))
