import pandas as pd
import os
import DataCleaning as data_cleaning
from EDA import Trends as correlations, Likes as likes, Views as views
import json


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
                if '.json' not in name and 'USvideos.csv' in name:
                    print(name)
                    print(root + '/' + name)
                    temp = pd.read_csv(root + '/' + name, encoding='utf-8')
                    df = df.append(temp)

        df.to_pickle('Data/pickles/entire_df_pickle')

    else:
        df = pd.read_pickle('Data/pickles/entire_df_pickle')

    categories = dict()
    with open('Data/youtube-new/US_category_id.json') as json_file:
        data = json.load(json_file)
        for i in data['items']:
            categories[i['id']] = i['snippet']['title']

    df = data_cleaning.clean_data(df)

    # EDA
    correlations.eda(df)
    likes.likes_eda(df, categories)
    views.eda(df, categories)

if __name__ == '__main__':
    main()
