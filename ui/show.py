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
    """
    Генерация матрицы конфликтов и оптимизация параллельной программы.

    :return: Минимальное количество ресурсов и раскраска
    """
    # Пример использования с графическим представлением
    graph = np.array(array)  # Здесь используйте вашу матрицу конфликтов

    G = nx.from_numpy_array(graph)
    pos = nx.spring_layout(G)

    # Подготовка графического окна
    plt.figure(num="Оптимизация параллельной программы. Рекурсивный алгоритм оптимальной раскраски.")
    nx.draw(G, pos, with_labels=True, alpha=0.5, font_size=16)

    # Выводим значения весов ребер
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    ts = time()
    cost, node_colors = logic.graph_coloring_optimization(graph)

    # Выводим раскраску узлов (задач)
    print(node_colors)
    print(cost)

    # Выводим информацию о количестве точек и длине пути
    info_text = f"Минимальное количество ресурсов (процессоров/регистров): {cost}\n" \
                f"Раскраска узлов (задач): {node_colors}\n" \
                f"Время: {round(time() - ts, 7)}"
    plt.text(0.05, 0.98, info_text, transform=plt.gca().transAxes, va='top', ha='left',
             bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))

    # Определим цвета для каждого ресурса (процессора/регистра)
    # Цвета для каждого узла в графе
    node_color_map = [node_colors[node] for node in G.nodes]

    # Рисуем узлы с раскраской
    nx.draw_networkx_nodes(G, pos, node_color=node_color_map, cmap=plt.cm.rainbow, node_size=500)

    # Рисуем рёбра
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)

    plt.show()