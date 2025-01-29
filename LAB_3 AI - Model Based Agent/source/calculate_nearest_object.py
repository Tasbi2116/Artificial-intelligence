# calculate_nearest_object.py

def find_nearest_object(room, x, y):
    min_distance = float('inf')
    target = None
    for i in range(len(room)):
        for j in range(len(room[i])):
            if room[i][j] == "object":
                distance = abs(i - x) + abs(j - y)  # Manhattan distance
                if distance < min_distance:
                    min_distance = distance
                    target = (i, j)
    return target