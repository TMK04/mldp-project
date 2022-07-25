from IPython.display import display
import matplotlib.pyplot as plt
import pandas as pd

def displayAsDF(ndarray, **kwargs):
  display(pd.DataFrame(ndarray, **kwargs))

# Prevent default print
pdp = display

vcs = lambda ndarray, ascending=True: ndarray.value_counts().sort_index(ascending=ascending)

displayVcs = lambda ndarray: displayAsDF(vcs(ndarray))
displayCols = lambda df: displayAsDF(df.columns, columns=["col"])

def mms(ndarray):
  min = ndarray.min()
  return (ndarray - min)/(ndarray.max() - min)

def pie_kwargs(col):
  x = vcs(col, False)
  return { "x": x, "labels": x.index, "autopct": "%1.1f%%" }

def white_fig(**kwargs):
  return plt.figure(facecolor="white", **kwargs)

# Adapted from https://stackoverflow.com/a/41385215
def pie_maker(total, cols):
  rows = (total // cols) + (total % cols)
  fig = white_fig(figsize=(5*cols, 4*rows))
  i = 1
  def pie(col):
    nonlocal i
    ax = fig.add_subplot(rows, cols, i)
    ax.pie(**pie_kwargs(col))
    plt.title(col.name)
    i += 1
  return pie