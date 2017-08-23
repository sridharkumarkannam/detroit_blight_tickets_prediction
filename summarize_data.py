import pandas as pd

def avg_predict_by_col(y, col):
    return pd.concat([y, col], axis=1).groupby(col.name).agg(['mean', 'std', 'count'])