class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), 1, n, k);
        return res;
    }
    private void backtrack(List<List<Integer>> res, List<Integer> path, int start, int n, int k) {
        if (path.size() == k) {
            res.add(new ArrayList<>(path));
            return;
        }

        for (int i = start; i <= n - (k - path.size()) + 1; i++) { // pruning
            path.add(i);
            backtrack(res, path, i + 1, n, k);
            path.remove(path.size() - 1);
        }
    }
}