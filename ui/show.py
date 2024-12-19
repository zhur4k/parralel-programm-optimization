import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from time import time
from model.logic import Logic
import tkinter as tk
from tkinter import messagebox

logic = Logic()

class Tkinter():
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.logic = Logic()

    def init_ui(self):
        self.root = tk.Tk()
        self.root.title("Random Adjacency Matrix Generator")

        self.label = tk.Label(self.root, text="Enter matrix size:")
        self.label.pack()

        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Generate", command=self.on_generate)
        self.button.pack()

        self.button = tk.Button(self.root, text="Run", command=graph_show)
        self.button.pack()

        self.matrix_display = tk.Text(self.root, height=20, width=50, state="disabled")
        self.matrix_display.pack()
        self.root.mainloop()

    def on_generate(self):
        global array
        try:
            size = int(self.entry.get())
            if not (1 <= size <= 12):
                raise ValueError("Size must be an integer between 1 and 12.")
            array = logic.generate_random_matrix(size)
            self.display_matrix(array)
        except ValueError as e:
            messagebox.showerror("Error", str(e))


    def display_matrix(self, matrix):
        self.matrix_display.config(state="normal")
        self.matrix_display.delete('1.0', tk.END)
        for row in matrix:
            self.matrix_display.insert(tk.END, ' '.join(map(str, row)) + '\n')
        self.matrix_display.config(state="disabled")

def graph_show():
    # Пример использования с графическим представлением
    graph = np.array(array)

    G = nx.from_numpy_array(np.array(graph))
    pos = nx.spring_layout(G)
    plt.subplots(num=f"Задача коммивояжёра. Метод ветвей и границ.")
    nx.draw(G, pos, with_labels=True, alpha=0.5, font_size=16, )
    # Выводим значения весов ребер
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, )

    ts = time()
    tour, cost = logic.tsp_branch_and_bound(graph)

    # Выводим информацию о количестве точек и длине пути
    info_text = f"Path{tour}\nBest path({cost})\nNodes({len(tour)})\nTime: {round(time() - ts, 7)}"
    plt.text(0.05, 0.98, info_text, transform=plt.gca().transAxes, va='top', ha='left',
             bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))

    path_edges = list(zip(tour, tour[1:] + [tour[0]]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='b', width=2, arrows=True,
                           arrowstyle='->, head_width=0.5, head_length=0.8')  # Выделение оптимального маршрута красным цветом

    print("Best tour:", tour)
    print("Cost:", cost)

    plt.show()