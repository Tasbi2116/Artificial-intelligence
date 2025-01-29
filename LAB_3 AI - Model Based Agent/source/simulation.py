# simulation.py
import time
import tkinter as tk
from environment import create_room, start
from perceptions import check_object, perceive_boundaries
from calculate_nearest_object import find_nearest_object
from actuators import collect_object
from target_movement import move_towards_target
from gui_setup import setup_gui, update_gui

# Initialize performance variables
total_move = 0
total_object_collected = 0
total_action = 0

# Set up GUI
root = tk.Tk()
root.title("Robot Room Simulation")

room_size = 8
gui_labels = setup_gui(root, room_size)
stats_label = tk.Label(root, text=" ", font=("Helvetica", 12), pady=10)
stats_label.grid(row=room_size, column=0, columnspan=room_size)

# Main simulation loop
for i in range(5):
    x, y = start()
    move = 0
    objects_collected = 0
    room = create_room()
    path = []

    while True:
        time.sleep(1)
        if check_object(room, x, y):
            collect_object(room, x, y)
            objects_collected += 1
            total_object_collected += 1
            total_action += 1

        path.append((x, y))
        update_gui(root, room, x, y, path, gui_labels, stats_label, total_object_collected, total_move, total_action)

        if perceive_boundaries(x, y, room):
            print("Objects collected in step:", i, "is---", objects_collected)
            print("Robot moves in step:", i, "is---", move, "times")
            break

        target = find_nearest_object(room, x, y)
        if target:
            (new_x, new_y), _, moved = move_towards_target(room, x, y, target)
        else:
            break

        if not moved:
            print("Objects collected in step", i, "is---", objects_collected)
            print("Robot moves in step", i, "is---", move, "times")
            print("Robot is blocked by hurdles")
            break

        move += 1
        total_move += 1
        total_action += 1
        x, y = new_x, new_y

performance = total_action / total_object_collected if total_object_collected > 0 else 0
print("Total objects collected:", total_object_collected)
print("Total moves:", total_move)
print("Total Action:", total_action)
print("Total Object Collected:", total_object_collected)
print("Final Performance:", performance)

root.mainloop()