class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap <Character, Integer> count = new HashMap<>();
        for(char ch:s.toCharArray()){
            count.put(ch, count.getOrDefault(ch, 0)+1);
        }
        for(char c:t.toCharArray()){
            if(!count.containsKey(c)){
                return false;
            }
            count.put(c, count.get(c)-1);
            if(count.get(c)<0){
                return false;
            }
        }
        return true;
    }
}