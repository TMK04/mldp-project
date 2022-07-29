from IPython.display import display
from numpy import e as E, power
from pandas import DataFrame

def displayAsDF(ndarray, **kwargs):
  display(DataFrame(ndarray, **kwargs))

# Prevent default print
pdp = display

vcs = lambda ndarray, ascending=True: ndarray.value_counts().sort_index(ascending=ascending)

displayVcs = lambda ndarray: displayAsDF(vcs(ndarray))
displayCols = lambda df: displayAsDF(df.columns, columns=["col"])

# Will be needed to "un-log" logged predictions for presenting scores
e = lambda y: power(E, y)