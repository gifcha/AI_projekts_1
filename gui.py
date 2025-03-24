import tkinter as tk
from tkinter import ttk
from tkinter.constants import *


class GUI:
    def start_game():
        print("First Move:", player_var.get(), "\nAlgorithm:", algorithm_var.get())

    # Create the main window
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("640x400")

    # Title label
    label_title = tk.Label(root, text="Uzsāk spēli", font=("Arial", 14))
    label_title.pack(ipady=20)
    
    # Player selection
    frame_player = tk.Frame(root)
    frame_player.pack()

    player_var = tk.StringVar(value="computer")
    ttk.Radiobutton(frame_player, text="Dators", variable=player_var, value="computer").grid(row=0, column=1)
    ttk.Radiobutton(frame_player, text="Cilvēks", variable=player_var, value="human").grid(row=0, column=2)

    # Algorithm selection
    label_algorithm = tk.Label(root, text="Algoritms", font=("Arial", 14))
    label_algorithm.pack(ipady=20)

    frame_algorithm = tk.Frame(root)
    frame_algorithm.pack()

    algorithm_var = tk.StringVar(value="alpha-beta")
    ttk.Radiobutton(frame_algorithm, text="Alfa-beta", variable=algorithm_var, value="alpha-beta").grid(row=0, column=1)
    ttk.Radiobutton(frame_algorithm, text="Minimaksa", variable=algorithm_var, value="minimax").grid(row=0, column=2)

    # Start button
    button_start = tk.Button(root, text="Sākt spēli", font=("Arial", 14), command=start_game)
    button_start.pack(pady=15, side=BOTTOM)

    # Run the Tkinter event loop
    root.mainloop()