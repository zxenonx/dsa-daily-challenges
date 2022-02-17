"""
Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

Expected Outcome:

Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_size = len(sample_list) // 3
start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start, end)
    print(f"chunk {i+1} reversed {list(reversed(sample_list[indexes]))}")
    start = end
    end += chunk_size
