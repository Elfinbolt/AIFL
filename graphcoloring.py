def add_edge(graph, u, v):
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)


def can_color(graph, colors, node, color):
    return all(colors.get(n) != color for n in graph.get(node, []))


def try_coloring(graph, nodes, colors, idx, max_colors):
    if idx == len(nodes):
        return True

    node = nodes[idx]
    for c in range(1, max_colors + 1):
        if can_color(graph, colors, node, c):
            colors[node] = c
            if try_coloring(graph, nodes, colors, idx + 1, max_colors):
                return True
            del colors[node]

    return False


def solve(graph, max_colors):
    colors = {}
    if try_coloring(graph, list(graph.keys()), colors, 0, max_colors):
        return colors
    return None


def find_min_colors(graph):
    for k in range(1, len(graph) + 1):
        result = solve(graph, k)
        if result:
            return k, result
    return None, None


def main():
    graph = {}

    n = int(input("Enter number of edges: "))
    for _ in range(n):
        raw = input("Enter edge in the format (u, v): ")
        u, v = raw.strip("()").split(",")
        add_edge(graph, u.strip(), v.strip())

    num_colors, coloring = find_min_colors(graph)

    if coloring:
        print(f"\nMinimum colors required: {num_colors}")
        print("\nColor assignments:")
        for node, color in sorted(coloring.items()):
            print(f"  {node} --> Color {color}")


main()