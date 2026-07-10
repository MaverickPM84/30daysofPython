# Exercise 13 - Ranges of Strings

# Question: Complete the script, so it generates the expected output using my_range  as input data. Please note that the items of the expected list output are all strings.

# my_range = range(1, 21)
#  Expected output: 

# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']  

my_range = range(1, 21)

print(list(map(str, my_range)))    

"""
The line works inside-out — Python evaluates the innermost function first and works outward:

python
print(list(map(str, my_range)))
#  4     3    2   1
Step-by-step breakdown
① my_range

python
my_range = range(1, 21)
# → range object: 1, 2, 3, ... 20  (integers)
② map(str, my_range)

python
map(str, my_range)
# → applies str() to every integer in my_range, one by one
# → lazy map object: "1", "2", "3", ... "20"  (strings, not yet a list)
map(function, iterable) takes two arguments — a function and something to iterate over — and applies the function to each item. Nothing is computed yet; it's lazy.

③ list(...)

python
list(map(str, my_range))
# → forces the lazy map object to evaluate and collects results into a real list
# → ['1', '2', '3', ... '20']
④ print(...)

python
print(['1', '2', '3', ... '20'])
# → displays the list to the console
Why map + list instead of a loop?
Your solution here is the idiomatic one-liner equivalent of this:

python
# Equivalent using a list comprehension (also very Pythonic)
print([str(x) for x in my_range])
# Equivalent using an explicit loop
result = []
for x in my_range:
    result.append(str(x))
print(result)
All three produce identical output. map() is slightly more memory-efficient for large datasets since it's lazy, but list(map(...)) and [... for ...] are both common in real Python code.

"""