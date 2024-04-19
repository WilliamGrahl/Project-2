import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def open_tkinter_window_1():
    data = pd.read_csv("omx30.csv")

    main_window = tk.Tk()
    main_window.title("OMX Stockholm 30 Analytics & Data")

    main_window.geometry("800x600")

    frame = tk.Frame(main_window, width=600)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('OMX Stockholm 30 Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    main_window.mainloop()


def open_tkinter_window_2():
    data = pd.read_csv("bitcoin.csv")

    main_window = tk.Tk()
    main_window.title("Bitcoin Analytics & Data")

    main_window.geometry("800x600")

    frame = tk.Frame(main_window, width=600)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('Bitcoin Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    main_window.mainloop()


def open_tkinter_window_3():
    data = pd.read_csv("gold.csv")

    main_window = tk.Tk()
    main_window.title("Gold Analytics & Data")

    main_window.geometry("800x600")

    frame = tk.Frame(main_window, width=600)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('Gold Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    main_window.mainloop()