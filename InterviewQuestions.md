1.1 Determine if string has unique characters.

Use hash map w/ key as character and value as character count. Anything with value > 1 doesnt have unique chars.

Time complexity O(n)
Space complexity O(n)

Can be done with standard arrays cause char => int

1.2 2 strings, method that checks to see if permutation

Hash both strings, check if both have same # of characters.

Time complexity O(ab)=O(n)

1.4 Palindrome Permutation

3 cases -> a : single letter
        -> aa/abab/abba : only even count
        -> aba : all even and one odd

string must only have one odd char count!!!!

odd = false
iterating through hashmap():
      if(char.value % 2):
        odd = true
      else
          return false

2.1 Remove duplicates in an unsorted list
  Put all elements in a Set(), duplicates immediately get take care of. {}

2.6 Check to see if a linked list is a Palindrome.
  1. Reverse the original list
  2. Iterate through, one by one, if there's a difference return false.
