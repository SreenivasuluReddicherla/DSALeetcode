class Solution {
    public int maxPoints(int[][] points) {
        if(points.length<=2){
            return points.length;
        }
        int result = 0;
        for(int i=0;i<points.length;i++){
            Map<String, Integer> slopeMap = new HashMap<>();
            int duplicate = 1;
            for(int j=i+1;j<points.length;j++){
                int dx = points[j][0]-points[i][0];
                int dy = points[j][1]-points[i][1];

                if(dx == 0 && dy == 0){
                    duplicate++;
                    continue;
                }
                int g = gcd(dx,dy);
                dx/=g;
                dy/=g;
                String slope = dy+"/"+dx;
                slopeMap.put(slope, slopeMap.getOrDefault(slope, 0)+1);
            }
            int localMax = 0;
            for(int count:slopeMap.values()){
                localMax = Math.max(localMax, count);
            }
            result = Math.max(result, localMax + duplicate);
        }
        return result;
    }
    private int gcd(int a, int b){
        return b==0? a:gcd(b, a%b);
    }
}