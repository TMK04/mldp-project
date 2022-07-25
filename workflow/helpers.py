from IPython.display import display
import pandas as pd

def displayAsDF(ndarray, **kwargs):
  display(pd.DataFrame(ndarray, **kwargs))

# Prevent default print
pdp = display

vcs = lambda ndarray, ascending=True: ndarray.value_counts().sort_index(ascending=ascending)

displayVcs = lambda ndarray: displayAsDF(vcs(ndarray))
displayCols = lambda df: displayAsDF(df.columns, columns=["col"])