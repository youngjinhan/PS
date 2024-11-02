class Solution {
    public boolean isCircularSentence(String sentence) {
        /** 
        Solution - Space-optimized Approach
        Time Complexity: O(n)
        Space Complexity: O(1)
        */
        int n = sentence.length();
        for (int i=0; i<n; i++) {
            if (sentence.charAt(i) == ' ' && sentence.charAt(i-1) != sentence.charAt(i+1)) return false;
        }
        return sentence.charAt(0) == sentence.charAt(n-1);


        /**
        My First Solution
        Time Complexity: O(n)
        Space Complexity: O(n)

        String[] words = sentence.split(" ");
        int n = words.length;
        for (int i = 0; i < n; i++) {
            if (words[i].charAt(words[i].length() - 1) != words[(i + 1) % n].charAt(0)) 
                return false;
        }
        return true;
        
        */
    }
}