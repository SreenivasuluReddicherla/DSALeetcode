class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()==0){
            return true;
        }
        if(s.length()==0){
            return false;
        }
        int tr = 0;
        for(int i=0;i<t.length();i++){
            if(s.charAt(tr)==t.charAt(i)){
                tr++;
                if(tr==s.length()){
                    return true;
                }
            }
            
        }
        return false;
    }
}