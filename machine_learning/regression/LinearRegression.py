from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV, ElasticNetCV
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import numpy as np
import math

def run(df):
    X = df[['comment_count', 'dislikes', 'views', 'comments_disabled', 'ratings_disabled']]
    Y = df['likes']

    scalar = StandardScaler()

    x_train, x_test, y_train, y_test = train_test_split(X, Y)

    x_train = scalar.fit_transform(x_train)

    x_test = scalar.transform(x_test)

    # Linear Regression
    lin_reg = LinearRegression()

    lin_reg.fit(x_train, y_train)
    y_pred = lin_reg.predict(x_test)
    y_pred = np.exp(y_pred)

    print('Regular Linear Regression:')
    print(f'MAE: {int(round(mean_absolute_error(y_test, y_pred))):,d} Likes')
    print(f'MSE: {int(round(mean_squared_error(y_test, y_pred))):,d} Likes')
    print()

    # Ridge Regression Param Tuning
    alphas = np.arange(0.1, 20.1, 0.1)
    params = dict({'alphas': [alphas]})
    ridge_grid = GridSearchCV(RidgeCV(), param_grid=params, refit=True, cv=5)

    ridge_regressor = grid_tune(ridge_grid, x_train, y_train)

    # Ridge Regression Testing

    print('Ridge Regression:')
    regression(ridge_regressor, x_test, y_test)
    print()

    # Lasso Regression Param Tuning
    lasso_grid = GridSearchCV(LassoCV(), param_grid=params, refit=True, cv=5)

    lasso_regressor = grid_tune(lasso_grid, x_train, y_train)

    # Lasso Regression Testing

    print('Lasso Regression:')
    regression(lasso_regressor, x_test, y_test)
    print()

    # ElasticNet Regression Param Tuning

    elastic_grid = GridSearchCV(ElasticNetCV(), param_grid=params, refit=True, cv=5)

    elastic_regressor = grid_tune(elastic_grid, x_train, y_train)

    # ElasticNet Regression Testing

    print('ElasticNet Regression:')
    regression(elastic_regressor, x_test, y_test)
    print()


def regression(model, x_test, y_test):

    y_pred = model.predict(x_test)

    y_pred = np.exp(y_pred)

    print(f'MAE: {int(round(mean_absolute_error(y_test, y_pred))):,d} Likes')
    print(f'MSE: {int(round(mean_squared_error(y_test, y_pred))):,d} Likes')


def grid_tune(grid, x_train, y_train):
    grid.fit(x_train, y_train)

    return grid.best_estimator_
