import math

class VietorisRipsFiltration:
    """
    Vietoris-Rips Filtration on metric points.
    Builds simplicial complex at varying epsilon radius thresholds.
    """
    def __init__(self, points):
        self.points = points

    def distance(self, p1, p2):
        return math.sqrt(sum((x - y)**2 for x, y in zip(p1, p2)))

    def edges_at_radius(self, epsilon):
        edges = []
        n = len(self.points)
        for i in range(n):
            for j in range(i + 1, n):
                if self.distance(self.points[i], self.points[j]) <= epsilon:
                    edges.append((i, j))
        return edges
