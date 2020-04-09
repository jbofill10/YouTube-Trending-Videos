import pandas as pd
import numpy as np


def preprocess(df):
    numerical_values = ['likes', 'views', 'dislikes', 'comment_count']
    log_df = pd.DataFrame()

    for label in numerical_values:
        log_df[label] = np.log(df[label].astype(int) + 1)
    for i in df:
        if i not in numerical_values:
            log_df[i] = df[i]

    return log_df