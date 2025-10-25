class Solution {
    private static final Map<Character, String> phoneMap = new HashMap<>() {{
        put('2', "abc");
        put('3', "def");
        put('4', "ghi");
        put('5', "jkl");
        put('6', "mno");
        put('7', "pqrs");
        put('8', "tuv");
        put('9', "wxyz");
    }};
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits == null || digits.isEmpty()) return res;
        backtrack(res, new StringBuilder(), digits, 0);
        return res;
    }
    private void backtrack(List<String> res, StringBuilder path, String digits, int index) {
        if (index == digits.length()) {
            res.add(path.toString());
            return;
        }
        String letters = phoneMap.get(digits.charAt(index));
        for (char c : letters.toCharArray()) {
            path.append(c);
            backtrack(res, path, digits, index + 1);
            path.deleteCharAt(path.length() - 1);
        }
    }
}