# gui_setup.py
import tkinter as tk

def setup_gui(root, room_size):
    gui_labels = [[tk.Label(root, text=" ", width=8, height=3, relief="solid") for _ in range(room_size)] for _ in range(room_size)]
    for i in range(room_size):
        for j in range(room_size):
            gui_labels[i][j].grid(row=i, column=j)
    return gui_labels

def update_gui(root, room, x, y, path, gui_labels, stats_label, total_object_collected, total_move, total_action):
    for i, row in enumerate(room):
        for j, cell in enumerate(row):
            if i == x and j == y:
                gui_labels[i][j].config(text="Robot", bg="yellow")  # Robot position
            elif (i, j) in path:
                gui_labels[i][j].config(text=".", bg="lightgreen")  # Mark path
            elif cell == "object":
                gui_labels[i][j].config(text="Object", bg="blue")  # Object
            elif cell == "hurdle":
                gui_labels[i][j].config(text="Hurdle", bg="red")  # Hurdle
            else:
                gui_labels[i][j].config(text="0", bg="white")  # Path

    # Update stats label
    stats_label.config(text=f"Objects Collected: {total_object_collected}, Total Moves: {total_move}, Total Actions: {total_action}")
    root.update()  # Update the GUI