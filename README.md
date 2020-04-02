# Description
- I have a data set of 800,000 records that contains information on YouTube videos.
- This information ranges from the title, publishing date, views, comment count, likes, dislikes, and more.
- I will try to use the given features to predict attributes such as likes.

# EDA (WIP)

## Numerical Data Distribution


![image](Charts/FrequencyDistrsVideoAttr.png)
Each of the columns seems to have a nice and normal distribution with no outliers.
## Looking at the Data on Likes

### Likes and Categories
![image](Charts/CategoriesLikes.png)

I was surprised in seeing that Gaming wasn't higher up on the list.  

### Like Distribution in Categories
![image](Charts/LikesInCategory.png)
  
It's interesting to see what video types usually do well. All of the videos under the 'Shows' category have a high amount of likes and are usually consistent in the amount of likes they receive. 

## Correlations

Considering the first task I have in mind is to predict likes, that is going to require some sort of regression model.
Let's start off by seeing the pearson correlations between our numeric features to get a rough idea of the data I'm working with.  

![image](Charts/corr_matrix.png)  

- Views and comment count seems to strongly correlate with the number of likes. 
    - Especially comment count  
      
Initially, it was my prediction that comment count would correlate the strongest to likes. Views alone do not mean people liked the video  

I noticed that comment_count has some slight correlation with dislikes and views. I don't think that dislikes and views would be accurate enough in predicting comment count, so multicollinearity is not an issue at the moment.


