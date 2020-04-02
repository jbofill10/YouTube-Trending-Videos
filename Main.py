import pandas as pd
import os
import DataCleaning as data_cleaning
from EDA import Correlations as correlations


def main():

    if not os.path.isfile('Data/pickles/entire_df_pickle'):
        df = pd.DataFrame(columns=['video_id',
                                   'trending_date',
                                   'title',
                                   'channel_title',
                                   'category_id',
                                   'publish_time',
                                   'tags',
                                   'views',
                                   'likes',
                                   'dislikes',
                                   'comment_count',
                                   'thumbnail_link',
                                   'comments_disabled',
                                   'ratings_disabled',
                                   'video_error_or_removed',
                                   'description'])
        for root, dirs, files in os.walk('Data/youtube-new'):
            for name in files:
                if '.json' not in name and 'JP' not in name \
                        and 'KR' not in name and 'MX' not in name and 'RU' not in name:
                    print(name)
                    print(root + '/' + name)
                    temp = pd.read_csv(root + '/' + name, encoding='utf-8')
                df = df.append(temp)

        df.to_pickle('Data/pickles/entire_df_pickle')

    else:
        df = pd.read_pickle('Data/pickles/entire_df_pickle')

    df = data_cleaning.clean_data(df)

    correlations.eda(df)


if __name__ == '__main__':
    main()
