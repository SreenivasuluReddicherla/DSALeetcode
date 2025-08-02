class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split(" ");
        if(pattern.length()!=words.length){
            return false;
        }
        HashMap<Character, String> ptos = new HashMap<>();
        HashMap<String, Character> stop = new HashMap<>();
        for(int i=0;i<words.length;i++){
            char c = pattern.charAt(i);
            String word = words[i];
            if(ptos.containsKey(c)){
                if(!ptos.get(c).equals(word)){
                    return false;
                }
            }else{
                ptos.put(c, word);
            }
            if(stop.containsKey(word)){
                if(stop.get(word)!=c){
                    return false;
                }
            }else{
                stop.put(word, c);
            }
        } 
        return true;
    }
}