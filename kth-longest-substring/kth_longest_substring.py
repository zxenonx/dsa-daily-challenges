"""
Find kth longest substring with the same characters in the string “aaaaaabbbbccc”; 
For k = 2 answer is “bbbb”

-- https://candor.co/interviews/find-kth-longest-substring-with-the-same-characters-in-the-string-aaaaaabbbbccc
"""

long_string = "aaaaaabbbbccc"
arrange_values = []
try:
    kth = int(input("Kth: "))
except ValueError:
    print("Enter an integer...")
    kth = int(input("Kth: "))
else:
    unique_values = set(long_string)
    subs = ""
    for value in unique_values:
        for letter in long_string:
            if letter == value:
                subs += letter
        arrange_values.append(subs)    
        subs = ""
        
    # order by length DESC
    print(sorted(arrange_values, key=len, reverse=True)[kth-1])
