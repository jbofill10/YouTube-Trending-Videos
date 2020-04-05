from EDA import Trends as correlations, Likes as likes, Views as views, Comments as comments

def init_eda(df, categories):

    #correlations.eda(df)
    #likes.likes_eda(df, categories)
    #views.eda(df, categories)

    comments.eda(df, categories)
