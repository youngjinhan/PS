class Solution {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] p1 = sentence1.split(" ");
        String[] p2 = sentence2.split(" ");
        if (p1.length < p2.length) {
            String[] tmp = p1;
            p1 = p2;
            p2 = tmp;
        }

        int lCnt = 0, rCnt = 0, n1 = p1.length, n2 = p2.length;
        while (lCnt < n2 && p1[lCnt].equals(p2[lCnt])) lCnt++;
        while (rCnt < n2 && p1[n1 - 1 - rCnt].equals(p2[n2 - 1 - rCnt])) rCnt++;
        return lCnt + rCnt >= n2;
    }
}