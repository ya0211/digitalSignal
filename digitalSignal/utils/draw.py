import numpy as np
import matplotlib.pyplot as plt
from digitalSignal import SignalArray


def draw(a: list, text: list, xlabel=None, ylabel=None, xlim=None, ylim=None,
         fig_size=(12, 9), style="plot", grid=None, file_name="figure.pdf"):

    plt.figure(figsize=fig_size)
    plt.subplots_adjust(hspace=0.5)

    def draw_fun(data: SignalArray, draw_style):
        if draw_style == "stem":
            plt.stem(data.index, data.element, markerfmt='C0.')
            bottom, top = plt.ylim()
            if min(data.element) >= 0:
                plt.ylim(0, top)
            else:
                pass
        elif draw_style == "plot":
            plt.plot(data.index, data.element)

    for i in range(0, len(a)):
        if len(a) <= 3:
            plt.subplot(3, 1, i+1)
        elif len(a) <= 8:
            plt.subplot(int(np.ceil(len(a)/2)), 2, i+1)
        plt.title(text[i])
        if grid is not None:
            plt.grid(linestyle=grid, linewidth=1)
        if xlabel is not None:
            plt.xlabel(xlabel[i])
        if xlim is not None:
            plt.xlim(*xlim)
        if ylim is not None:
            plt.ylim(*ylim)
        if ylabel is not None:
            plt.ylabel(ylabel[i])

        if isinstance(style, list):
            draw_fun(a[i], style[i])
        elif isinstance(style, str):
            draw_fun(a[i], style)

    plt.savefig(file_name)
    plt.close()
