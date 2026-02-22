def a_star_search(graph, heuristics, start, goal):
    open_list = [[heuristics[start], start, [start], 0]]
    closed_list = []
    print(f"--- A* Search Start ---")
    print(f"Start Location: {start}")
    print(f"Destination: {goal}\n")

    while open_list:
        open_list.sort(key=lambda x: x[0])
        f_val, current_node, path, g_cost = open_list.pop(0)

        if current_node in closed_list:
            continue

        closed_list.append(current_node)

        if current_node == goal:
            return path, g_cost, closed_list, [[item[1], item[0]] for item in open_list]

        if current_node in graph:
            for neighbor, weight in graph[current_node]:
                if neighbor not in closed_list:
                    new_g_cost = g_cost + weight
                    new_f_val = new_g_cost + heuristics[neighbor]
                    new_path = path + [neighbor]
                    open_list.append([new_f_val, neighbor, new_path, new_g_cost])

    return None


graph = {
    'Sanvordem': [('Xelvona', 4), ('Panchvadi', 6), ('Curchorem', 3), ('Rumbrem', 7)],
    'Xelvona': [('Sanvordem', 4)],
    'Panchvadi': [('Sanvordem', 6), ('Macasana', 4)],
    'Macasana': [('Panchvadi', 4)],
    'Curchorem': [('Sanvordem', 3), ('Kakoda', 4)],
    'Kakoda': [('Curchorem', 4), ('Hodar', 6)],
    'Hodar': [('Kakoda', 6), ('Vodlemol Cacora', 5)],
    'Vodlemol Cacora': [('Hodar', 5)],
    'Rumbrem': [('Sanvordem', 7)]
}

heuristics = {
    'Sanvordem': 18,
    'Rumbrem': 16,
    'Panchvadi': 14,
    'Macasana': 12,
    'Xelvona': 13,
    'Curchorem': 8,
    'Kakoda': 6,
    'Hodar': 3,
    'Vodlemol Cacora': 0
}

print("Available Locations:")
for place in graph.keys():
    print("-", place)

start_node = input("\nEnter START location: ").strip()
goal_node = input("Enter DESTINATION location: ").strip()

if start_node not in graph or goal_node not in graph:
    print("\nInvalid start or destination.")
else:
    result = a_star_search(graph, heuristics, start_node, goal_node)

    if result:
        path, total_cost, closed, remaining = result
        print("Path Sequence:")
        print(" -> ".join(path))
        print("\nNode f(n) Calculation (g + h):")
        accumulated_g = 0
        for i in range(len(path)):
            node = path[i]
            if i > 0:
                for neighbor, weight in graph[path[i-1]]:
                    if neighbor == node:
                        accumulated_g += weight
            print(f"{node}: f(n) = {accumulated_g} (g) + {heuristics[node]} (h) = {accumulated_g + heuristics[node]}")
        print(f"\nTotal Actual Path Cost: {total_cost} km")
        print(f"Closed List: {closed}")
        print(f"Open List (Remaining with f-values): {remaining}")
