def best_first_search(graph, heuristics, start, goal):
    open_list = [[heuristics[start], start, [start], 0]]
    closed_list = []
    print(f"--- Best-First Search Start ---")
    print(f"Start Location: {start}")
    print(f"Destination: {goal}\n")

    while open_list:
        open_list.sort(key=lambda x: x[0])
        h_val, current_node, path, current_cost = open_list.pop(0)

        if current_node in closed_list:
            continue

        closed_list.append(current_node)

        if current_node == goal:
            return path, current_cost, closed_list, [item[1] for item in open_list]

        if current_node in graph:
            for neighbor, weight in graph[current_node]:
                if neighbor not in closed_list:
                    new_path = path + [neighbor]
                    new_cost = current_cost + weight
                    open_list.append([heuristics[neighbor], neighbor, new_path, new_cost])

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
    result = best_first_search(graph, heuristics, start_node, goal_node)

    if result:
        path, total_cost, closed, remaining = result
        print("Path Sequence:")
        print(" -> ".join(path))
        print("\nNode Heuristics (h(n) used for selection):")
        for node in path:
            print(f"{node} : {heuristics[node]} km")
        print(f"\nTotal Actual Path Cost: {total_cost} km")
        print(f"Closed List: {closed}")
        print(f"Open List (Remaining): {remaining}")
