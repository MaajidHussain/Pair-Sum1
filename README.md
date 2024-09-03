# Pair-Sum1
# Summary: 
The function finds the indices of the two numbers that add up to the target using a hash map (seen dictionary) for efficient lookups. When it encounters a number, it calculates the complement needed to reach the target and checks if this complement has been seen before. If it has, it returns the indices of the complement and the current number. If not, it adds the current number to the dictionary for future lookups. This approach ensures that the function operates efficiently in linear time.


Detailed Explanation

seen = {}: We start with an empty dictionary named seen. This dictionary will map each number to its index in the list. The purpose is to quickly check if we have already encountered a number that complements the current number to reach the target.
Iteration Through the List:

The function iterates over each number in nums using a for loop with enumerate, which provides both the index and the value of each element.


Detailed Walkthrough:
1.Initialization:

seen = {}: Start with an empty dictionary to keep track of numbers and their indices.

2.Iteration Through the List:
  a)First Iteration:
  Index: 0
  Number: 2
  Complement: 9 - 2 = 7
  Check seen:
  7 is not in seen (since seen is empty at this point).
  Update seen:
  Add 2 to seen with its index: seen = {2: 0}

  b)Second Iteration:
  Index: 1
  Number: 11
  Complement: 9 - 11 = -2
  Check seen:
  -2 is not in seen.
  Update seen:
  Add 11 to seen with its index: seen = {2: 0, 11: 1}

  c)Third Iteration:
  Index: 2
  Number: 7
  Complement: 9 - 7 = 2
  Check seen:
  2 is in seen with index 0.
  Return Result:
  Since the complement 2 was found in seen at index 0, the function returns [0, 2].

  d)Summary
  Result: The function finds that the numbers at indices 0 (which is 2) and 2 (which is 7) sum up to the target value 9.


Why This Approach Works
  Efficiency: By using a dictionary (seen), the function can quickly check if a complement exists (constant time lookups). This makes the algorithm run in linear time 𝑂(𝑛)
  where 𝑛 is the number of elements in the list.
  
  Tracking: The dictionary efficiently keeps track of the indices of numbers that have been processed, enabling quick identification of pairs that sum up to the target.
  This approach ensures that each element is processed only once and complements are found in constant time, making the solution both fast and straightforward.
