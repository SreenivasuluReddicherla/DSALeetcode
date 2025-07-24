class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<String> seen = new HashSet<>();
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                int val = board[i][j];
                if(val != '.'){
                    if(!seen.add(val+"in row"+i)||
                        !seen.add(val+"in col"+j)||
                        !seen.add(val+"in block"+i/3+"-"+j/3)){
                            return false;
                        }
                }
            }
        }
        return true;
    }
}