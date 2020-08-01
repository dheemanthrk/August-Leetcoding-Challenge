# O(n) solution 1:

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lc = word.lower()
        uc = word.upper()
        if word[1:]==lc[1:]:
            return True
        elif word[1:]==uc[1:] and word[0].isupper():
            return True
        else:
            return False

# O(n) solution 2:

class Solution:
    def detectCapitalUse(self, word):
        Num_cap, n = 0, len(word)
        for letter in word: 
            Num_cap += letter.isupper()
        if Num_cap == 0 or Num_cap == n or Num_cap == 1 and word[0].isupper():
            return True
        return False