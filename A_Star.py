graph = {
    "Sanvordem": {
        "Xelvona": 4,
        "Panchvadi": 6,
        "Curchorem": 3,    
        "Rumbrem": 7
    },
    "Xelvona": {
        "Sanvordem": 4
    },
    "Panchvadi": {
        "Sanvordem": 6,
        "Macasana": 4
    },
    "Macasana": {
        "Panchvadi": 4
    },
    "Curchorem": {          
        "Sanvordem": 3,
        "Kakoda": 4
    },
    "Kakoda": {
        "Curchorem": 4,
        "Hodar": 6
    },
    "Hodar": {           
        "Kakoda": 6,
        "Vodlemol Cacora": 5
    },
    "Vodlemol Cacora": {
        "Hodar": 5
    },
    "Rumbrem": {
        "Sanvordem": 7
    }
}

# Heuristic
heuristic = {
    "Sanvordem": 0,
    "Xelvona": 4,
    "Panchvadi": 6,
    "Macasana": 9,
    "Curchorem": 3,      
    "Kakoda": 6,
    "Hodar": 9,          
    "Vodlemol Cacora": 13,
    "Rumbrem": 7
}

def a_star(start, goal):
    open_list = []
    closed_list = set()

    # (f(n), current_node, path, g(n))
    open_list.append((heuristic[start], start, [start], 0))

    while open_list:
        # Sort based on f(n)
        open_list.sort(key=lambda x: x[0])
        f, current, path, g = open_list.pop(0)

        if current == goal:
            return path, g

        closed_list.add(current)

        for neighbor, edge_cost in graph[current].items():
            if neighbor not in closed_list:
                new_g = g + edge_cost
                new_f = new_g + heuristic.get(neighbor, 999)

                open_list.append(
                    (new_f, neighbor, path + [neighbor], new_g)
                )

    return None, None


# User Input

print("Available Locations:")
for place in graph.keys():
    print("-", place)

start_node = input("\nEnter START location: ").strip()
goal_node = input("Enter DESTINATION location: ").strip()

if start_node not in graph or goal_node not in graph:
    print("\nInvalid start or destination.")
else:
    path, total_cost = a_star(start_node, goal_node)

    if path:
        print("\nPath Found:")
        print(" -> ".join(path))
        print(f"\nTotal Path Cost: {total_cost}")
    else:
        print("\nNo path found.")
