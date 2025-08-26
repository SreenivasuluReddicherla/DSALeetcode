class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        int i = 0, n = words.length;

        while (i < n) {
            int j = i, lineLen = 0;

            // pack as many words as possible
            while (j < n && lineLen + words[j].length() + (j - i) <= maxWidth) {
                lineLen += words[j].length();
                j++;
            }

            int spaces = maxWidth - lineLen;
            int gaps = j - i - 1;

            StringBuilder sb = new StringBuilder();

            // case 1: last line OR single word
            if (j == n || gaps == 0) {
                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) sb.append(" ");
                }
                while (sb.length() < maxWidth) sb.append(" ");
            } else {
                int spaceEach = spaces / gaps;
                int extra = spaces % gaps;

                for (int k = i; k < j; k++) {
                    sb.append(words[k]);
                    if (k < j - 1) {
                        for (int s = 0; s < spaceEach; s++) sb.append(" ");
                        if (extra-- > 0) sb.append(" ");
                    }
                }
            }

            res.add(sb.toString());
            i = j;
        }
        return res;
    }
}