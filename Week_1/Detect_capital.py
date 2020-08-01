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

