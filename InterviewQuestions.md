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
