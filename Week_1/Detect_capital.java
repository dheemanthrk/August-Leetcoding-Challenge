class Solution {
    public boolean detectCapitalUse(String word) {
        return word.toLowerCase().equals(word) ||
            word.toUpperCase().equals(word) ||
            word.charAt(0) >= 'A' && word.charAt(0) <= 'Z' && word.substring(1).toLowerCase().equals(word.substring(1));
    }
}