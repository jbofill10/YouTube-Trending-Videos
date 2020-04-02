import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd


def eda(df):
    
    style.use('seaborn-poster')
    numerical_df = df[['likes', 'views', 'dislikes', 'comments_disabled', 'comment_count', 'ratings_disabled']].apply(pd.to_numeric)

    sns.heatmap(numerical_df.corr(method='pearson'), cmap=sns.light_palette('purple'), annot=True, annot_kws={'size':16})
    plt.xticks(rotation=45)
    #plt.savefig('Charts/corr_matrix.png', bbox_inches='tight')
    plt.show()