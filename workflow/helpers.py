from IPython.display import display
from numpy import e as E, power
from pandas import DataFrame
import matplotlib.pyplot as plt

y_col = "salary_in_usd"

def displayAsDF(ndarray, **kwargs):
  display(DataFrame(ndarray, **kwargs))

# Prevent default print
pdp = display

vcs = lambda ndarray, ascending=True: ndarray.value_counts().sort_index(ascending=ascending)

displayVcs = lambda ndarray: displayAsDF(vcs(ndarray))
displayCols = lambda df: displayAsDF(df.columns, columns=["col"])

whiteFig = lambda **kwargs: plt.figure(facecolor="white", **kwargs)

def pie(pieable, x=None):
  if x is None:
    x = pieable
  return pieable.pie(x=x, labels=x.index, autopct="%1.1f%%")

# Adapted from https://stackoverflow.com/a/41385215
def pie_maker(total, cols=None):
  if cols is None:
    cols = total
  rows = (total // cols) + (total % cols)
  fig = whiteFig(figsize=(5*cols, 4*rows))
  i = 1
  def subPie(col):
    nonlocal i
    ax = fig.add_subplot(rows, cols, i)
    x = vcs(col, False)
    pie(ax, x)
    plt.title(col.name)
    i += 1
  return subPie

# Will be needed to "un-log" logged predictions for presenting scores
e = lambda y: power(E, y)