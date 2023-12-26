from itertools import permutations

locations = {
    1: (23.8728568, 90.3984184, "Uttara Branch"),
    2: (23.8513998, 90.3944536, "City Bank Airport"),
    3: (23.8330429, 90.4092871, "City Bank Nikunja"),
    4: (23.8679743, 90.3840879, "City Bank Beside Uttara Diagnostic"),
    5: (23.8248293, 90.3551134, "City Bank Mirpur 12"),
    6: (23.827149, 90.4106238, "City Bank Le Meridien"),
    7: (23.8629078, 90.3816318, "City Bank Shaheed Sarani"),
    8: (23.8673789, 90.429412, "City Bank Narayanganj"),
    9: (23.8248938, 90.3549467, "City Bank Pallabi"),
    10: (23.813316, 90.4147498, "City Bank JFP"),
}


def calculate_distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5


def total_distance(route):
    return sum(calculate_distance(locations[route[i]], locations[route[i + 1]]) for i in range(len(route) - 1))


def find_optimal_route():
    all_routes = permutations(locations.keys())
    best_route = min(all_routes, key=total_distance)
    return best_route


if __name__ == "__main__":
    optimal_route = find_optimal_route()

    print("Optimal Route:")
    for location_id in optimal_route:
        print(f"{locations[location_id][2]} - Lat: {locations[location_id][0]}, Lon: {locations[location_id][1]}")

    with open("optimal_route.txt", "w") as file:
        for location_id in optimal_route:
            file.write(
                f"{locations[location_id][2]} - Lat: {locations[location_id][0]}, Lon: {locations[location_id][1]}\n")
