import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import pandas as pd


def likes_eda(df, categories):
    numerical_values = ['likes', 'views', 'dislikes', 'comment_count']
    log_df = pd.DataFrame()

    for label in numerical_values:
        log_df[label] = np.log(df[label].astype(int) + 1)
    for i in df:
        if i not in numerical_values:
            log_df[i] = df[i]

    style.use('seaborn-poster')

    # Freq Distr of Likes, Dislikes, Views, and Comment Count (Log)
    fig, ax = plt.subplots(2, 2)
    plt.subplots_adjust(hspace=0.27, top=0.92)
    sns.distplot(log_df['dislikes'], bins=25, ax=ax[0][1], color='r')
    sns.distplot(log_df['likes'], bins=25, ax=ax[0][0], color='g')
    sns.distplot(log_df['views'], bins=25, ax=ax[1][0], color='y')
    sns.distplot(log_df['comment_count'], bins=25, ax=ax[1][1])
    plt.suptitle('Frequency Distributions of Likes, Dislikes, Views, and Comment Count (Log)', fontsize=20,
                 fontweight='bold')
    plt.savefig('Charts/FrequencyDistrsVideoAttr.png', bbox_inches='tight')
    plt.show()

    # Categories with like count
    fig, ax = plt.subplots()
    categories_and_likes = df.groupby(['category_id'])['likes'].sum().sort_values(ascending=False)

    ax = sns.barplot(y=[categories[str(i)] for i in categories_and_likes.index], x=categories_and_likes.values)
    for p in ax.patches:
        width = p.get_width()
        ax.text(width + 69999990,
                p.get_y() + p.get_height() / 2. + .1,
                np.format_float_scientific(int(width), precision=1, exp_digits=2),
                ha="center", fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.title('Categories and their Total Likes (Base 10)', fontweight='bold')
    plt.xlabel('Likes', fontweight='bold')
    plt.savefig('Charts/CategoriesLikes.png', bbox_inches='tight')
    plt.show()

    # Like Distr over categories
    unique_id = list(log_df['category_id'].unique())

    cat_list = [categories[str(i)] for i in unique_id]

    style.use('seaborn-poster')
    plt.suptitle('Like (Log) Distributions in Each Category', fontsize=20, fontweight='bold')
    sns.boxplot(y='category_id', x='likes', data=log_df, orient='h', palette='tab20c')
    plt.yticks(range(0, len(cat_list)), cat_list)
    plt.ylabel('Category', fontweight='bold')
    plt.xlabel('Likes (Log)', fontweight='bold')
    plt.savefig('Charts/LikesInCategory.png', bbox_inches='tight')
    plt.show()
