from machine_learning.regression import LinearRegression as l_r
from machine_learning.clustering import KMeans as kmeans
from machine_learning import Preprocessing as preprocessing


def run(df, categories):

    #log_df = preprocessing.preprocess(df)
    #l_r.run(log_df)

    kmeans.kmeans(df, categories)
