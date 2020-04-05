import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns


def eda(df, categories):
    style.use('seaborn-poster')
    numerical_values = ['likes', 'views', 'dislikes', 'comment_count']
    log_df = pd.DataFrame()

    for label in numerical_values:
        log_df[label] = np.log(df[label].astype(int) + 1)
    for i in df:
        if i not in numerical_values:
            log_df[i] = df[i]

    categories_and_comments = df.groupby(['category_id'])['comment_count'].sum().sort_values(ascending=False)

    ax = sns.barplot(y=[categories[str(i)] for i in categories_and_comments.index], x=categories_and_comments.values, ec='Black')
    for p in ax.patches:
        width = p.get_width()
        ax.text(width + 6990000,
                p.get_y() + p.get_height() / 2. + .1,
                np.format_float_scientific(int(width), precision=1, exp_digits=2),
                ha="center", fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.title('Categories and their Comment Counts (Base 10)', fontweight='bold')
    plt.xlabel('Comment Count', fontweight='bold')
    plt.savefig('Charts/CategoriesComments.png', bbox_inches='tight')
    plt.show()

    unique_id = list(log_df['category_id'].unique())
    plt.subplots_adjust(bottom=.35)
    cat_list = [categories[str(i)] for i in unique_id]

    plt.suptitle('Comment Count (Log) Distributions in Each Category', fontsize=20, fontweight='bold')
    sns.boxplot(x='category_id', y='comment_count', data=log_df)
    plt.xticks(range(0, len(cat_list)), cat_list, rotation=70)
    plt.ylabel('Comment Count (Log)', fontweight='bold')
    plt.xlabel('Category', fontweight='bold')
    plt.savefig('Charts/CommentsInCat.png')
    plt.show()
