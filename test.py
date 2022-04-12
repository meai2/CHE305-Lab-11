import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from IPython.display import display

data = load_iris()
df = pd.DataFrame(data.data, columns = data.feature_names)

display(df.to_string())
