from main import *
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def create_omx_frame(main_window):
    main_window.title("OMX Stockholm 30 Analytics & Data")
    data = pd.read_csv("omx30.csv")
    frame = tk.Frame(main_window, width=600)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('OMX Stockholm 30 Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    return frame


def create_bitcoin_frame(main_window):
    data = pd.read_csv("bitcoin.csv")
    main_window.title("Bitcoin Analytics & Data")
    frame = tk.Frame(main_window, width=600)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('Bitcoin Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    return frame

def create_gold_frame(main_window):
    data = pd.read_csv("gold.csv")
    main_window.title("Gold Analytics & Data")
    frame = tk.Frame(main_window, width=600)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('Gold Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    return frame

def create_USD_frame(main_window):
    main_window.title("Analytics & Data")
    data = pd.read_csv("usd.csv")
    frame = tk.Frame(main_window, width=600)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('USD Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    return frame

def create_silver_frame(main_window):
    main_window.title("Analytics & Data")
    data = pd.read_csv("silver.csv")
    frame = tk.Frame(main_window, width=600)
    figure = plt.Figure(figsize=(5, 4), dpi=100)
    figure_plot = figure.add_subplot(1, 1, 1)
    figure_plot.set_ylabel('Value')

    dataframe = data.groupby('Date').sum()

    dataframe.plot(kind='line', legend=True, ax=figure_plot,
                color='r', marker='o', fontsize=10)
    figure_plot.set_title('Silver Analytics & Data')

    line_graph = FigureCanvasTkAgg(figure, frame)
    line_graph.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    return frame