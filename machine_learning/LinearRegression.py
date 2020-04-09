from sklearn.linear_model import LinearRegression, RidgeCV
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import numpy as np
import math

def run(df):
    X = df[['comment_count', 'dislikes', 'views', 'comments_disabled', 'ratings_disabled']]
    Y = df['likes']

    x_train, x_test, y_train, y_test = train_test_split(X, Y)

    # Linear Regression
    lin_reg = LinearRegression()
    scalar = StandardScaler()

    x_train = scalar.fit_transform(x_train)
    x_test = scalar.transform(x_test)
    lin_reg.fit(x_train, y_train)
    y_pred = lin_reg.predict(x_test)
    y_pred = np.exp(y_pred)

    print('Regular Linear Regression:')
    print(f'MAE: {int(round(mean_absolute_error(y_test, y_pred)))}')
    print(f'MSE: {int(round(mean_squared_error(y_test, y_pred)))}')
    print()

    # Ridge Regression Param Tuning
    alphas = np.arange(0.1, 20.1, 0.1)
    params = dict({'alphas': [alphas]})
    ridge_grid = GridSearchCV(RidgeCV(), param_grid=params, refit=True, cv=5)

    ridge_regressor = grid_tune(ridge_grid, x_train, y_train)

    print('Ridge Regression:')
    regression(ridge_regressor, x_test, y_test)
    print()


def regression(model, x_test, y_test):

    y_pred = model.predict(x_test)

    y_pred = np.exp(y_pred)

    print(f'MAE: {int(round(mean_absolute_error(y_test, y_pred)))}')
    print(f'MSE: {int(round(mean_squared_error(y_test, y_pred)))}')


def grid_tune(grid, x_train, y_train):
    grid.fit(x_train, y_train)

    return grid.best_estimator_
