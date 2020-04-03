import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style


def eda(df, categories):
    
    style.use('seaborn-poster')
    
    numerical_values = ['likes', 'views', 'dislikes', 'comment_count']
    log_df = pd.DataFrame()

    for label in numerical_values:
        log_df[label] = np.log(df[label].astype(int) + 1)
    for i in df:
        if i not in numerical_values:
            log_df[i] = df[i]

    # Categories with like count
    fig, ax = plt.subplots()
    categories_and_views = df.groupby(['category_id'])['views'].sum().sort_values(ascending=False)
    print(categories_and_views)
    ax = sns.barplot(y=[categories[str(i)] for i in categories_and_views.index], x=categories_and_views.values)

    for p in ax.patches:
        width = p.get_width()
        ax.text(width + 1929999999,
                p.get_y() + p.get_height() / 2. + .1,
                np.format_float_scientific(int(width), precision=1, exp_digits=2),
                ha="center", fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.title('Categories and their Total Views (Base 10)', fontweight='bold')
    plt.xlabel('Views', fontweight='bold')
    plt.savefig('Charts/CategoriesViews.png', bbox_inches='tight')
    plt.show()

    # Like Distr over categories
    unique_id = list(log_df['category_id'].unique())
    plt.subplots_adjust(bottom=.35)
    cat_list = [categories[str(i)] for i in unique_id]

    plt.suptitle('Views (Log) Distributions in Each Category', fontsize=20, fontweight='bold')
    sns.boxplot(x='category_id', y='views', data=log_df)
    plt.xticks(range(0, len(cat_list)), cat_list, rotation=70)
    plt.ylabel('Views (Log)', fontweight='bold')
    plt.xlabel('Category', fontweight='bold')
    plt.savefig('Charts/ViewsInCategory.png')
    plt.show()