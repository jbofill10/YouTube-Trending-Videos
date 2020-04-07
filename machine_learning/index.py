from machine_learning import LinearRegression as l_r
from machine_learning import Preprocessing as preprocessing

def run(df):
    #df = preprocessing.preprocess(df)
    l_r.run(df)
