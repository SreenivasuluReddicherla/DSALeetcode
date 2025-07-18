class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicates = 1
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicates += 1
                else:
                    dx = x2 - x1
                    dy = y2 - y1
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    # Always keep slope direction consistent
                    # We make sure the direction is unique by forcing dx to be positive
                    if dx < 0:
                        dx *= -1
                        dy *= -1

                    # Handle zero dx (vertical line)
                    if dx == 0:
                        dy = 1

                    # Handle zero dy (horizontal line)
                    if dy == 0:
                        dx = 1

                    slopes[(dy, dx)] += 1

            max_points = max(max_points, duplicates + max(slopes.values(), default=0))

        return max_points