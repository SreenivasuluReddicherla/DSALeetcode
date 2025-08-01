class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        HashMap<Character, Character> stot = new HashMap<>();
        HashMap<Character, Character> ttos = new HashMap<>();
        for(int i=0;i<s.length();i++){
            char sc = s.charAt(i);
            char tc = t.charAt(i);
            if(stot.containsKey(sc)){
                if(stot.get(sc)!=tc){
                    return false;
                }
            }else{
                stot.put(sc,tc);
            }
            if(ttos.containsKey(tc)){
                if(ttos.get(tc)!=sc){
                    return false;
                }
            }else{
                ttos.put(tc,sc);
            }
        }
        return true;
    }
}