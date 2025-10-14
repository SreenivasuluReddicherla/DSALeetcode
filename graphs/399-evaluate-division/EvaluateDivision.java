class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = buildGraph(equations, values);
        double[] result = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            String start = queries.get(i).get(0);
            String end = queries.get(i).get(1);
            if (!graph.containsKey(start) || !graph.containsKey(end)) {
                result[i] = -1.0;
            } else if (start.equals(end)) {
                result[i] = 1.0;
            } else {
                result[i] = dfs(graph, start, end, new HashSet<>(), 1.0);
            }
        }

        return result;
    }

    private double dfs(Map<String, Map<String, Double>> graph, String curr, String target, Set<String> visited, double product) {
        visited.add(curr);
        Map<String, Double> neighbors = graph.get(curr);

        if (neighbors.containsKey(target)) {
            return product * neighbors.get(target);
        }

        for (String next : neighbors.keySet()) {
            if (!visited.contains(next)) {
                double res = dfs(graph, next, target, visited, product * neighbors.get(next));
                if (res != -1.0) {
                    return res;
                }
            }
        }

        return -1.0;
    }

    private Map<String, Map<String, Double>> buildGraph(List<List<String>> equations, double[] values) {
        Map<String, Map<String, Double>> graph = new HashMap<>();

        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);
            double val = values[i];

            graph.putIfAbsent(a, new HashMap<>());
            graph.putIfAbsent(b, new HashMap<>());

            graph.get(a).put(b, val);
            graph.get(b).put(a, 1 / val);
        }

        return graph;
    }
}